#Exercise4
num = int(input("Enter a number between 1-10"))
if(num == 1): #if statements that will check numbers from one to ten and display the roman numeral associated with it
     print("|")
elif(num == 2):
     print("||")
elif(num == 3):
    print("|||")
elif(num == 4):
    print("|V")
elif(num == 5):
    print("V")
elif(num == 6):
    print("V|")
elif(num == 7):
    print("V||")
elif(num == 8):
    print("V|||")
elif(num == 9):
    print("|X")
elif(num == 10):
    print("X")
else: #if the number is out of range an error message will show
    print("Number not in range")
    
#exercise 16
year = int(input("Enter a year")) 

if((year%400 == 0)or((year%4 ==0)and(year%100 != 0))):
    print("29 days") #if the year fits in the if statement it is considered a leap year and will have a feburary that is 29 days

else:  #if not it will have 28 days
    print("28 days")