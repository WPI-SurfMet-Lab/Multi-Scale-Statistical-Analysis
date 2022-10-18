import numpy as np
from read_data import *
import sys
import matplotlib.pyplot as plt

DEGREE = 10      # Degree of polynomial regression for interpolation model
BASE = 0        # The surface to base the scales off of

# Take in argument data which should be an array of all surfaces and their data
# Function will interpolate the data based on the first surface, filling any of these
# scales not in another surface with its predicted value based on a polynomial model
def interpolate(data, stat):
    # Get the scales to be the base of inteprolation
    base = data[BASE]
    base_x = base["scale_of_analysis"]

    new_data = []

    # Use a logarithmic transformation and polynomial regression for each surface to obtain a model
    # for the given statistic for each scale
    for surf in data:
        # Get data
        yData = surf[stat]
        xData = np.log(surf["scale_of_analysis"])

        # Train model
        weights = np.polyfit(xData, yData, DEGREE)
        model = np.poly1d(weights)
        xp = np.linspace(xData.min(), xData.max(), 70)
        y_predict = model(xp)

        # Visualize data and compare with model
        # plt.scatter(xData, yData, c='b', facecolor='none', alpha=.3)
        # plt.plot(xp, y_predict, c='purple')
        # plt.xlabel("Log of Scale of Analysis")
        # plt.ylabel(stat)

        # Replace old data with new data aligned on the same scale
        d = {"scale of analysis": [], stat: []}
        df = pd.DataFrame(data=d)
        for i, val in enumerate(base_x):
            if val not in surf["scale_of_analysis"].values:
                new_stat = surf[stat][i] = model(np.log(val))
                df.loc[i] = [val, new_stat]
            else:
                loc = np.where(surf["scale_of_analysis"].values == val)[0][0]
                old_stat = surf[stat][loc]
                df.loc[i] = [val, old_stat]
        new_data.append(df)
        # Visualize data and compare with model
        # print(df)
        # plt.plot(np.log(df["scale of analysis"]), df[stat], c='red')
        # plt.show()

    # Visualize new plots on the same scales
    # print("\n\nNew Scales:\n")
    # colors = ['r', 'b', 'g', 'y', 'orange']
    # for i, surf in enumerate(new_data):
    #     print(surf["scale of analysis"])
    #     plt.scatter(np.log(surf["scale of analysis"]), surf[stat], c=colors[i], alpha=.3)
    # plt.xlabel("Log of Scale of Analysis")
    # plt.ylabel(stat)
    # plt.show()

    return new_data


if __name__ == "__main__":
    args = sys.argv[1:]
    stat = args[0]

    data = [read_data('./../../samples/sample1.txt'),
            read_data('./../../samples/sample2.txt'),
            read_data('./../../samples/sample3.txt'),
            read_data('./../../samples/sample4.txt'),
            read_data('./../../samples/area-scale-test-data.txt')]
    interpolate(data, stat)
