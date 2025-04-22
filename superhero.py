class Superhero:
    def __init__(self, name, power, universe):
        self.name = name
        self.power = power
        self.universe = universe

    def introduce(self):
        return f"I am {self.name} from {self.universe}, and my power is {self.power}!"

# Subclass
class Mutant(Superhero):
    def __init__(self, name, power, universe, mutation_type):
        super().__init__(name, power, universe)
        self.mutation_type = mutation_type

    def introduce(self):
        return f"I am {self.name}, a mutant from {self.universe} with {self.mutation_type} abilities!"

# Example usage
if __name__ == "__main__":
    hero = Superhero("Wonder Woman", "Super Strength", "DC")
    mutant = Mutant("Storm", "Weather Control", "Marvel", "Elemental")

    print(hero.introduce())
    print(mutant.introduce())
