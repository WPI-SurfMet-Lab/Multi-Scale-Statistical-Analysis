from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import numpy as np
from read_data import *
import sys
import matplotlib.pyplot as plt
import os

DEGREE = 10      # Degree of polynomial regression for interpolation model
BASE = 0        # The surface to base the scales off of
PERIOD = 10
HEIGHT = 2
SHIFT = 1

# Take in argument data which should be an array of all surfaces and their data
# Function will interpolate the data based on the first surface, filling any of these
# scales not in another surface with its predicted value based on a polynomial model
def interpolate(data, stat):
    # Get the scales to be the base of inteprolation
    base = data[BASE]
    base_x = base[stat]

    # Use a logarithmic transformation and polynomial regression for each surface to obtain a model
    # for the given statistic for each scale
    for surf in data:
        # Get data
        yData = surf[stat]
        xData = np.log(surf["scale of analysis"])

        # Train model
        weights = np.polyfit(xData, yData, DEGREE)
        model = np.poly1d(weights)
        xp = np.linspace(xData.min(), xData.max(), 70)
        y_predict = model(xp)

        # Visualize data and compare with model
        plt.scatter(xData, yData, c='b', facecolor='none', alpha=.5)
        plt.plot(xp, y_predict, c='purple')
        plt.xlabel("Log of Scale of Analysis")
        plt.ylabel(stat)
        plt.show()

        # Replace old data with new data aligned on the same scale
        for i, val in enumerate(xData):
            if val not in base_x:
                yData[i] = model(val)

    # Visualize new plots on the same scales
    print("\n\nNew Scales:\n")
    colors = ['r', 'b', 'g', 'y']
    for i, surf in enumerate(data):
        plt.scatter(np.log(surf["scale of analysis"]), surf[stat], c=colors[i], alpha=.3)
    plt.xlabel("Log of Scale of Analysis")
    plt.ylabel(stat)
    plt.show()
        
if __name__ == "__main__":
    args = sys.argv[1:]
    stat = args[0]
    filename1 = args[1]
    filename2 = args[2]
    filename3 = args[3]
    filename4 = args[4]

    data = []
    data.append(read_data(filename1))
    data.append(read_data(filename2))
    data.append(read_data(filename3))
    data.append(read_data(filename4))
    interpolate(data, stat)