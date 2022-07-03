# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 11:45:52 2022

@author: jared
"""

import matplotlib.pyplot as plt

dataset = [5, 6, 3, 3, 4, 2, 7, 8, 9, 2, 5, 4, 3, 11, 21, 31, 22, 27, 28, 18]

plt.figure(dpi=500)
plt.hist(dataset, bins=4, range=[0,32], facecolor='blue', edgecolor='black', alpha=.5)
plt.xticks(range(0,33,8))
plt.xlabel('Week 1 Discussion')

plt.show()
