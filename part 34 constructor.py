class Point():
  def __init__(self, x, y):
    self.x = x 
    self.y = y

  def move(self):
    print("move")

  def draw(self):
    print("draw")

point = Point(10,20)
print(point.x)

class Person():
  def __init__(self, name):
    self.name = name
  
  def talk(self):
    print(f"Hello {self.name}, Nice to meet you!")

person = Person("Boy")
person.talk()
