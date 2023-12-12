#example 1
course_room = {"CS101" : 3004, "CS102" : 4501, "CS103": 6755, "NT110" : 1244, "CM241" : 1411} #setting up the dictonary for this program
course_instructions = {"CS101" : "Haynes", "CS102" : "Alvarado", "CS103" : "Rich", "NT110" : "Burke", "CM241" : "Lee"}
course_meeting = {"CS101" : "8:00 a.m.", "CS102" : "9:00 a.m.", "CS103" : "10:00 a.m.", "NT110" : "11:00 a.m.", "CM241" : "1:00 a.m."}

def main(): #main method 
    courseNum = input("Enter a course number") #user input to ask for their course number
    
    print("Your course room number is",course_room.get(courseNum)) #this method will use the .get() to check for information from the key value and display its related value
    print("Your instructor for the course is",course_instructions.get(courseNum))
    print("Your course meeting time is",course_meeting.get(courseNum))
    
    
main() #calling the main method 
#example 8
import pickle #in order to open pickle must be imported
#setting up constants for the menu options
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
EXIT = 5

#main function
def main():
    name_email = {} #creating the name and email dictionary  
    choice = 0
    while choice != EXIT: #creating a loop that will run while the user does not enter 5
        choice = menu() #taking the choice input to menu function
        if choice == LOOK_UP: #based on choice variable the different fucntions will run 
            look_up(name_email)
        elif choice == ADD:
            add(name_email)
        elif choice == CHANGE:
            change(name_email)
        elif choice == DELETE:
            delete(name_email)
    outputfile.close()
def menu():
    print("1 - Look up an email") #menu option sfor the user
    print("2 - Add a new email")
    print("3 - Change an email")
    print("4 - Delete an email")
    print("5 - Exit ")
    
    choice = int(input("Enter a menu option"))
    
    if choice < LOOK_UP or choice > EXIT: #if menu option is out of bounds
        choice = int(input("Enter a valid choice"))
        
    return choice 
    
def look_up(name_email): #if user enters 1
    name = input("Enter a name") #getting the key
    
    print(name_email.get(name, "Information not found"))#based on the key printing value

def add(name_email): #if user enters 2
    name = input("Enter your name") #getting the key
    email = input("Enter your email address") #getting the new value
    
    if name not in name_email: #if key is not already in the dictionary
        name_email[name] = email #adding the value
        outputfile = open("name_email.dat", "wb") #open the file
        pickle.dump(name_email, outputfile) #saving changes to file
        outputfile.close() #closing file
    else:
        print("Duplicate Data")
        
def change(name_email): #if user enters 3
    name = input("Enter your name") #enter key
    if name in name_email:
        newEmail = input("Enter your new email") #getting the new value
        name_email[name] = newEmail #updating the value
        outputfile = open("name_email.dat", "wb") #open the file
        pickle.dump(name_email, outputfile) #saving changes to file
        outputfile.close() #closing file
    else:
        print("Name not found")
def delete(name_email): #if user enters 4
    name = input("Enter your name")
    if name in name_email: #if key is found 
        del name_email[name] #delete key and value
        outputfile = open("name_email.dat", "wb") #open the file
        pickle.dump(name_email, outputfile) #saving changes to file
        outputfile.close() #closing file
    else:
        print("Name not found")
    
main() #calling main function