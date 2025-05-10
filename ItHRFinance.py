import pandas as pd

data = {
    'employee_id': range(1, 11),
    'department': ['IT', 'IT', 'IT', 'HR', 'HR', 'Finance', 'Finance', 'Finance',
                   'Finance', 'Finance'],
    'salary': [120000, 125000, None, 70000, None, 90000, None, 95000, None, 100000]
}
df = pd.DataFrame(data)
print(df)

df['salary_filled'] = df.groupby('department')['salary'].transform(lambda x: x.fillna(x.median()))
top_department = df.groupby('department')['salary_filled'].mean().idxmax()
print(top_department)   #IT