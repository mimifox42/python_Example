name = input("Enter your Name: ") #user will enter their name and golf score
golfScore= input("Enter your golf score:")

golf_file = open('golf.txt', 'a') #open the file with the append to add to the exisiting information and not write over it
golf_file.write("\n") # skip a line between records and write name and golfscore
golf_file.write(name)
golf_file.write(' ')
golf_file.write(golfScore)
golf_file.close()
golf_file = open('golf.txt', 'r') #open the file to read all the records 
for line in golf_file:
    print(line) #printing it