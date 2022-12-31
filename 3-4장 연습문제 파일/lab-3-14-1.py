import turtle

x=input("집의 크기는 얼마로 할까요? ")
x=int(x)

t=turtle.Turtle()
t.shape("turtle")

t.forward(x)
t.left(120)
t.forward(x)
t.left(120)
t.forward(x)


t.left(30)
t.forward(x)
t.left(90)
t.forward(x)
t.left(90)
t.forward(x)
t.left(90)
t.forward(x)

t.left(180)

