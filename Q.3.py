# Library
import math
import My_lib

# Function


def fun_dydx(v, x):
    return v

# Function


def fun_dzdx(y, z, x): 
    return z + 1


# initial values
x0 = 0
x_lim = 1
y0 = 1
yn = 2 * (math.e - 1)
zh = 1.6
zl = 0.4
h = 0.03

# Recalling function and saving values
y, z = My_lib.shooting_method(
    fun_dydx, fun_dzdx, x0, x_lim, y0, yn, zl, zh, h, "Q.3.txt")
print("Using z(x = %.0f) = %f, we obtain y_e(x = %.0f) = %f ≈ β = %f ." %
      (x0, z, x_lim, y, yn))

# Output
# Using z(x = 0) = 0.966321, we obtain y_e(x = 1) = 3.436564 ≈ β = 3.436564 . 
