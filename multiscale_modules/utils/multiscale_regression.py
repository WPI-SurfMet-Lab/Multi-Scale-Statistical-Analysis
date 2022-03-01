from read_data import read_data
from interpolate import *
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Takes in an array of surfaces to perform regression on, the predictor data, the stat to predict,
# and the type of regression to use
# Assumes the data is already scale aligned
def multi_regression(data, predictor, stat, type):
    predictor = np.array(predictor).reshape(-1,1)
    models = []
    scores = []
    model = LinearRegression()
    for scale, val in enumerate(data[0]["scale of analysis"]):
        yData = []
        for surf in data:
            yData.append(surf[stat][scale])
        model.fit(predictor, yData)
        score = model.score(predictor, yData)
        models.append(model)
        scores.append(score)

        # Visualize regression
        # xp = np.linspace(predictor.min(), predictor.max(), 50).reshape(-1,1)
        # y_predict = model.predict(xp)
        # plt.scatter(predictor, yData, c='b')
        # plt.plot(xp, y_predict, c='r')
        # plt.xlabel("Coeff of Friction")
        # plt.ylabel(stat + " at scale " + str(val))
        # plt.show()
    
    # Visualize resulting plot of R2 of the regression over all of the scales
    plt.scatter(data[0]["scale of analysis"], scores, marker='*', color='b')
    plt.xlabel("Log of Scale of analysis")
    plt.ylabel("R2")
    plt.show()


if __name__ == "__main__":
    args = sys.argv[1:]
    stat = args[0]

    data = []
    data.append(read_data('./../../samples/sample1.txt'))
    data.append(read_data('./../../samples/sample2.txt'))
    data.append(read_data('./../../samples/sample3.txt'))
    data.append(read_data('./../../samples/sample4.txt'))
    data.append(read_data('./../../samples/area-scale-test-data.txt'))
    data = interpolate(data, stat)
    # Change predictor list with measured outside statistic you would like to use
    # Ex: Coefficient of friction [.3, .4, .5, .6, .7]
    predictor = [.3, .4, .5, .6, .7]
    multi_regression(data, predictor, stat, 'linear')
