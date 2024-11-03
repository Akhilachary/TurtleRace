import random
import turtle
from turtle import Turtle,Screen
WIDTH=400
HEIGHT=400
start=True
# s1=Screen()
# s1.setup(400,400)
def no_turtles():
    while True:
        no_of_turltes=input("Enter the numbers of turtles that are participating in race(2-10)?: ")
        if no_of_turltes.isdigit():
            no_of_turltes=int(no_of_turltes)
        else:
            print("Please enter numeric value!.")
            continue
        if no_of_turltes>=2 and no_of_turltes<=10:
            return no_of_turltes
        else:
            print("please give valid range!.")
            continue

colors=['red','green','purple','yellow','pink','orange','black','blue','brown','aqua']
def making_turtles(turtles,space):
    turtle_list = []
    for i in range(1,turtles+1):
        t=Turtle()
        t.penup()
        t.color(colors[i-1])
        t.shape('turtle')
        t.left(90)
        t.goto(-WIDTH//2+(space*i),-HEIGHT//2)
        turtle_list.append(t)
    return turtle_list
def race(turtle_list):
    not_reached=True
    while not_reached:
        for t in turtle_list:
            distance=random.randint(4,10)
            t.forward(distance)
            x,y=t.pos()
            if y >=200:
                print(f"the winner is {t.pencolor()} turtle")
                not_reached=False
                return
while start:
    count=no_turtles()
    Screen().clearscreen()
    x_spacing=WIDTH//(count+1)
    list=making_turtles(count,x_spacing)
    race(list)
    again=input("If you want to race again?('yes'/'no'):").lower()
    if again == 'yes':
        continue
    else:
        start=False

Turtle().screen.mainloop()