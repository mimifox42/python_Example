#evenOdd sorter
import random #importing random function to be used
def evenOdd(l):#taking the list to this function 
    print(l) #printing the list before 
    for x in l: # for loop to go through every number in the list 
        if(x%2 == 0): #go through the list and print the even on one side 
            print(x, "\n")
        else: #and vice versa for odd list
            print("\t", x, "\n") 
            
list_size = int(input("Enter a list size"))  #asking user input for a size of the list
list = []  #initating a list
for x in range(list_size): #a for loop that goes until it hits the list size number
    list.append(random.randint(1,100)) #adding a random number between 1-100 in this for loop
list.sort() #sorting the for loop 
evenOdd(list) #sending the list to the evenOdd function

#magic square
square = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] #initializing a 2d array square
for x in range(9): #because the square had 9 values I am runnign the for loop 9 times
    r = int(input("What row value?")) #to change the valie in the square I am first asking the user what row they want to change
    c= int(input("What column value?")) #and column
    square[r][c] = int(input("What number?")) #once the user enters the spot they want to add a number I will ask them to enter a number


def magicSquare(square): #for it to be a magic square all values must be equal so I am checking that in this function
	row1 = square[0][0] + square[0][1] + square[0][2] 
	row2 = square[1][0] + square[1][1] + square[1][2]
	row3 = square[2][0] + square[2][1] + square[2][2]
	line1 = square[0][0] + square[1][0] + square[2][0]
	line2 = square[0][1] + square[1][1] + square[2][1]
	line3 = square[0][2] + square[1][2] + square[2][2]
	diag1 = square[0][0] + square[1][1] + square[2][2]
	diag2 = square[0][2] + square[1][1] + square[2][0]

	if (row1 == row2 == row3 == line1 == line2 == line3 == diag1 == diag2): #if they are all equal then it is a magic square
		print("This is a magic square")
	else: #if not then it is not a magic square
		print("This is not a magic square")

magicSquare(square) #running the function