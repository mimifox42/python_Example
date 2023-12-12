def recursive_list(list, start, end):#going through the elements in a list 
    if start > end: #if the list has gone through each element in the list end the recursive function
        return 0
    else:
        return list[start] + recursive_list(list, start+1, end) #add the first element in the list to the rest fo them, and adding one to start value to reach each number
        
list = [2,3,4,5,6] #defining the list
print(recursive_list(list, 0,4)) #printing the total sum of the list with the starting and ending values