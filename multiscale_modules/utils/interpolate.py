from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import numpy as np
from read_data import *
import sys
import matplotlib.pyplot as plt

DEGREE = 2      # Degree of polynomial regression for interpolation model
BASE = 0        # The surface to base the scales off of

# Take in argument data which should be an array of all surfaces and their data
# Function will interpolate the data based on the first surface, filling any of these
# scales not in another surface with its predicted value based on a polynomial model
def interpolate(data):
    num_surfaces = len(data)
    models = []
    inter_data = []

    base = data[BASE]
    base_x = base["scale of analysis"]
    print("BASE SCALES= " + str(base_x))

    for surf in data:
        # fit polynomial regression
        # append to list of models
        inter_data.append([])
        yData = surf["relative area"]
        xData = surf["scale of analysis"]

        # poly = PolynomialFeatures(degree=DEGREE)
        # features = poly.fit_transform(xData.values.reshape(-1,1))
        # model = LinearRegression()
        # model.fit(features,yData)
        # models.append(model)
        model = np.polyfit(np.log(xData), yData, 1)
        c0 = model[1]
        c1 = model[0]
        l = np.log(xData)
        y_predict = c0 + c1 * l

        # y_predict = model.predict(features)
        plt.scatter(xData, yData)
        plt.plot(xData, y_predict, c="b")
        plt.show()

        for i, val in enumerate(xData):
            if val not in base_x:
                yData[i] = c0 + c1 * np.log(val)
    print("\n\nNew Scales:\n")
    for surf in data:
        print(surf["scale of analysis"])
        
if __name__ == "__main__":
    args = sys.argv[1:]
    filename1 = args[0]
    filename2 = args[1]

    data = []
    data.append(read_data(filename1))
    data.append(read_data(filename2))
    interpolate(data)