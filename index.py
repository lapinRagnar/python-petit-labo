import pandas as pd

air_quality = pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True)

# quich show of the csv
print("air_quality.head()", air_quality.head())

# I want a quick visual check of the data.
air_quality.plot()

# I want to plot only the columns of the data table with the data from Paris.
air_quality["station_paris"].plot()

# I want to visually compare the values measured in London versus Paris.
air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)

# a boxplot.
air_quality.plot.box()

# I want each of the columns in a separate subplot.
air_quality.plot.area(figsize=(12, 4), subplots=True)


# How to create new columns derived from existing columns
# I want to express the concentration of the station in London in mg/m
# (If we assume temperature of 25 degrees Celsius and pressure of 1013 hPa, the conversion factor is 1.882)
air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882
air_quality.head()


"""
To create a new column, use the [] brackets with the new column name at the left side of the assignment.
Note
The calculation of the values is done element-wise. This means all values in the given column are multiplied by the value 1.882 at once. You do not need to use a loop to iterate each of the rows!
"""

# I want to check the ratio of the values in Paris versus Antwerp and save the result in a new column.
air_quality["ratio_paris_antwerp"] = (air_quality["station_paris"] / air_quality["station_antwerp"])
air_quality.head()



