class car:
 def __init__(self, make, model, year, color):
  #self.make = make
  #self.model = model
  #self.year = year
  #self.color = color
  #self.started = False
  #self.speed = 0
 #self.max_speed = 200

#1
def __str__(self):
    return f"{self.make} {self.model} {self.color} ({self.year})"

@classmethod
def change_showroom(cls, new_name):
    cls.showroom = new_name

@staticmethod
def show_intro_message():
    print("This class represents a car and its properties.")

#1
toyota_camry = car("Toyota", "Camry", 2022, "Red" )

print("(a) Toyota Camry attributes:")
print("Make:", toyota_camry.make)
print("Model:", toyota_camry.model)
print("Year:", toyota_camry.year)
print("Color:", toyota_camry.color)
print("Started:", toyota_camry.started)
print("Speed:", toyota_camry.speed)
print("Maximum speed:", toyota_camry.max_speed)

#2 create ford_mustang
ford_mustang= car("ford","mustang",2022,"black")
print("\n(b) ford mustang attributes:")
print("make:",ford_mustang.make)
print("Model:", ford_mustang.model)
print("Year:", ford_mustang.year)
print("Color:", ford_mustang.color)
print("Started:", ford_mustang.started)
print("Speed:", ford_mustang.speed)
print("Maximum speed:", ford_mustang.max_speed)

#3
print(car.make)
except AttributeError as error:
print("\n(c) Error:", error)

#4 display class dictionary
print(car.make)
except AttributeError as error:
print("\n(c) Error:", error)

#5 add and change the showroom attribute
car.showroom = "NewAge"

print("\n(e) Showroom:", car.showroom)

car.change_showroom("City Motors")
print("Updated showroom:", car.showroom)
print("Updated class dictionary:", car.dict)
#6
car.showroom = "NewAge"

print("\n(e) Showroom:", car.showroom)

car.change_showroom("City Motors")
print("Updated showroom:", car.showroom)
print("Updated class dictionary:", car.dict)

#7
print("\n(f) Toyota instance dictionary:")
print(toyota_camry.dict)

#8
print("\n(g) Toyota string:", str(toyota_camry))
print("Ford string:", str(ford_mustang))

#9
print("\n(g) Toyota string:", str(toyota_camry))
print("Ford string:", str(ford_mustang))