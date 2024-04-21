import pandas as pd

titanic = pd.read_csv("sample_data/titanic.csv")
print(titanic.head())

air_quality = pd.read_csv("sample_data/air_quality_long.csv", index_col="date.utc", parse_dates=True)
print(air_quality)


#Now we reshape the layout of Tables
# First we sort table rows
print(titanic.sort_values(by="Age").head())

#Now I want to sort the Titanic data according to the cabin class and age in descending order.
print(titanic.sort_values(by=['Pclass', 'Age'], ascending=False).head())