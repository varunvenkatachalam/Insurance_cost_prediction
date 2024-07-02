from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('insurance_model.joblib')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the HTML form
        age = float(request.form['age'])
        bmi = float(request.form['bmi'])
        children = int(request.form['children'])

        # Make a prediction using the loaded model
        input_data = np.array([[age, bmi, children]])
        prediction = model.predict(input_data)[0]

        # Round the prediction to two decimal places
        rounded_prediction = round(prediction, 2)

        # Render the HTML template with the prediction
        return render_template('index.html', prediction=rounded_prediction)

    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True,port=5656)
