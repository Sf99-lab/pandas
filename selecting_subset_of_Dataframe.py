import pandas as pd

titanic = pd.read_csv("./titanic.csv")

print(titanic.head())

#select specific column from the dataframe
ages = titanic["Age"]
print("\nSelecting Age column from the datafram:")
print(ages)

#checking type of the output
print("\n Type of the Output: ", type(ages))
#OR
print("\n", type(titanic["Age"]))

#shape of the output
print('\n Shape of the Output: ', titanic['Age'].shape)

#age and sex of titanic passengers
age_sex = titanic[['Age', 'Sex']]
print("\n",age_sex.head())
print()
print(type(titanic[['Age', 'Sex']]))

print(titanic[['Age', 'Sex']].shape)

#passengers older than 35 years
above_35 = titanic[titanic['Age'] > 35 ]
print(above_35.head())

#check
print(titanic['Age'] > 35)
print(above_35.shape)
print(titanic.shape)

#selecting passengers form cabin class 2 and 3
class_23 = titanic[titanic['Pclass'].isin([2,3])]
print("Passenger from Cabin class 2 and 3: ",class_23)
print(class_23.shape)

#passengers data with age is known
age_not_null = titanic[titanic['Age'].notna()]
print("Passengers with known ages: ")
print(age_not_null)
print(age_not_null.shape)

#selecting specific row and column
row_column = titanic.loc[titanic['Age'] > 35, 'Name']
print(row_column)

#Choosing slice from the Dataframe(rows 10 till 25 and columns 3 to 5.)
slice_from_dataframe = titanic.iloc[9:25, 2:5]
print(slice_from_dataframe)

#assignoing new values to the first 3 elements of the fourth column:
titanic.iloc[0:3, 3] = "anonymous"
print(titanic.head())
print(titanic['Name'].head())