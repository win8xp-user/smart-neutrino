# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 01:22:17 2023

@author: SergeEvseev
"""
import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 3.0, 0.5 # mean and standard deviation
print(mu, sigma)
s_norm = np.random.normal(mu, sigma, 1000)
# Display the histogram of the samples, along with the probability density function

count, bins, ignored = plt.hist(s_norm, 100, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
                np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
          linewidth=2, color='y')
plt.show()

# scale parameter (log mean) and
# shape parameter (log standard deviation)
# mu, sigma = 3.0, 0.5 

# s = np.random.lognormal(mu, sigma, 1000)
# # Display the histogram of the samples, along with the probability density function

# count, bins, ignored = plt.hist(s, 100, density=True, align='mid')
# x = np.linspace(min(bins), max(bins), 100)
# pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2))
#         / (x * sigma * np.sqrt(2 * np.pi)))
# plt.plot(x, pdf, linewidth=2, color='r')
# plt.axis('tight')
# plt.show()
