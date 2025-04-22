# superhero.py

class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self._power = power      # protected attribute (encapsulation)
        self.city = city

    def use_power(self):
        print(f"{self.name} uses {self._power} to protect {self.city}!")

    def reveal_identity(self):
        return f"{self.name} is a superhero in {self.city}."


# Subclass (Inheritance + Polymorphism)
class FlyingHero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed

    def use_power(self):  # Polymorphism: override method
        print(f"{self.name} flies at {self.flight_speed} km/h and uses {self._power} to save {self.city}!")
