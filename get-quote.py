import random
def principal():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1
  rnd = random.randint(0, last)
  x = 0
  while(x <= 1):
      print(quotes[rnd])
      x += 1
      rnd = random.randint(0, last)
if __name__== "__main__":
  principal()
