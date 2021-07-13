import random


def random_phone():
  str1 = '1234567890'
  ls = list(str1)
  random.shuffle(ls)
  psw = ''.join([random.choice(ls) for x in range(10)])
  ex3 = psw
  return ex3


random_phone()