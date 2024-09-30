import pandas as pd
import numpy as np
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

import matplotlib.pyplot as plot



print("Starting ...")
wine = load_wine()
X =  wine.data
Y =  wine.target
feature_name =  wine.feature_names

print(feature_name)
df =  pd.DataFrame(X, columns=feature_name);
df['target']=Y
print(df.head())

## Training Model
X_train, X_test, y_train, y_test =train_test_split(X,Y,test_size=.2,random_state=42)
svm =  SVC(kernel='linear')
#svm = SVC(C=1.0, kernel='linear', degree=3, gamma='scale', coef0=0.0, shrinking=True, probability=False, tol=0.001, cache_size=200, class_weight=None, verbose=False, max_iter=-1, decision_function_shape='ovr', break_ties=False, random_state=None)
svm.fit(X_train,y_train)

## Predicting 
y_predict =  svm.predict(X_test)
accuracy =  accuracy_score(y_test, y_predict)
print("Rajiv....")
print(accuracy)
coef =  svm.coef_

print(coef)
importance  = np.sum(np.abs(coef), axis=0)
indicies = np.argsort(importance)[::-1]
print(indicies)

## Plotting

plot.figure(figsize=(10,6))
plot.bar(range(X.shape[1]), importance[indicies])
#print(plot)
