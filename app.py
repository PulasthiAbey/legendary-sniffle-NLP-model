from flask import Flask, request
import joblib

app = Flask(__name__)

model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = model.predict([data['input']])
    return {'prediction': int(prediction[0])}

if __name__ == '__main__':
    app.run()
