# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import seaborn as sns
import pickle

from flask import Flask
from flask import request
from flask import jsonify

with open('model1.bin', 'rb') as f_in:
    model = pickle.load(f_in)

with open('dv.bin', 'rb') as f_in:
    dv = pickle.load(f_in)

app = Flask('credit')

client = {"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes" }

@app.route('/predict', methods=['POST'])
def predict():
   client = request.get_json()
   X = dv.transform([client])
   predict = round(model.predict_proba(X)[0,1],3)

   credit_accepted = predict >= 0.5
   result = {
      'credit_probability' : float(predict),
      'credit_accepted': bool(credit_accepted)
   }
   return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
