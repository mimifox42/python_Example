#example 3
def recursive_lines(n): #defining the function and calling number of rows that this should have
    if n == 0: #if n is less than or equal to zero the program should end 
        return 0
    else: #if n is greater than zero it should 
        recursive_lines(n-1) #minus one from n in order to use recursive 
        print("*" * n) #and print out the n number of stars
    
print(recursive_lines(10)) #calling the fucntion to print out the stars
   
#example4
def largest_list(list, start, end): #defining the function
    if start == end:#if the list has gone through all elements or the list has one value
        return list[start, end] #return the highest value or the first if theres only one
    else:
        first = list[start]#defining the first variable to first num in list
        second = list[start + 1] #second number to second element of the list
        if first > second: #if first is greater than second then return first as a larger num
            return first
        else: #vice versa for the second
            return second



print(largest_list([23, 234, 7, 89, 100], 0, 4) ) #printing the returning value of a list with 5 elements

#example5
def recursive_list(list, start, end):#going through the elements in a list 
    if start > end: #if the list has gone through each element in the list end the recursive function
        return 0
    else:
        return list[start] + recursive_list(list, start+1, end) #add the first element in the list to the rest fo them, and adding one to start value to reach each number
        
list = [2,3,4,5,6] #defining the list
print(recursive_list(list, 0,4)) #printing the total sum of the list with the starting and ending values