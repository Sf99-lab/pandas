import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv("sample_data/titanic.csv")
air_quality = pd.read_csv("sample_data/air_quality_long.csv", index_col="date.utc", parse_dates=True)

#The subset of data will be called no2_subset.
# filter for no2 data only
no2 = air_quality[air_quality["parameter"] == "no2"]

#now we use 2 measurements (head) for each location (groupby)
no2_subset = no2.sort_index().groupby(["location"]).head(2)
print(no2_subset)

#display the three stations as separate columns next to each other.
three_sep_column = no2.pivot(columns="location", values="value")
print(three_sep_column)

print(no2.head())

#plotting of multiple columns
ax = no2.pivot(columns="location", values="value").plot()
plt.show()

# mean concentrations for NO2
#  and PM2.5
#  in each of the stations in table form
concentration = air_quality.pivot_table(
    values="value", index="location", columns="parameter", aggfunc="mean"
)
print(concentration)

# add a new index to the DataFrame with reset_index().
no2_pivoted = no2.pivot(columns="location", values="value").reset_index()

print(no2_pivoted.head())

# collect all air quality NO2 measurements in a single column (long format).
no_2 = no2_pivoted.melt(id_vars="date.utc")
print(no_2)

#The parameters passed to pandas.melt() can be defined in more detail:
no_2 = no2_pivoted.melt(
    id_vars="date.utc",
    value_vars=["BETR801", "FR04014", "London Westminster"],
    value_name="NO_2",
    var_name="id_location",
)
print(no_2.head())