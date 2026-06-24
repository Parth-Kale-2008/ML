import pandas as pd

data = pd.read_csv("employee_sales_data.csv")

data = data.drop_duplicates(subset=[
    'Employee_ID',
    'Name',
    'Department',
    'Join_Date',
    'Salary',
    'City',
    'Sales'
])

print(data['Employee_ID'].is_unique)
data['Join_Date'] = pd.to_datetime(data['Join_Date'], errors='coerce')
data['Salary'] = data['Salary'].fillna(data["Salary"].median())
data['Salary'] = data['Salary'].apply(lambda x: f"{x:,.0f}")
data['City'] = data['City'].str.title()
data['City'] = data['City'].replace({"Bangalore": "Bengaluru"})
data["Sales"] = pd.to_numeric(data["Sales"], errors="coerce")

data.to_csv("Newfile.csv", index=False)
print("New CSV created successfully")