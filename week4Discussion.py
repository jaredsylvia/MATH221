# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 14:12:09 2022

@author: jared
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statistics

dailyCalories = []

def disPlot(calories, title, xlabel):
    calories.sort()
    fig = sns.displot(calories, bins=(int(calories[-1]) - int(calories[0])))
    plt.title(title)
    plt.xlabel(xlabel)
    
    plt.show()
    return fig


for i in range(0,100000):
    dailyCalories.append(np.random.randint(300,500) +\
                         np.random.randint(500,800) + \
                         np.random.randint(800,1000))

disPlot(dailyCalories, 'Daily Caloric Intake', 'Calories')

caloricMean = statistics.mean(dailyCalories)
caloricStDev = statistics.stdev(dailyCalories)
print("Mean: {}\nStDev: {}".format(caloricMean, caloricStDev))
