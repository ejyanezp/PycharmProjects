import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, expon, binom


# values = np.random.uniform(-10.0, 10.0, 100000)
# plt.hist(values, 50)


pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = np.random.normal(50.0, 10.0, 1000) / pageSpeeds
# plt.scatter(pageSpeeds, purchaseAmount)

nd_array = np.array([pageSpeeds, purchaseAmount])
cov_arr = np.cov(nd_array)
print(cov_arr)
print(f'{np.var(pageSpeeds)} ≈ {cov_arr[0][0]}')
print(f'{np.var(purchaseAmount)} ≈ {cov_arr[1][1]}')

# x = np.arange(0, 4, 0.001)
# axes = plt.axes()
# axes.grid()
# plt.plot(x, norm.pdf(x, 2, 0.5))
# plt.plot(x, expon.pdf(x), 'r:')  # r: ==> linea roja punteada
# plt.legend(['set1', 'set2'], loc=1)  # loc=1 ==> Poner la leyenda en la esquina superior derecha


# x = np.arange(0, 10, 0.001)
# plt.plot(x, expon.pdf(x))

# n, p = 10, 0.5
# x = np.arange(0, 10, 0.001)
# plt.plot(x, binom.pmf(x, n, p))

# plt.show()
