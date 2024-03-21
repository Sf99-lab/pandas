import pandas as pd

titanic = pd.read_csv("./titanic.csv")

print(titanic.head())

#Average age of titanic passengers
avg_age = titanic["Age"].mean()
print(avg_age)

#the median age and ticket fare price of the Titanic passengers
median_age_fare = titanic[["Age", "Fare"]].median()
print(median_age_fare)

#ggregating statistics
agr_statistics = titanic[["Age", "Fare"]].describe()
print(agr_statistics)

#Instead of the predefined statistics, specific combinations of aggregating statistics for given columns can be defined using the DataFrame.agg() method:
custom_aggregate = titanic.agg(
    {
        "Age": ["min", "max", "median", "skew"],
        "Fare": ["min", "max", "median", "mean"],
    }
)

print(custom_aggregate)

#the average age for male versus female Titanic passengers
print(titanic[["Sex", "Age" ]].groupby("Sex").mean())

'''we explicitly selected the 2 columns first. If not, the mean method is
applied to each column containing numerical columns by passing numeric_only=True:'''
explicit_selection_column = titanic.groupby('Sex').mean(numeric_only=True)
print(explicit_selection_column)

#Average age for each gender
avg_age_each_gender = titanic.groupby('Sex')["Age"].mean()
print((avg_age_each_gender))

#mean of ticket fare price for each sex
fare_mean = titanic.groupby(["Sex", "Pclass"])["Fare"].mean()
print(fare_mean)

#number of passengers in each cabin classes
print(titanic["Pclass"].value_counts())
