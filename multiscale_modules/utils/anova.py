import pandas as pd
import matplotlib.pyplot as plt

import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from interpolate import interpolate
from read_data import load_data

# Small p-value, large f-test means there is significant difference in the means
# 0.1 is a large p-value --> typically ~.05 for significance
def anova(data, col_name):
    """ Runs anova tests on any number of surfaces to determine if there is a statistical significance
    in the difference between their means.  The function will print out the anova summary table and 
    plot the confidence intervals of the surfaces

    Args:
        data (pd.Dataframe): the data to be analyzed.  Should have multiple surfaces in the same dataframe
            each with a label in data['label']
        col_name (string): the dependent variable to test.  Should be the name of a column in the dataframe
    """
    # Anova tests and get table
    model = ols(f'{col_name} ~ label', data).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)
    print(anova_table)

    # hoc-test to determine confidence
    tukey = pairwise_tukeyhsd(data[col_name], data['label'], alpha=.05)
    print(tukey.summary())
    tukey.plot_simultaneous()
    plt.vlines(x=1.276, ymin=-.05, ymax=4.5, color='red') # TODO: How to find x-value for this red line? (Currently hardcoded)
    plt.show()

def lda(data_x, data_y, test_x):
    clf = LinearDiscriminantAnalysis()
    clf.fit(data_x, data_y)
    prediction = clf.predict(test_x)

d1 = load_data('../../samples', 'sample1.txt')
d2 = load_data('../../samples', 'sample2.txt')
d3 = load_data('../../samples', 'sample3.txt')
d4 = load_data('../../samples', 'sample4.txt')
data = interpolate([d1, d2, d3, d4], 'relative_area')
for num, surf in enumerate(data):
    surf['label'] = f'surf{num}'
data = pd.concat(data, ignore_index=True)
anova(data, 'relative_area')