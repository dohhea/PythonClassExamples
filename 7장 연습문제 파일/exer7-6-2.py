import random
import turtle
t = turtle.Turtle()

# n-각형을 그리는 함수를 정의한다.
def n_polygon(n, length, color):
    t.color(color)
    t.begin_fill()
    for i in range(n):
        t.forward(length)
        t.left(360//n) # 정수 나눗셈은 //으로 한다.
    t.end_fill()

colors=['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']
angle=int(input("몇각형? "))
for i in range(18):
    t.left(20)
    n_polygon(angle, 100, random.choice(colors))

turtle.mainloop()
