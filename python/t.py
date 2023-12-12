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