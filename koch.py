import turtle as t

def koch(n, longueur):
    if n==0:
        t.forward(longueur)
    else:
        koch(n-1,longueur/3)
        t.left(60)
        koch(n-1,longueur/3)
        t.right(120)
        koch(n-1,longueur/3)
        t.left(60)
        koch(n-1,longueur/3)

t.home()
t.begin_poly()
t.begin_fill()
t.speed(0)
t.fillcolor('red')
t.hideturtle()
for i in range(6):
    koch(1,400)
    t.right(120)
t.end_fill()
t.end_poly()
print(t.get_poly())
t.exitonclick()