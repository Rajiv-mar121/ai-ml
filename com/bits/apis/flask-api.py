from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

""" sample payload
{
    "Date": [
        "02-02-2022"
    ]
} 
"""

""" # Load the trained model using pickle
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file) """

# Load the trained model
model = joblib.load('models/random_forest_model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
   
    print(data)
    df = pd.DataFrame(data)
    print("Rajiv")
    print(df)
    df['y'] = df['Date'].apply(lambda x: int(x[-4:]))
    df['m'] = df['Date'].apply(lambda x: int(x[3:5]))
    df['d'] = df['Date'].apply(lambda x: int(x[:2]))  
    
    x = df[['y', 'm','d']]
    predictions = model.predict(x)
    return jsonify(predictions.tolist())

if __name__ == '__main__':
    app.run(debug=True)
    """ app.run(host='0.0.0.0', port=5000) """