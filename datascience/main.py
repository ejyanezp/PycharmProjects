import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, expon, binom


# values = np.random.uniform(-10.0, 10.0, 100000)
# plt.hist(values, 50)

x = np.arange(0, 4, 0.001)
axes = plt.axes()
axes.grid()
plt.plot(x, norm.pdf(x, 2, 0.5))
plt.plot(x, expon.pdf(x), 'r:')  # r: ==> linea roja punteada
plt.legend(['set1', 'set2'], loc=1)  # loc=1 ==> Poner la leyenda en la esquina superior derecha


# x = np.arange(0, 10, 0.001)
# plt.plot(x, expon.pdf(x))

# n, p = 10, 0.5
# x = np.arange(0, 10, 0.001)
# plt.plot(x, binom.pmf(x, n, p))

plt.show()
