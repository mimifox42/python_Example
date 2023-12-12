#example 15
def calc_average (t1, t2, t3, t4, t5): #saetting 5 variables that are test score values
    total = (t1 + t2 + t3 +t4 +t5)/5 # to calc average it must be addded up and then divided by the number of tests
    print(total)
def determine_grade(t1, t2, t3, t4, t5):
    for num in t1, t2, t3, t4, t5: #going through each test score
        if(num >=90 and num <=100): #each number will go through and print the number grade 
            print("A")
        elif(num >=80 and num <=89):
            print("B")
        elif(num >=70 and num <=79):
            print("C")
        elif(num >=60 and num <=69):
            print("D")
        elif(num < 60):
            print("F")
      
            
test1 = int(input("Enter your first test grade ")) #user input for 5 grades
test2 = int(input("Enter your second test grade "))
test3 = int(input("Enter your third test grade "))
test4 = int(input("Enter your fourth test grade "))
test5 = int(input("Enter your fifth test grade "))
determine_grade(test1, test2, test3, test4, test5)
calc_average(test1,test2,test3,test4,test5) #putting these values into the cal_average function

#example17
def is_prime(n):
    for x in range(2, n): #running through all numbers  until the number given
        if(n % x) == 0: #if it is not a prime it will have another number that is divisble by
            print("False")
            break
        else: #if no other number is divisble it is a prime and will print true
            print("True")
            break

num = int(input("Enter a number")) #getting input from user
is_prime(num) #running the function using the number from the user