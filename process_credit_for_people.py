# -*- coding: utf-8 -*-
"""
@author: Maicon Douglas Filipiaki
"""

import pandas as pd
# import of file csv
base  = pd.read_csv('original.csv')

# view statistic of data 
base.describe()

# find information
base.loc[base['age'] < 0]

# delete column 
#Params -> Name column, delete all column, not return  
base.drop('age', 1, inplace=True)

# delete only regiter incorrent
base.drop(base[base.age < 0].index, inplace=True)

# put value manual - The best option
# put value equivalent the average
base.mean() # view average of data 
base['age'].mean()