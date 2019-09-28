import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt

book = pd.ExcelFile('data.xlsx')
clients_df = book.parse('Soc_Dem')
clients_df.head()

#Checking for missing data and remove them
clients_df.isnull().sum()
clients_df.dropna(inplace = True)

under_age = list(clients_df.loc[clients_df['Age'] < 18].index)
clients_df.drop(under_age, inplace = True)
bins = pd.IntervalIndex.from_tuples([(18,30),(31,45),(46,60),(61,99)])
ages_df = clients_df.groupby(['Sex',pd.cut(clients_df.Age,bins)]).count()
ages_count = ages_df['Client']
ages_count
