#example3 
answer = "y"
total = 0
budget = int(input("Enter the budget")) #user prompted to enter the budget
while (answer == "y"): #loop is running until the user enters anything but a "y"
    expenses = int(input("Enter expenses"))
    total = expenses + total #adding the total of the expenses
    answer = input("Do you have more expenses?") 
if(total > budget): #testing if the expenses is over the budget
    over = total - budget
    print("you are ", over, "over the budget")
else: #if not it is under the budget
    under = budget - total
    print("you are ", under, "under the budget")
 
#example7
x = .01 #setting up first day amount
total = 0
count = 1
days= int(input("Enter the number of days")) #prompting user to enter number of days
for count in range(2, days + 1): #setting up for loop to run on day two
   x *= 2 #doubling penny value
   total += x #colecting the total
   print("days    "  "  total")
   print("------     ------")
   print(count ,'${:,.2f}'.format(x))
print("The total amount earned is ", '${:,.2f}'.format(total+ 0.01)) #printing out the total earned + first day and converting it to currency
   