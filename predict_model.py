# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import seaborn as sns
import pickle


#model_file = 'model_C1.bin'

#with open(model_file, 'rb') as f_in:
#    (dv, model) = pickle.load(f_in)

with open('model1.bin', 'rb') as f_in:
    model = pickle.load(f_in)

with open('dv.bin', 'rb') as f_in:
    dv = pickle.load(f_in)

client = {"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes" }

X = dv.transform([client])
predict = round(model.predict_proba(X)[0,1],3)
print(predict)

