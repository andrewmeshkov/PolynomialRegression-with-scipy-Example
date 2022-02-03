import math
import numpy as np

#curve fit is function of a simple polynomial regression, this is demonstrated here for finding polynomial regression coefficients

from scipy.optimize import curve_fit

#example function

def fi(x, a0, a1, a2, a3, a4, b1, b2, b3, b4):
    return (a0 + a1 * np.cos((x / 12 + b1 / 24) * 2 * math.pi) + a2 * np.cos((x / 24 + b2 / 24) * 2 * math.pi) +
        a3 * np.cos((x / 168 + b3 / 24) * 2 * math.pi) + a4 * np.cos((x / 672 + b4 / 24) * 2 * math.pi))

#the function values from 0 to 168 are fed to the input

t = np.arange(0, 168)
ls = np.array([int(input()) for i in range(168)])

coef, _ = curve_fit(fi, t, ls)
for i in range(168, 336):
    print(int(fi(i, *coef)))