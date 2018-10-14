## Fast and dirty GBM
#%%
import pandas as pd 
import numpy as np
from lightgbm import LGBMClassifier
from scipy.stats import randint
from scipy.stats import uniform
from sklearn.model_selection import StratifedKFold, RandomizedSearchCV

from code.dfmaxreducer import Maxreducer
reducer = Maxreducer()

train = pd.read_csv("./input/raw/application_train.csv")
# test = pd.read_csv("./input/raw/application_test.csv")

train = train.select_dtypes(exclude='object')
train = reducer.reduce(train, verbose=True)
for d in train.dtypes.unique():
    print(d)

#%%
clf = LGBMClassifier()
clf.fit(train.filter(regex=r'^EXT_SOURCE_.', axis=1), train['TARGET'])


