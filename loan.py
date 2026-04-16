from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
import numpy as np

X = np.array([
    #salary,credit score and if there is existing loan
    [33000,550,1],
    [65000,630,0],
    [70000,670,0],
    [85000,710,1],
    [35000,330,0],
    [43000,560,1]
])

y = np.array([0,1,1,1,0,0])

model = LogisticRegression()
model.fit(X,y)

prediction = model.predict([[75000,720,0]])
print("if 0 is output loan is rejected and if the output is 1 loan is approved :",prediction)