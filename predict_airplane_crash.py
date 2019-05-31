import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import date, timedelta, datetime
data = pd.read_csv('../socialite/airplane-crashes-since-1908/Airplane_Crashes_and_Fatalities_Since_1908.csv')
print(data.keys())
np.random.seed(50)
obs, feat = data.shape
print(obs)
print(feat)
print(data.sample(5))
result = data.isnull().sum()
print(result)