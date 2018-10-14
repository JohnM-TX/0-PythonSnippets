#%% for demo only: reduce features...
import eda.boruta_py
from sklearn.ensemble import RandomForestClassifier

X = train.drop('TARGET', axis=1)
allobjs = X.select_dtypes(include='object')
for obj in allobjs.columns:
    X[obj] = X[obj].astype('category').cat.codes
X.fillna(-1, inplace=True)
y = train.TARGET.values
forest = RandomForestClassifier(n_jobs=-1, class_weight='balanced_subsample')
feat_selector = eda.boruta_py.BorutaPy(forest, n_estimators=500, verbose=2, 
    perc=90, max_iter=50, )
feat_selector.fit(X.values, y)
feat_selector.support_
feat_selector.ranking_