from flask import Flask, request
import numpy as np
import random

app = Flask(__name__)

history = ["Historiography and Historical Methodologies", "World History and Globalization",
           "Colonialism and Post-Colonialism", "The Cold War and Its Impact", "The Rise and Fall of Empires", "Comparative Revolutions", "Gender and History", "Environmental History", "War and Society", "Intellectual History"]


@app.route('/predict', methods=['POST'])
def predict():   
    random_history = random.sample(history, 3)
    print(random_history)
    return random_history


if __name__ == '__main__':
    app.run()
