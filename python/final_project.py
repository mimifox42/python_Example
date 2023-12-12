#final project Miriam Fox
#I decided to make the program the simpliest it can for the user it would be to instead of asking for the date ask the user for their name which I made sure to validate in the program and the graph uses name and their order details 
import pickle #importing pickle fucntion
import matplotlib.pyplot as plt #importing to be able to plot graph
f = open("product_list.txt") #opening the product list file
file_list = {} #initiating a file list
orders = {} #initiating a orders list
file_title = f.readline() #first line of the file is a title
file_list = f.readlines() #the rest of the file is products
barcode_product_name={} #initiating a dict for barcodes and product name
barcode_price = {} #initiating a dictionary for barcode and its corresponding prices
order_details = {} #initiating a dictionary for name and its order details
        
with open("order.dat", "rb") as file: #open to pickle the file
    order_details = pickle.load(file) #loading the pickle file
with open("bar.dat", "rb") as file1: #odening second pickle file that contains second dict
    name_bar = pickle.load(file1) #loading that file
    
LOOK_UP = 1 #setting up constants for the menu
SHOP = 2
SUMMARY = 3
EXIT = 4

def main(): #main function
    choice = 0 #setting menu choice to zero
    while choice != EXIT: #while user doesnt not enter 4
        choice = menu() #setting the choice to equal the menu function
        if choice == LOOK_UP: #if user enters 1
            lookup() #go to this function
        elif choice == SHOP: #if user enters 1
            shop() #go to this function
        elif choice == SUMMARY: #if user enters 1
            summary() #go to this function
def menu(): #menu function
    print("1 - Look up an order") #show options to user
    print("2 - Shop")
    print("3 - Item Summary")
    print("4 - Exit")
    
    choice_ = 4 #initiating value to exit value
    while True: #try except for validating user input in this menu
        try: #get user input for menu and continuie program with that num
            choice = int(input("Enter the menu option you want"))
            return choice
        except ValueError: #if anything but a value in the menu is entered program restarts
            print("Please enter a number only")
            main()
        else:
            break #if user wants to exit it closes program
            choice_ = choice
            
   
   
def lookup(): #defining first mneu option
    name = input("Enter a name") #getting the name
    if name.isalpha(): #test if name only contains letters
        if name in name_bar: #confirming the name is has bought something in the past
            retu = name_bar.get(name, "Information not found" ) #saving the users barcode purchases with variable
            print(retu)#based on the key printing value
        else:
            print("Record not found") #returning to main menu
            main()
    else: #print message to user to enter correct input
        print("Please enter only letters")
        main() #go back to main function
    user = input("Do you want to return anything? Yes or No") #asking user if they want to return anything
    while (user.lower() == "yes"): #is user enters yes
        bar = input("Which item barcode would you like to return?") #asking them which barcode they want to return
        if bar in retu: #checking to see if the barcode is found in the users orders 
            retu.replace(bar, " ") #if so replace the barcode with empty string - which is currently not working
            pickle.dump(name_bar, open("bar.dat", "wb")) #updating file with the change of information
        else:
            print("Bar not found") #either barcode is not a valid code ot there is no roecord of them buyingwith that barcode
            main()
        user = input("Do you want to return anything? Yes or No") #
    main()
    
    pickle.dump(order_details, open("order.dat", "wb"))  #saving both files
    pickle.dump(name_bar, open("bar.dat", "wb"))

def shop():
    total = 0.00 #setting up the total 
    for g in file_list: #going through the file to print those values and save them in their respective files
        barcode = g.split()[0]
        product_name = g.split()[1]
        price = g.split()[2]
        barcode_product_name[barcode] = product_name
        barcode_price[barcode] = price
        print(barcode + "\t" + " " + product_name + "\t" + "\t" +  price)
    name = input("Enter the name on your reciept") #getting the customers name
    if name.isalpha():
        print("Welcome", name)
    else:
        print("Please enter only letters for the name")
        main()
    bar = input("Enter barcode of the item you wish to purchase type pay to purchases") #which item would you like to buy
    name_bar[name] = bar
    while bar != "pay": #while user wants to enter more time to buy
        print(barcode_product_name.get(bar, "Information not found")) #get the price of the barocde entered
        print(barcode_price.get(bar, "Not Found")) 
        total += float(barcode_price.get(bar) )#calculating the total
        name_bar[name] += " " + bar #adding all the barcodes, this program currently adds two barcodes since I first had to set the person in the system and then add the rest of their barcodes
        bar = input("Enter barcode of the item you wish to purchase type pay to complete purchase ")#countinung the loop
        
    if name not in order_details: 
        order_details[name] = total #adding the info to the order details dict
    print("The total for your order is ", total) #print the total of the order
    pickle.dump(order_details, open("order.dat", "wb")) #updating all the info 
    pickle.dump(name_bar, open("bar.dat", "wb"))
       
def summary(): 
    order_plots = order_details.items() #setting up a list of the plots
    order_plots = sorted(myList) #sort those items to make the graph clear
    x, y = zip(*myList) #assignign these plots x and y
    plt.plot(x, y) #plot those items 
    plt.xlabel('Name') #naming the x 
    plt.ylabel('Order Total')  #naming the y
    plt.title('Grocery Store Orders') #naming the graph
    plt.show() #show the graph

main()  #calling the main function
   
    
    
    
        
    