import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor
import math
import joblib
#resources\data.csv
#C:\Users\USER\git\python\AIML-Code\ai-ml\resources\data.csv
df = pd.read_csv("resources\data.csv")
print(df.head())

# Forecasting using RandomForestRegressor

df['y'] = df['Date'].apply(lambda x: int(x[-4:]))
df['m'] = df['Date'].apply(lambda x: int(x[3:5]))
df['d'] = df['Date'].apply(lambda x: int(x[:2]))
x = df[['y', 'm','d']]
orig_data = df["QTY"]
print(orig_data)


mod = GridSearchCV(RandomForestRegressor(), 
            {'max_features':[0.95],
            'n_estimators': [5, 10, 25, 50]},
             scoring = 'neg_mean_absolute_percentage_error', n_jobs = -1)

#mod = RandomForestRegressor() # Good
random_forest_reg_model = mod.fit(x,orig_data)    
fitted_data = random_forest_reg_model.predict(x)
print(fitted_data)

filename = 'random_forest_model.joblib'
#pickle.dump(random_forest_reg_model, open(filename, 'wb'))
joblib.dump(random_forest_reg_model, "models/"+filename)