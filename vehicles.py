class Vehicle:
    def move(self):
        return "Moving..."

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚢"

# Example usage
if __name__ == "__main__":
    car = Car()
    plane = Plane()
    boat = Boat()

    print(car.move())
    print(plane.move())
    print(boat.move())
