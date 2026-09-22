import pandas as pd
data = {'name':['alice','bob','charlie'],
        'age':[25,30,35],
        'city':['new york','los angeles','chicago']}

df = pd.DataFrame(data)
print("dataframe:\n", df)

average_age = df['age'].mean()
print("\nAverage age:", average_age)

filtered_df = df[df['age'] > 28]
print("\nFiltered dataframe(age > 28):\n",filtered_df)

df['salart'] = [50000,60000,70000]
print("\nDataframe with salary column:\n", df)
