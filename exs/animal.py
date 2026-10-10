class animal:
    def __init__(self, animal):
        self.animal = animal

    def andar(self):
        print(f"{self.animal} está andando ")

    def nadar(self):
        print(f"{self.animal} está nadando")
    
    def falar(self):
        print(f"{self.animal} está falando: https://www.youtube.com/watch?v=hW6cl36H93c")

animal1 = animal("Cavalo")
animal2 = animal("Hipopótamo")
animal3 = animal("Lagarta")

print(f"animal: {animal1.animal} : {animal}")
print(f"animal: {animal2.animal} : {animal}")
print(f"animal: {animal3.animal} : {animal}")


animal1.andar()
animal2.nadar()
animal3.falar()
