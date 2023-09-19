import turtle as t

n = 8
s = 20
angle = 360. / n

t.home()
t.begin_poly()
# t.speed(1000)
t.ht
for k in range(n):
    t.forward(s)
    t.left(angle)
t.end_poly()
print(t.get_poly())
