import random


class ON:
  def __init__(self, year, age, block):
    self.year = year
    self.age = age
    self.block = block

  def random_play(self):
    a = 5
    b = random.randrange(0, 6)
    if b == a:
      print("*-*-*-*-*-*-*-*-*-*-*-*-*-*")
      print("You Win!")
      print("Your number is: 5")
      print("*-*-*-*-*-*-*-*-*-*-*-*-*-*")

    else:
      print("You Lose!")
      print("Your number is: " + str(b))


it = ON.random_play(True)