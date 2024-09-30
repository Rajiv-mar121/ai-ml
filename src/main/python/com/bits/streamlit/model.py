from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

iris =  load_iris()
X_train, X_test, Y_train,Y_test =train_test_split(iris.data, iris.target,test_size=0.2,random_state=42)

model =  RandomForestClassifier()
model.fit(X_train, Y_train)
accuracy  = model.score(X_test,Y_test)

print(f"Model accuracy : {accuracy}")
#C:\Users\USER\git\python\AIML-Code\ai-ml\models models
with open("random_for_streamlit_model.pkl",'wb') as f:
    pickle.dump(model,f)

#pickle.dump('random_forest_model.pkl', open(filename, 'wb'))
