from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
import pandas as pd

X = pd.DataFrame({
    "A":[1,2,3,4],
    "B":[2,3,4,5],
    "C":[5,6,7,8]
})

y = [0,1,0,1]

selector = SelectKBest(score_func=f_classif,k=2)

X_new = selector.fit_transform(X,y)

print(X_new)