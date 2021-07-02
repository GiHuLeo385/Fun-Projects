import statistics
import turtle

print("This is a 2 variable linear regression analysis programme")
No_of_sets = int(input("Number of variable-sets: "))

"""This is use to resize the graph at the end, you have to tweak it a couple of times to get it right, the rule of thumb is if the data is around 100, then 1 is find"""
margin = float(input("Please input ratio for the graph(> 1 is bigger, < 0 is smaller): "))

x = []
y = []
xy = []

print("Please enter all x data, and press enter after each")
for i in range(0, No_of_sets):
    x_data = float(input())
    x.append(x_data * margin)

print("Please enter all y data, and press enter after each")
for i in range(0, No_of_sets):
    y_data = float(input())
    y.append(y_data * margin)

for i1, i2 in zip(x, y):
    xy.append(i1 * i2)

x_square = [i ** 2 for i in x]

mean_x = statistics.mean(x)
mean_y = statistics.mean(y)
mean_xy = statistics.mean(xy)
slope = (mean_x * mean_y - mean_xy) / (mean_x ** 2 - statistics.mean(x_square))
intercept = (mean_y - slope * mean_x)

"""Draw the X-Y Axis"""

turtle.penup()
turtle.goto(-700, -300)
turtle.pendown()
turtle.forward(max(x) + 30)
turtle.penup()
turtle.goto(-700, -300)
turtle.left(90)
turtle.pendown()
turtle.forward(max(y) + 30)

"""Draw the Data points"""

for i1, i2 in zip(x, y):
    turtle.penup()
    turtle.goto(i1 - 700, i2 - 300)
    turtle.dot(10, "red")

"""Draw the Regression Line"""
turtle.penup()
turtle.goto(-700, round(intercept, 0) - 300)
turtle.pendown()
turtle.color("blue")
turtle.goto(max(x) - 700, round(slope * max(x) + intercept, 0) - 300)

turtle.mainloop()
