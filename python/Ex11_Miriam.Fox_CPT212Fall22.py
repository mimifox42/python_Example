#most frequent character
stri = input("Enter a string").lower() #user input for a string

count = 0 #initializing the counter to keep track of how many times a letter appears in a string
most_frequent_character = " " #initializing the character to " " and this will keep track of the most frequent character

for x in stri: #goign through each letter in the string
    if x.isascii(): #if statement to make sure its an ascii character 
        if stri.count(x)>count: #automatically the first character will be mentioned more then zero times but after that it will check to find the most used char
            count = stri.count(x) #counting the amount  of times the char is in the string
            most_frequent_character = x #getting the char that is most frequent 
print("The character",most_frequent_character, "occurs in",stri, count, "times") #printing out the most frequent char and the maount of times its present 

#average # of words / sentence
file = open("text.txt", "r") #opening the file to read from it
lines = 0 #initializing the lines to 0 so I could count them
for line in file: #for loop to go through each line in file and add one as it loops 
    lines+=1 
file.close() #close the file
file = open("text.txt", "r") #reopen the file 
file_open = file.read() #assigning it to a string variable
total = file_open.split()#spliting the file by each empty space

   
print(len(total) // lines)#printing the average words per line by dividing the total words by the number of lines