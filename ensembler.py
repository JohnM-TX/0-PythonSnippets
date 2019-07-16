#%%
import os 
from glob import glob
import numpy as np
import pandas as pd
from sklearn.preprocessing import minmax_scale
from sklearn.metrics import roc_auc_score
from scipy.stats import rankdata


#%% args
subdir = './ensembles'
indexcol = 'id'
scale = True #not implemented

#%%
files = glob(os.path.join(subdir, '*.csv'))

preds_list = []
for s in subs:
    vals = pd.read_csv(s, index_col=indexcol).sort_index().values
    preds_list.append(vals)

preds_array = np.concatenate(preds_list, axis=1)

#%%
# create wieghted average, scale as necessary, save to csv.zip



