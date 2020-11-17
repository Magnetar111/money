# money
#It's a python program based on greedy algorithm.

#Input part:
n = int(input('''Country: 1.India
         2.America \n'''))
c = int(input('''In which currency: 1.Rs to Rs
                   2.$ to $
                   3.Rs to $
                   4.$ to Rs \n''' ))
a = int(input('Enter amount:'))


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
      print("2000")
   while(n>= 500):
      c = c + 1
      n = n - 500
      print("500")
   while(n>= 200):
      c = c + 1
      n = n - 200
      print("200")
   while(n>=100):
      c = c + 1
      n = n - 100
      print("100")
   while(n>=50):
      c = c + 1
      n = n - 50
      print("50")
   while(n>=20):
      c = c + 1
      n = n -20
      print("20")
   while(n>=10):
      c = c + 1
      n = n - 10
      print("10")
   while(n>=5):
      c = c + 1
      n = n - 5
      print("5")
   while(n>=2):
    c = c + 1
    n = n - 2
    print("2")
   while(n>0):
    c = c + 1
    n = n - 1
    print("1")
   print(c," COUNT ")
