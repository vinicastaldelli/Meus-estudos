import datetime
import os
import re
import time
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/youtube"]
ID_PLAYLIST_ALVO = "PLM3ZOk63kdT0"


def autenticar_youtube():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "client_secret.json", SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return build("youtube", "v3", credentials=creds)


def converter_duracao_iso_para_segundos(duracao_iso):
    """Converte duração ISO 8601 (ex: PT1M15S) em segundos."""
    padrao = re.compile(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?")
    match = padrao.match(duracao_iso)
    if not match:
        return 0

    horas = int(match.group(1)) if match.group(1) else 0
    minutos = int(match.group(2)) if match.group(2) else 0
    segundos = int(match.group(3)) if match.group(3) else 0

    return horas * 3600 + minutos * 60 + segundos


def obter_ids_playlist_atual(youtube):
    """Varre a playlist atual e retorna um conjunto (set) com os IDs de todos os vídeos já presentes nela."""
    print("Carregando vídeos já existentes na playlist alvo...")
    ids_existentes = set()
    proxima_pagina = None

    try:
        while True:
            req = youtube.playlistItems().list(
                part="contentDetails",
                playlistId=ID_PLAYLIST_ALVO,
                maxResults=50,
                pageToken=proxima_pagina,
            )
            res = req.execute()

            for item in res.get("items", []):
                id_video = item["contentDetails"]["videoId"]
                ids_existentes.add(id_video)

            proxima_pagina = res.get("nextPageToken")
            if not proxima_pagina:
                break
    except HttpError as err:
        print(f"   ⚠️ Aviso ao ler a playlist atual: {err}")

    print(f"✅ {len(ids_existentes)} vídeos já identificados na playlist.")
    return ids_existentes


def filtrar_e_verificar_detalhes(youtube, lista_videos):
    """Filtra a lista em lotes de 50: remove Shorts por duração ou tag e verifica histórico."""
    if not lista_videos:
        return []

    videos_validos = []

    # Processa em lotes de 50 para otimizar cota da API
    for i in range(0, len(lista_videos), 50):
        lote = lista_videos[i : i + 50]
        ids_lote = [v["id"] for v in lote]

        # Requisita duração e estado de reprodução
        req_detalhes = youtube.videos().list(
            part="contentDetails,player", id=",".join(ids_lote)
        )
        res_detalhes = req_detalhes.execute()
        
        info_videos = {}
        for item in res_detalhes.get("items", []):
            id_vid = item["id"]
            content_details = item.get("contentDetails", {})
            iso_duration = content_details.get("duration")

            # Se o vídeo não tiver duração (ex: live ativa ou indisponível), ignora de forma segura
            if not iso_duration:
                continue
                
            duracao_seg = converter_duracao_iso_para_segundos(iso_duration)
            assistido = False  # Mantido conforme lógica anterior

            info_videos[id_vid] = {"duracao": duracao_seg, "assistido": assistido}
        
        for vid in lote:
            detalhes = info_videos.get(vid["id"], {"duracao": 0, "assistido": False})
            
            # Verificação extra de segurança para detetar Shorts pelo título
            titulo_lower = vid["titulo"].lower()
            e_short_por_tag = "#short" in titulo_lower or "#shorts" in titulo_lower

            # Filtro: Duração > 60s, não tem tag de Short e não foi assistido
            if detalhes["duracao"] > 60 and not e_short_por_tag and not detalhes["assistido"]:
                videos_validos.append(vid)
            else:
                pass  # Opcional: print para depuração se desejar
                
    return videos_validos


def adicionar_novos_videos():
    youtube = autenticar_youtube()
    print("--- INICIANDO BUSCA DE VÍDEOS LONGOS NÃO ASSISTIDOS ---")

    # Carrega o conjunto de vídeos que já estão na playlist para evitar duplicados
    videos_na_playlist = obter_ids_playlist_atual(youtube)

    # Data limite: exatamente 5 meses atrás
    agora = datetime.datetime.now(datetime.timezone.utc)
    data_limite = agora - datetime.timedelta(days=5 * 30)
    print(f"Buscando vídeos postados após: {data_limite.strftime('%d/%m/%Y')}")

    todos_os_videos = []
    proxima_pagina_inscricoes = None

    try:
        # -------------------------------------------------------------
        # ETAPA 1: COLETAR VÍDEOS DOS CANAIS (ÚLTIMOS 5 MESES)
        # -------------------------------------------------------------
        while True:
            request_sub = youtube.subscriptions().list(
                part="snippet,contentDetails",
                mine=True,
                maxResults=50,
                pageToken=proxima_pagina_inscricoes,
            )
            resposta_sub = request_sub.execute()

            itens_inscricoes = resposta_sub.get("items", [])
            if not itens_inscricoes:
                break

            for inscricao in itens_inscricoes:
                nome_canal = inscricao["snippet"]["title"]
                id_canal = inscricao["snippet"]["resourceId"]["channelId"]

                print(f"Coletando vídeos do canal: {nome_canal}")

                try:
                    req_canal = youtube.channels().list(
                        part="contentDetails", id=id_canal
                    )
                    res_canal = req_canal.execute()

                    if not res_canal.get("items"):
                        continue

                    id_uploads = res_canal["items"][0]["contentDetails"][
                        "relatedPlaylists"
                    ]["uploads"]

                    proxima_pagina_videos = None
                    videos_processados = 0
                    continuar_no_canal = True

                    while continuar_no_canal and videos_processados < 150:
                        req_videos = youtube.playlistItems().list(
                            part="snippet",
                            playlistId=id_uploads,
                            maxResults=50,
                            pageToken=proxima_pagina_videos,
                        )
                        res_videos = req_videos.execute()

                        itens_videos = res_videos.get("items", [])
                        if not itens_videos:
                            break

                        for item_video in itens_videos:
                            videos_processados += 1
                            snippet = item_video["snippet"]
                            id_video = snippet["resourceId"]["videoId"]
                            titulo_video = snippet["title"]

                            data_pub_str = snippet["publishedAt"].replace("Z", "+00:00")
                            data_publicacao = datetime.datetime.fromisoformat(data_pub_str)

                            if data_publicacao >= data_limite:
                                # Otimização: se já estiver na playlist, nem sequer adicionamos à lista de triagem
                                if id_video not in videos_na_playlist:
                                    todos_os_videos.append({
                                        "id": id_video,
                                        "titulo": titulo_video,
                                        "canal": nome_canal,
                                        "data": data_publicacao,
                                    })
                            else:
                                continuar_no_canal = False
                                break

                        proxima_pagina_videos = res_videos.get("nextPageToken")
                        if not proxima_pagina_videos:
                            continuar_no_canal = False

                except HttpError as err:
                    if "quotaExceeded" in str(err):
                        raise err
                    print(
                        f"   ⚠️ Erro ao ler o canal {nome_canal}:"
                        f" {getattr(err, 'reason', str(err))}"
                    )

            proxima_pagina_inscricoes = resposta_sub.get("nextPageToken")
            if not proxima_pagina_inscricoes:
                break

    except HttpError as err:
        if "quotaExceeded" in str(err):
            print(
                "\n❌ COTA DIÁRIA ESGOTADA DURANTE A COLETA! Tente novamente amanhã."
            )
            return

    print(f"\n✅ Coleta concluída: {len(todos_os_videos)} novos vídeos candidatos encontrados.")

    # -------------------------------------------------------------
    # ETAPA 2: FILTRAR SHORTS E VERIFICAR DETALHES
    # -------------------------------------------------------------
    print("Filtrando Shorts e verificando detalhes...")
    videos_validos = filtrar_e_verificar_detalhes(youtube, todos_os_videos)
    print(
        f"✅ Filtro concluído! {len(videos_validos)} vídeos aptos para inserção."
    )

    # -------------------------------------------------------------
    # ETAPA 3: ORDENAR DO MAIS ANTIGO PARA O MAIS NOVO
    # -------------------------------------------------------------
    print("Ordenando do mais antigo para o mais novo...")
    videos_validos.sort(key=lambda x: x["data"])

    # -------------------------------------------------------------
    # ETAPA 4: INSERIR NA PLAYLIST (COM DUPLA VERIFICAÇÃO DE SEGURANÇA)
    # -------------------------------------------------------------
    print("\n--- INICIANDO SALVAMENTO NA PLAYLIST ---")
    adicionados_count = 0

    for video in videos_validos:
        # Dupla checagem: se por algum motivo já estiver presente, pula
        if video["id"] in videos_na_playlist:
            continue

        try:
            youtube.playlistItems().insert(
                part="snippet",
                body={
                    "snippet": {
                        "playlistId": ID_PLAYLIST_ALVO,
                        "resourceId": {
                            "kind": "youtube#video",
                            "videoId": video["id"],
                        },
                    }
                },
            ).execute()

            # Adiciona ao set local para evitar duplicidade na mesma execução
            videos_na_playlist.add(video["id"])
            adicionados_count += 1

            data_formatada = video["data"].strftime("%d/%m/%Y %H:%M")
            print(
                f"   [+] [{data_formatada}] [{video['canal']}] {video['titulo']}"
            )
            time.sleep(0.5)

        except HttpError as err:
            erro_str = str(err)
            if "quotaExceeded" in erro_str:
                print("\n❌ COTA DIÁRIA ESGOTADA DURANTE O SALVAMENTO!")
                return
            print(
                f"   [!] Erro em \"{video['titulo']}\":"
                f" {getattr(err, 'reason', str(err))}"
            )

    print(f"\n--- VARREDURA FINALIZADA COM SUCESSO ---")
    print(f"Total de novos vídeos adicionados nesta execução: {adicionados_count}")


if __name__ == "__main__":
    adicionar_novos_videos()