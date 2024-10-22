# Working with Date and Time
import pandas as pd

import datetime as dt


"""
datetime is built in Python Programming Module
The datetime module includes date and datetime classes for representing dates and datetimes.
The date constructor accepts arguements of year, month and day. Python defaults to 0 for any missing values.
The datetime constructor accepts arguement for year, month, day, hour, minute and second.
"""

date = dt.date(2024,12,2)
# print(date)
# print(date.year, " ", date.month, " " , date.day)

time = dt.datetime(2024,12,2,8,13,59)
# print(time)
# print(time.hour, " ", time.minute, " " , time.second)


"""
The TimeStamp and DateIndex Objects

Pandas ships with many classes related to datetimes
The Timestamp is similar to Python's datetime object (but with expanded functonality)
A DatetimeIndex is an index of Timestamp objects
The TimeStamp constructor accepts a string, a datetime object or equivalent arguement to the datetime class.
"""
# print(pd.Timestamp(2024,9,20))
# print(pd.Timestamp(2027,12,3,18,24,49))
# print(pd.Timestamp(dt.date(2024,12,2)))
# print(pd.Timestamp(dt.datetime(2024,12,2,8,13,59)))
# print(pd.Timestamp("2024-9-20"))
# print(pd.Timestamp("2024/9/20"))
# print(pd.Timestamp("2024-9-20 08:30:54"))

    #can also make a series
series = pd.Series([pd.Timestamp("2024-9-20 08:30:54")])
# print(series)
# print(series.iloc[0])

index = pd.DatetimeIndex(["2024-9-20","2023-10-24"])
# print(index)
# print(index[0])
# print(type(index[0]))



"""
Create range of Dates with pd.date_range function

This func generates and returns a DatetimeIndex holding a sequence of dates
func of requries 2 of the 3 parameters(start, end, periods)
with Start and end, Pandas will assume a daily interval
Every element in DateTimeIndex is a timestamp.

D is for Days
B is Business Days Mon - Fri only
W is weekly jump by default it start from Sunday
W-(dayname)
h jump in terms of Hours
6H 6hr ahead
ME for Month End
MS for Month Start
YE for Year End
YS for Year Start

we can also combine frequecies for day and hrs like freq = "24D 3H"

periods It tells how many values to include in Final result
"""

range = pd.date_range(start="2025-01-01",end="2025-01-07")
# print(range)
    # freq = "D" is default
range = pd.date_range(start="2025-01-01",end="2025-01-07",freq="D")
# print(range)

range = pd.date_range(start="2025-01-01",end="2025-01-07",freq="2D")
# print(range)

range = pd.date_range(start="2025-01-01",end="2025-01-07",freq="B")
# print(range)

range = pd.date_range(start="2025-01-01",end="2025-01-31",freq="W")
# print(range)

range = pd.date_range(start="2025-01-01",end="2025-01-31",freq="W-WED")
# print(range)

range = pd.date_range(start="2025-01-01",end="2025-01-31",freq="h")
# print(range)

range = pd.date_range(start="2025-01-01",end="2025-01-31",freq="6h")
# print(range)

range = pd.date_range(start="2025-01-01",end="2025-12-31",freq="ME")
# print(range)

range = pd.date_range(start="2025-01-01",end="2025-12-31",freq="MS")
# print(range)

range = pd.date_range(start="2025-01-01",end="2030-12-31",freq="YE")
# print(range)

range = pd.date_range(start="2025-01-01",end="2030-12-31",freq="YS")
# print(range)


    # understand Period Paramter
    # It tells how many values to include in Final result
range = pd.date_range(start="2025-01-01", freq="D", periods=25)
# print(range)

range = pd.date_range(start="2025-01-01", freq="2D", periods=25)
# print(range)

range = pd.date_range(end="2025-01-31", freq="2D", periods=25)
# print(range)

"""
The dt Attribute

The dt attribute reveals a DateTimeProperties object with attributes/methods for working with datetimes.
It is similar to str attribute for String Methods
The DateTimeProperties object has attributes like day, month and year to reveal information about each date in Series.
The day_name method returns the written day of the week
Attribute like is_month_end and is_quarter_start return Boolean Series.
"""

series = pd.Series(pd.date_range(start="2000-01-01", end = "2020-12-31", freq="24D 3h"))
# print(series)
# print(series.dt.day, " " , series.dt.month, " ", series.dt.year, " " , series.dt.hour, " " , series.dt.day_of_year, " " , series.dt.day_name())
# print(series.dt.is_month_end)
# print(series.dt.is_month_start)
# print(series[series.dt.is_month_start])




"""
Selecting Rows from a DataFrame with a DataTimeIndex

The iloc is available for index-based extraction
The loc accessor is accepts string for TimeStamps to extract by index label/value.NOTE that Python's datetime object will not work.
Use list slicing to extract a sequence of dates. The truncate method is another alternative.

"""

ibm = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/ibm.csv",parse_dates=["Date"],index_col=["Date"]).sort_index()
# print(ibm)

# print(ibm.iloc[200])
# print(ibm.loc["2023-10-06"])
# print(ibm.loc[pd.Timestamp(2023,10,6)])
# print(ibm.loc["2014-03-04" : "2014-12-31"])
# print(ibm.loc[pd.Timestamp(2014,3,4) : pd.Timestamp(2014,12,31)])
# print(ibm.truncate("2014-03-04","2014-12-31"))
# print(ibm.loc["2023-10-06","Close"])
# print(ibm.loc["2023-10-06","High":"Close"])
# print(ibm.loc[pd.Timestamp(2014,3,4) : pd.Timestamp(2014,12,31), "High":"Close"])




"""
The DateOffSet Object

A DateOffSet Object add time to a TimeStamp to arrive at a new TimeStamp
The DateOffSet constructor accepts days, weeks, months, years parameters and more.
We can pass a DateOffSet object to the freq parameter of the pd.date_range function.

Simply
It can add or substract the number of days months weeks or years to our current DF Date column or Date Index..

How to do...extract the index attribute and add the DateOffset using +/- sign
"""

# print(ibm.index)

# print(ibm.index + pd.DateOffset(days=5))
# print(ibm.index - pd.DateOffset(days=5))
# print(ibm.index + pd.DateOffset(months=3))
# print(ibm.index - pd.DateOffset(years=1))
# print(ibm.index + pd.DateOffset(hours=7))
# print(ibm.index + pd.DateOffset(years=1, months=3, days=5, hours=14, minutes=23, seconds=12))

    # Can use DateOffset in freq Parameter too
# print(pd.date_range(start="1991-09-20", end="2024-09-20", freq=pd.DateOffset(years=1)))


"""
Specialized DateOffSets

pd.tseries.offsets
we can add different amount of time to each data (month end, quarter end, year begin)
"""

# print(ibm.index + pd.tseries.offsets.MonthEnd())
# print(ibm.index - pd.tseries.offsets.MonthEnd())
# print(ibm.index + pd.tseries.offsets.MonthBegin())

# print(ibm.index + pd.tseries.offsets.QuarterEnd())
# print(ibm.index - pd.tseries.offsets.QuarterEnd())

# print(ibm.index - pd.tseries.offsets.QuarterEnd(startingMonth=1))
# print(ibm.index - pd.tseries.offsets.YearBegin())




"""
Timedeltas

1. A Timedelta is a Pandas object that represents a duration (an amount of time)
2. Substracting two TimeStamp object will yield a Timedelta object (this applies to substracting a Series from another Series).
3. The Timedelta constructor accepts parameters for time as well as String descriptions.

"""

    # 2nd point
# print(pd.Timestamp("2023-03-31 12:30:48") - pd.Timestamp("2023-03-20 19:25:59"))
# print(pd.Timestamp("2023-03-20 19:25:59") - pd.Timestamp("2023-03-31 12:30:48"))


    # 3rd point
# print(pd.Timedelta(days=3, hours=2, minutes=5))
# print(pd.Timedelta("3 days"))
# print(pd.Timedelta("3 days 2 hours 5 minutes"))



ecom = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/ecommerce.csv",parse_dates=["order_date","delivery_date"],date_format="%m/%d/%y")
print(ecom)