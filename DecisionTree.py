import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = {
    "Age":["25-30","31-35","36-40","41-45","46-50","51-55","56-60"],
    "salary":["80-100k","110-150k","160-200k","200-2300k","231-2500k","2100-2150k","1500-1600k"],
    "existing_loan":["yes","yes","yes","no","no","yes","no"],
    "loan_will_approve":["no","no","yes","yes","yes","no","yes"]
}

df = pd.DataFrame(data)
df_encoded = pd.get_dummies(df)

X = df_encoded.drop("loan_will_approve_yes", axis=1)
y = df_encoded["loan_will_approve_yes"]

model = DecisionTreeClassifier(criterion="gini", max_depth=4)
model.fit(X, y)

test_data = pd.DataFrame({
    "Age":["56-60"],
    "salary":["1500-1600k"],
    "existing_loan":["no"]
})

test_encoded = pd.get_dummies(test_data)
test_encoded = test_encoded.reindex(columns=X.columns, fill_value=0)
prediction = model.predict(test_encoded)

print("If loan is approved 1 will be displayed else 0:", prediction)
