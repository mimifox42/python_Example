import turtle #importing turtle 
y = 10 #setting up how forward the turtle should move so the squares are sperate from eachover
for x in range(50): #it should iterate 50 times to form the squares
    turtle.left(90) #in order to make a square it needs to be a 90 degress angle
    turtle.forward(y)
    y+=10 #in order for it to get increasingly big it must be increased every time it goes through the code
    