# Define a function to print a value
class Point:
  def draw(self):
    print("Draw")

  
  def move(self):
    print("Move")

# Turning classes into objects
point1 = Point()
point1.x = 12
point1.draw()
print(point1.x)
Point().move