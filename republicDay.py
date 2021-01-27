import turtle as aj



aj.tracer(8, 10)
aj.pensize(4)
def square():
    for i in range(4):
        aj.pencolor('dark green')
        aj.fd(60)
        aj.rt(90)
        aj.pencolor('white')

def circle():
    aj.rt(90)
    aj.pensize(4)
    aj.pencolor('dark orange')
    aj.circle(30)
    aj.rt(15)

def big():
    for i in range(4):
        aj.fd(50)
        aj.rt(12)
for i in range(100):
    square()
    aj.rt(10)
    big()
    circle()
aj.pd()
aj.lt(100)
aj.pu()


aj.pencolor('dark blue')
aj.write("HAPPY REPUBLIC DAY",move=False, align="center", font=('verdana', 30, 'normal'))
aj.delay(50)