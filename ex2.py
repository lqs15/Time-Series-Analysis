from pandas import read_csv
from pandas import DataFrame
from pandas import Grouper
from matplotlib import pyplot
from statsmodels.tsa.seasonal import seasonal_decompose
series = read_csv('daily-minimum-temperatures.csv', header=0, index_col=0, parse_dates=True, squeeze=True)
result = seasonal_decompose(series, model='additive', freq=1)
result.plot()
pyplot.show()

