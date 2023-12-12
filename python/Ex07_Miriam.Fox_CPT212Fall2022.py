def is_prime(number):
        for x in range(2, number): #going through all the numbers between 2 and the number to check if it is divisible 
            if(number % x == 0): #in any number is divisible by anything but itself and 2 it is not prime
                return False
            
        return True #otherwise it is and will be printed
for number in range(2,101):
    if(is_prime(number)== True): #if the fucntion returned true it should print
        print(number)
    else:
        continue



