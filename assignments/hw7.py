from sympy import Symbol, ln, latex, diff, pretty_print
from sympy.mpmath import findroot

# p4
x = Symbol('x')
g = (1 + x) * ln(1 + x)
R = (x ** 2) / (2 * (1 + x / 3))

form = g - x - R
diff_1 = diff(form, x, 1)
diff_2 = diff(form, x, 2)

pretty_print(diff_1)
findroot(diff_1, 0)
