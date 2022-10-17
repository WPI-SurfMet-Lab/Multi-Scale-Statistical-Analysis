import pandas as pd

import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from bioinfokit.analys import stat

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from interpolate import interpolate
from read_data import load_data

def anova(surf1, surf2, col_name):
    data = pd.DataFrame()
    data['A'] = surf1[col_name]
    data['B'] = surf2[col_name]
    col1, col2 = 'A', 'B'
    arr = []
    for col in data.columns:
        arr.append(data[col])
    fvalue, pvalue = stats.f_oneway(*arr)
    print("F-value:\t" + str(fvalue) + "\nP-value:\t" + str(pvalue))

    model = ols(f'{col1} ~ {col2}', data).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)
    print(anova_table)

    res = stat()
    res.tukey_hsd(df=data, res_var=col1, xfac_var=col2, anova_model=f'{col1} ~ {col2}')
    print(res.tukey_summary)

def lda(data_x, data_y, test_x):
    clf = LinearDiscriminantAnalysis()
    clf.fit(data_x, data_y)
    prediction = clf.predict(test_x)

d1 = load_data('../../samples', 'sample1.txt')
d2 = load_data('../../samples', 'sample2.txt')
data = interpolate([d1, d2], 'relative area')
anova(data[0], data[1], 'relative area')