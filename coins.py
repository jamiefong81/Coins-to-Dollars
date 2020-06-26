#!/bin/python3

#A try except block in case someone puts in letters or symbols
try:
        def main():
            #Ask how many of each coins they have
            quarters = float(input("How many quarters do you have?\n"))
            dimes = float(input("How many dimes do you have?\n"))
            nickels = float(input("How many nickels do you have?\n"))
            pennies = float(input("How many pennies do you have?\n"))
            #Defining values
            q = float(0.25)
            d = float(0.1)
            n = float(0.05)
            p = float(0.01)
            #Converison
            fquarters = quarters * q
            fdimes = dimes * d
            fnickels = nickels * n
            fpennies = pennies * p
            print("You have $" + str(fquarters + fdimes + fnickels + fpennies))

        main()

except:
    print("Invalid Option")
