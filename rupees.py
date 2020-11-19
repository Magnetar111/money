#Input Part:
while (True):
    country = int(input('''Country: 1.India
         2.America \n'''))
    currency = int(input('''In which currency: 1.According to country
                   2.Rs to $
                   3.$ to Rs \n''' ))
    try:
        n = float(input("Cash owed:"))

    except:
        print("plzz Enter the number")
    if (n < 0):
        n = float(input("Cash owed:"))
        n = round(n * 100)

    #main function Indian:
    def cash(n):
        print("Total Rs", n)
        c = 0
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
        print("COUNT", c, "\n")

    #main function American:
    def cash2(n):
        print("Total $", n)
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
        print("COUNT", c, "\n")

    #for currency 1:
    if (country == 1 and currency == 1):
        cash(n)
    elif (country == 2 and currency == 1):
        cash2(n)

    #currency 2:
    elif (country == 1 and currency == 2):
        #Rs to $
        m = int(n / 74.23) #According to 19/11/20 1$ = Rs74.23
        n = m
        cash2(n)
    elif (country == 2 and currency == 2):
        #Rs to $
        m = int(n / 74.23) #According to 19/11/20 1$ = Rs74.23
        n = m
        cash2(n)

    #currency 3:
    elif (country == 1 and currency == 3):
        #$ to Rs
        m = int(n * 74.23)
        n = m
        cash(n)
    elif (country == 2 and currency == 3):
        #$ to rs
        m = int(n * 74.23)
        n = m
        cash(n)
