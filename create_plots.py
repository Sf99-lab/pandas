import pandas as pd
import matplotlib.pyplot as plt

air_quality = pd.read_csv('./air_quality_no2.csv', index_col=0, parse_dates=True)
print(air_quality.head())

#Visual Check of the data
air_quality.plot()

plt.show()

#Visual of Station Paris
air_quality['station_paris'].plot()
plt.show()

#visually compare the NO2 values measured in London versus Paris
air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
plt.show()

# Assuming air_quality is your DataFrame
methods = [
    method_name
    for method_name in dir(air_quality.plot)
    if not method_name.startswith("_")
]

print(methods)


#box plot
air_quality.plot.box()
plt.show()

#columns in a separate subplot
axs = air_quality.plot.area(figsize=(12,4), subplots=True)
plt.show()

#customize, extend or save the resulting plot
fig, axs = plt.subplots(figsize=(12, 4))

air_quality.plot.area(ax=axs)

axs.set_ylabel("NO$_2$ concentration")

fig.savefig("no2_concentrations.png")

plt.show()