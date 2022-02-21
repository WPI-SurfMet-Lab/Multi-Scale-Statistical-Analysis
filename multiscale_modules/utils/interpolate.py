from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# Take in argument data which should be an array of all surfaces and their data
def interpolate(data):
    num_surfaces = len(data)
    models = []
    inter_data = []

    for surf in data:
        # fit polynomial regression
        # append to list of models
        inter_data.append([])
        xData = surf["relative area"]
        yData = surf["scale of analysis"]

        model = PolynomialFeatures(degree=4)
        X_poly = model.fit_transform(xData)
        model.fit(X_poly,yData)
        models.append(model)