class Animals:
  def name_of_animals(self, name):
    self.name_of_animals = name
  def life(self):
    print("life")
    

class Vivipar(Animals):
  def give_birth(self):
    print(f"{self.name_of_animals} is an Animal will give birth for breeding ")


class Ovipar(Animals):
  def lay_eggs(self):
    print(f"{self.name_of_animals} is an Animal will lay eggs for breeding")


class Ovovivipar(Animals):
  def hybrid(self):
    print(f"{self.name_of_animals} is an Animal will lay eggs and give birth for breeding")


dog = Vivipar()
dog.name_of_animals("Dog")
dog.give_birth()
dog.life()

bird = Ovipar()
bird.name_of_animals("Bird")
bird.lay_eggs()
bird.life()

stingray = Ovovivipar()
stingray.name_of_animals("Stingray")
stingray.hybrid()
stingray.life()