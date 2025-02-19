from oop import myobj


class Cars:
    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    def display (self):
        print(f"My car is a {self.color} {self.make},{self.model} manufactured in {self.year}")

myobj=Cars("Ford","Raptor",2024,"blue")
myobj.display()
myobj2=Cars("Bugatti","Centroclieci",2023,"black")
myobj2.display()
myobj3=Cars("Audi","R8",2025,"white")
myobj3.display()
myobj4=Cars("Jeep","Wrangler",2024,"red")
myobj4.display()
myobj5=Cars("Lotus","Emira",2022,"blue")
myobj5.display()