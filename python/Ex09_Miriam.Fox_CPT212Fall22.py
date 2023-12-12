num = 12 #setting up my number variable 
list = [10, 20, 42, 3, 6, 2, 43, 2] #creating my list

def largerThanN(n, list): #creating the function to print any number larger than n
    for x in list: #for every number in the list
        if x > n:  #if it is greater than n
            print(x) #it should be printed
        
largerThanN(num, list) #calling my variable

#wordlist 
import sys #in order for my program to end  
wordList = [] #initializing my wordlist
user1 = input("Enter word") #user input for five words
user2 = input("Enter word")
user3 = input("Enter word")
user4 = input("Enter word")
user5 = input("Enter word")
count = 1 #setting up a counter to print the number alongside the word
for word in user1, user2, user3, user4, user5:
    wordList.append(word) #or loop to add words to wordlist
    print(count, " ", word)
    count+=1 #increasing the counter by one each iteration
swap = "y" #initializing my swap variable
def swap_function(wordList): 
        swap = input("Do you want to swap?") #asking user if they want to swap words
        if(swap.upper() == "Y"): #if the response is y
           firstSwap = int(input("Enter the first number to swap?")) #enter two numbers to swap
           secondSwap = int(input("Enter the second number to swap?"))
           temp= wordList[firstSwap-1] #temperary value to hold the swapped values
           temp2 =wordList[secondSwap-1]
           wordList[firstSwap-1] = temp2 #swapping those values
           wordList[secondSwap-1] = temp
           c = 1
           for word in wordList:
            print(c, " ", word)
            c+=1 #and printing the swapped wordlist
        else: # if the user does not answer y then the program closes
            print("Program finished")
            sys.exit()

while (swap.upper()=="Y"): #while loop to run while the swap value = y
    swap_function(wordList)
        
    




  