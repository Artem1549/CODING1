import turtle
import  random

turtle.shape("turtle")

def draw_polygon(side_lenght, sides):
    for i in range(0,sides):
        turtle.forward(side_lenght)
        turtle.right(360/sides)

    turtle.done()

#draw_polygon(100,10)



def rand_walker(steps):
    for i in range(0,steps):
        randwalk = random.randint(1,4)

        if (randwalk == 1):
             turtle.forward(50)
        elif(randwalk == 2):
            turtle.backward(50)
        elif(randwalk == 3):
            turtle.left(90)
        elif(randwalk == 4):
            turtle.right(90)


def main():   
    
    rand_walker(100)
    turtle.reset()
    draw_polygon(100,10)
    

main()



        

