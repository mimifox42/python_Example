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