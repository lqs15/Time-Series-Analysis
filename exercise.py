from dateutil.parser import parse 
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
plt.rcParams.update({'figure.figsize': (10, 7), 'figure.dpi': 120})

#python code and daily-min-temperatures.csv file are on the same folder
#my try

### Import as Dataframe
##df = pd.read_csv('daily-min-temperatures.csv', parse_dates=['Temp'])
##df.head()

#The example code won't work either

# Import as Dataframe
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/a10.csv', parse_dates=['date'])
df.head()

#source https://www.machinelearningplus.com/time-series/time-series-analysis-python/



