import pandas as pd

air_quality_no2 = pd.read_csv("sample_data/air_quality_no2_long.csv",
                              parse_dates = True)

air_quality_no2 = air_quality_no2[["date.utc", "location",
                                   "parameter", "value"]]
print("                  Table1 data\n", air_quality_no2.head())

air_quality_pm25 = pd.read_csv("sample_data/air_quality_pm25_long.csv",
                               parse_dates=True)
air_quality_pm25 = air_quality_pm25[["date.utc", "location",
                                     "parameter", "value"]]

print("                  Table2 data\n", air_quality_pm25.head())

print('''  \n\n       It is Time to concatinate two Tables with similar structure, in a single table''')

air_quality = pd.concat([air_quality_pm25, air_quality_no2], axis=0)

print("\n", air_quality.head())

print("\n              lets verify the operation\n")
print('Shape of the ``air_quality_pm25`` table:  ', air_quality_pm25.shape)
print('Shape of the ``air_quality_no2`` table: ', air_quality_no2.shape)
print('Shape of the resulting ``air_quality`` table: ', air_quality.shape)
print('Hence the resulting table has 3178 = 1110 + 2068 rows')

print('\n\n          Another way to verify it\n')
'''Sorting the table on the datetime information illustrates also the 
combination of both tables, with the parameter column defining the origin of
 the table (either no2 from table air_quality_no2 or pm25 from table air_quality_pm25):'''
air_quality = air_quality.sort_values("date.utc")
print(air_quality.head())

'''In this specific example, the parameter column provided by the data
 ensures that each of the original tables can be identified. '''
air_quality = pd.concat([air_quality_pm25, air_quality_no2],
                        keys=['PM25', 'NO2'])
print(air_quality.head())
'''Add the station coordinates, provided by the stations metadata table,
 to the corresponding rows in the measurements table.'''
print('''\n            Join table using a common identifier''')
stations_coord = pd.read_csv("sample_data/air_quality_stations.csv")
print("\n", stations_coord.head())
print(air_quality.head())

air_quality = pd.merge(air_quality, stations_coord, how="left", on="location")
print(air_quality.head())

'''Using the merge() function, for each of the rows in the 
air_quality table, the corresponding coordinates are added from
 the air_quality_stations_coord table. Both tables have the 
 column location in common which is used as a key to combine 
 the information. By choosing the left join, only the locations 
 available in the air_quality (left) table, i.e. FR04014, 
 BETR801 and London Westminster, end up in the resulting table.
  The merge function supports multiple join options similar to 
  database-style operations.'''

'''Next we add air quality parameters metadata stored in a data file air_quality_parameters.csv'''

air_quality_parameters = pd.read_csv('sample_data/air_quality_parameters.csv')
print(air_quality_parameters.head())
air_quality = pd.merge(air_quality, air_quality_parameters,
                       how='left', left_on='parameter', right_on='id')
print(air_quality.head())



'''REMEMBER
Multiple tables can be concatenated both column-wise and row-wise using the concat function.

For database-like merging/joining of tables, use the merge function.'''