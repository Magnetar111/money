# money
#It's a python program based on greedy algorithm.

while True:
   try:
    n = float(input("Cash owed:"))
   except:
    print("plzz Enter the number")
   c = 0
   if (n < 0):
     n = float(input("Cash owed:"))
     n = round(n * 100)
   while(n>=2000):
      c = c + 1
      n = n - 2000
      print("$")
   while(n>= 500):
      c = c + 1
      n = n - 500
      print("&")
   while(n>= 200):
      c = c + 1
      n = n - 200
      print("@")
   while(n>=100):
      c = c + 1
      n = n - 100
      print("!")
   while(n>=50):
      c = c + 1
      n = n - 50
      print("?")
   while(n>=20):
      c = c + 1
      n = n -20
      print("*")
   while(n>=10):
      c = c + 1
      n = n - 10
      print("^")
   while(n>=5):
      c = c + 1
      n = n - 5
      print("%")
   while(n>=2):
    c = c + 1
    n = n - 2
    print(">>")
   while(n>0):
    c = c + 1
    n = n - 1
    print("<<")
   print(c," COUNT ")
