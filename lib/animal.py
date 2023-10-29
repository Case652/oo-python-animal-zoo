class Animal:
    all = []
    def __init__(self,species,weight,nickname,zoo):
        self.species = species
        self.weight = weight
        self.nickname = nickname
        self.zoo = zoo
        Animal.all.append(self)

    @property
    def nickname(self):
        return self._nickname

    @nickname.setter
    def nickname(self,nickname):
        if not hasattr(self,"_nickname"):
            self._nickname = nickname
        else:
            print("No")

    @property
    def species(self):
        return self._species

    @species.setter
    def species(self,species):
        if not hasattr(self,"_species"):
            self._species = species
        else:
            print("No")
    
    @classmethod
    def find_by_species(self,species):
        return [animal for animal in self.all if animal.species == species]
        
        # __repr__ tool to see things, debug uses
    def __repr__(self):
        return f'<Animal species="{self.species}" zoo_name="{self.zoo.name}" >'
