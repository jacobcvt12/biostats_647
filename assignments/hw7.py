from sympy import Symbol, ln, latex, diff, pretty_print
from sympy.mpmath import findroot

# p4
x = Symbol('x')
g = (1 + x) * ln(1 + x)
R = (x ** 2) / (2 * (1 + x / 3))

form = g - x - R
diff_1 = diff(form, x, 1)
diff_2 = diff(form, x, 2)


def diff_func(x):
    return 2*x**2/(3*(2*x/3 + 2)**2) - 2*x/(2*x/3 + 2) + ln(x + 1)

findroot(diff_func, 0)
