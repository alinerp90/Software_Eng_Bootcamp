# Program to use a calculator based on the user choice

""""
For investment:
1. (P) Input the amount of money that they are depositing.
2. (r)Input the interest rate (as a percentage). Only the number of the interest rate should be entered.
3. (t)Input the number of years they plan on investing.
4. Then ask the user to input if they want “simple” (A = P *(1 + r*t)) or “compound” (A = P * math.pow((1+r),t))
interest, and store this in a variable called interest. 

For bond:
1. (P)Input present value of the house
2. (i) = (I/100) /12 Input interest rate(I) in number
3. (n) Input number of months they plan to repay the bond
"""

import math

print("Welcome, please choose one of the below:")
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")
print(" ")

response = input("Please enter either 'investment' or 'bond' to choose which calculation you want to do: ")
calculation = response.upper()

if calculation == "INVESTMENT":
    P = int(input("Please insert in number the amount of money that you want to deposit: "))
    R = int(input("Please insert only the number of the interest rate choose: "))
    r = R / 100
    t = int(input("Please insert the number of year that you are planing on invest: "))
    interest = input("Please enter either 'simple' or 'compound' interest: ")
    interest = interest.upper()

    if interest == "SIMPLE":
        A = P * (1 + r * t)
        print(A)

    elif interest == "COMPOUND":
        A = P * math.pow((1 + r), t)
        print(A)

    else:
        print("please enter a valid interest.")

elif calculation == "BOND":
    P = int(input("Please insert the present value of the house: "))
    I = int(input("Please insert the interest rate in number: "))
    n = int(input("Please insert the number of months that you are planing to repay the bond: "))
    i = (I / 100) / 12
    repayment = (i * P) / (1 - (1 + i) ** (-n))
    print(repayment)

else:
    print("Please enter a valid value")
