import pandas as pd

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)
print(df)

print("\nEXploring Data column:")

print(df["Age"])

#create series from scratch
ages = pd.Series([22,35,58], name="Ages")

print(ages) #print created Series

#print max value form series
print("\nMax age: ", ages.max())

#print max value of ages from dataframe
print("\nThe max value is: ", df["Age"].max())

print()

#Basic statistics of data from the data table
print(df.describe())

