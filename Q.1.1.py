# Library
import math
import My_lib

# Function


def fun(y, x):
    return (y * math.log(y)) / x


x = []
y = []

# initial values
x.append(2)
y.append(2.71828)

# Recalling function and saving values
My_lib.explicit_euler(fun, x, y, 60)

j = open("Q.1.1.txt", 'a')
for i in range(len(x)):
    j.write("%5.21f                %5.21f\n" % (x[i], y[i]))
j.close()

print("For Q1.(a) solution at x = %.0f is %s" % (x[-1], y[-1]))

# For Q1.(a) solution at x = 60 is 42300784541.69497
