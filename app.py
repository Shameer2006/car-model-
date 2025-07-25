from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('random_forest_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form values and convert to float
    input_features = [float(x) for x in request.form.values()]
    features = [np.array(input_features)]

    # Make prediction
    prediction = model.predict(features)
    output = prediction[0]

    return render_template('index.html', prediction_text=f'Predicted Value: {output}')

if __name__ == "__main__":
    app.run(debug=True)