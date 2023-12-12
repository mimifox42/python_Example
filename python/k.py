import sys 
wordList = []
user1 = input("Enter word")
user2 = input("Enter word")
user3 = input("Enter word")
user4 = input("Enter word")
user5 = input("Enter word")
count = 1
for word in user1, user2, user3, user4, user5:
    wordList.append(word)
    print(count, " ", word)
    count+=1
swap = "y"
def swap_function(wordList): 
        swap = input("Do you want to swap?")
        if(swap.upper() == "Y"):
           firstSwap = int(input("Enter the first number to swap?"))
           secondSwap = int(input("Enter the second number to swap?"))
           temp= wordList[firstSwap-1]
           temp2 =wordList[secondSwap-1]
           wordList[firstSwap-1] = temp2
           wordList[secondSwap-1] = temp
           c = 1
           for word in wordList:
            print(c, " ", word)
            c+=1
        else:
            print("Program finished")
            sys.exit()

while (swap.upper()=="Y"):
    swap_function(wordList)
        
    




  