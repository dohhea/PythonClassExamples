import random
import turtle
t = turtle.Turtle()

# n-각형을 그리는 함수를 정의한다.
def n_polygon(n, length):
	for i in range(n):
		t.forward(length)
		t.left(360//n) # 정수 나눗셈은 //으로 한다.

colors=['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']
angle=int(input("몇각형? "))
for i in range(18):
    t.left(20)
    t.color(random.choice(colors))
    t.begin_fill()
    n_polygon(angle, 100)
    t.end_fill()

turtle.mainloop()