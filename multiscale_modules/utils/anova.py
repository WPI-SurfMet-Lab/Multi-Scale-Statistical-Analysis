import pandas as pd

import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from bioinfokit.analys import stat

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

def anova(data, col1, col2):
    x = [[1, 2], [3, 3], [4, 5], [4, 2]]
    data = pd.DataFrame(x, columns=['A', 'B'])
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
    
anova(0, 'A', 'B')