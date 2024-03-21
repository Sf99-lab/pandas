#In this script we create new columns drived from existing columns
import pandas as pd

air_quality = pd.read_csv("./air_quality_no2.csv", index_col=0, parse_dates=True)

print(air_quality.head())

air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882

print(air_quality.head()) #this will show the csv file with one more column

#check the ratio of the values in Paris versus Antwerp and save the result in a new column.
air_quality["ratio_paris_antwerp"] = (
    air_quality["station_paris"] / air_quality["station_antwerp"]
)

print(air_quality.head())

#rename the data columns
air_quality_renamed = air_quality.rename(
    columns={
        "station_antwerp": "BETR801",
        "station_paris": "FR04014",
        "station_london": "London Westminster",
    }
)

print(air_quality_renamed.head())

#convert column names to lowercase letter
air_quality_renamed = air_quality_renamed.rename(columns=str.lower)
print(air_quality_renamed)

