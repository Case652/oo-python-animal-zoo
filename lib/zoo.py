from lib.animal import Animal
class Zoo:

    all = []

    def __init__(self,name="NY ZOO",location="NYC"):
        self.name = name
        self.location = location
        Zoo.all.append(self)

    @property
    def animals(self):
        return [animal for animal in Animal.all if animal.zoo == self]
        
    def animals_species(self):
        return list({animal.species for animal in self.animals()})
        # return A unique List of species 
    # alternativly =
    @property
    def animal_species(self):
        species = []
        for animal in self.animals:
            if animal.species not in species:
                species.append(animal.species)
        return species

    def find_by_species(self,species):
        return [animal for animal in self.animals if animal.species == species]
        # return A list of animals from a searched species
    @property
    def animal_nicknames(self):
        return [animal.nickname for animal in self.animals]

    @classmethod
    def find_by_location(self,location):
        return [zoo for zoo in self.location if zoo.location == location]
        
    def __repr__(self):
        return f'<Zoo name="{self.name}" location="{self.location}" >'

    