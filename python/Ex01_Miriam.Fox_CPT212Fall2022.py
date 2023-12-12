#exercise4 
item1 = float(input("Whats the price for item1?"))
item2 = float(input("Whats the price for item2?"))
item3 = float(input("Whats the price for item3?"))
item4 = float(input("Whats the price for item4?"))
item5 = float(input("Whats the price for item5?"))
total = item1+item2+item3+item4+item5
salesTax = total * 0.07
completeTotal = total + salesTax
print(total)
print(salesTax)
print(completeTotal)

#exercise9
weather = float(input("Enter a temperature in Celsius"))
F = (9/5)*weather + 32
print(F)

#exercise14
p = float(input("Enter principal amount"))
r = float(input("Enter annual interest rate"))
n = float(input("Enter number of times the interest is compounded"))
t= float(input("Enter the number of years the account will be left to earn interest"))

total = p * (1+r/n) ** (n*t)

print(total)