# Library
import My_lib

# Function


def fun_dydx(v, x):
    return v

# Function


def fun_dzdx(y, z, x):
    return 1 - z - x


# initial values
x = 0
y = 2
z = 1
h = 0.3

# Recalling function and saving values
y, x = My_lib.runge_kutta(
    fun_dydx, fun_dzdx, x, y, z, 11, h, "Q.2.txt")
print("For Q.2 Approximate solution at x = %.0f is %s" % (x, str(y)))

# Output
