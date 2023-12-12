largestNum = float('-inf')#because I do not know where the numbers will start this guarantees that the first value will be the largest until another one is larger, same thing for the smallest value
smallestNum = float('inf') #
file = open('randnums.txt', 'r')#opening the file to read the values
for line in file:#looping to read every line of the file
    num = int(line) #converting the line to int in order to compare the values
    if(num > largestNum):# if the num is greater then the value stored in largestNum the number should be replaced to it 
        largestNum = num
    if(num < smallestNum):#if the number on the line is smaller then the value in smallestNum the value should be replaced
        smallestNum = num
print("The largest value is ", largestNum)#printing both values after the loop is finished
print("The smallest value is ", smallestNum)

    
    