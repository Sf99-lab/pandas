import pandas as pd

# read data
titanic = pd.read_csv("./titanic.csv")

print(titanic)

# I want to see the first 8 rows of a pandas DataFrame.
print("\nFirst 8 rows:")
print(titanic.head(8))

print()

# A check on how pandas interpreted each of the column data types
print(titanic.dtypes)

# store Titanic data to a spreadsheet.
titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)

#Reload the data to a Dataframe
titanic = pd.read_excel("titanic.xlsx", sheet_name="passengers")
print()
print(titanic)

print(titanic.head()) #display first five rows

print()

#Technical summary of a Dataframe
print(titanic.info())
