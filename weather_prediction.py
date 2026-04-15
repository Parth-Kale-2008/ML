import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB

data = {
    'Outlook': ['Sunny','Sunny','Overcast','Rain','Rain','Rain','Overcast'],
    'Temperature': ['Hot','Hot','Hot','Mild','Cool','Cool','Cool'],
    'Humidity': ['High','High','High','High','Normal','Normal','Normal'],
    'Wind': ['Weak','Strong','Weak','Weak','Weak','Strong','Strong'],
    'Play': ['No','No','Yes','Yes','Yes','No','Yes']
}

df = pd.DataFrame(data)

le = LabelEncoder()
for column in df.columns:
    df[column] = le.fit_transform(df[column])

X = df.drop('Play', axis=1)
y = df['Play']

model = GaussianNB()
model.fit(X, y)

sample_df = pd.DataFrame([[2, 2, 1, 1]], columns=X.columns)
prediction = model.predict(sample_df)

print("Prediction:", "Yes" if prediction[0] == 1 else "No")