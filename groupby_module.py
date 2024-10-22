import pandas as pd

fortune = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/fortune1000.csv",index_col="Rank").dropna(how="all")
print(fortune)

"""
The GroupBy Method
Grouping is a way to organize the data based on column's values
The groupby() method returns a DataFrameGroupBy object. It resembles a group of DataFrames in a dictionary like structure
The DataFrameGroupBy object can perform aggregate operations on each group within it.

"""


sectors = fortune.groupby("Sector")

    # check the type DataFrameGroupBy
# print(sectors)

    # Give unique values of the column
# print(len(sectors))

    # Gives the count of each value come in that column
# print(sectors.size())

    # print the rows with first occurance of the Sector
# print(sectors.first())

    # print the rows with last occurance of the Sector
# print(sectors.last())


"""
Retrieve a Group with the get_group Method
The get_group method on the DataFrameGroupBy object retrieve a nested DataFrame belonging to a specific group/category.
"""
# print(sectors.get_group("Energy"))


"""
Method on the GroupBy Object

1. use [] on the DataFrameGroupBy object to "extract" a column from the original DataFrame
2. The resulting SeriesGroupBy object will have aggregation methods available on it.
3. Pandas will perform the calculation on every group within the collection
4. For example, the sum() method will sum together the Revenues for every row by group/categary

"""
    # this much code gives sum results for only one type of sector
# print(fortune[fortune["Sector"]=="Retailing"]["Revenue"].sum())

    # by using groupby() method on a column we can further use aggreagate methods on groupBy Object
    # to get the results for all types of groups present in a column
# print(sectors["Revenue"].sum())
# print(sectors["Employees"].sum())
# print(sectors["Employees"].mean())
# print(sectors["Profits"].max())
# print(sectors["Profits"].min())
# print(sectors[["Employees","Profits"]].sum())




"""
Grouping by Multiple Columns

1. Pass a list of columns to the groupby method to group by pairings of values across columns
2. Target a column to retrieve the SeriesGroupBy object, then perform an aggregation with a method
3. Pandas will return a MultiIndex Series where the levels will be original groups

"""

grouping = fortune.groupby(["Sector","Industry"])
# print(grouping)
# print(len(grouping))
# print(grouping.size())
# print(grouping["Revenue"].sum())
# print(grouping["Employees"].mean())



"""
The agg Method

1. The "agg()" method applies different aggragation methods on different columns
2. Invoke the agg method directly on DataFrameGroupBy object
3. Pass the method a dictionary where the keys are the columns and the values are the aggregation operations.

NOTE :- 
similar to simple aggragation we do...it just 
agg() return the DataFrame where as .sum() return Series

Only advantage is we can provide multiple key-value pairs in one line or under one method
"""

# print(sectors.agg({"Revenue":"sum"}))
    # OR both have same functioning...
# print(sectors["Revenue"].sum())

    # Advantage :- can provide multiple key-value pairs to get multiple results with diff aggregate methods.
# print(sectors.agg({"Revenue":"sum","Employees":"min","Profits":"max"}))




"""
Iterating through Groups

1. The DataFrameGroupBy object supports the "apply()" method (just like a Series and a DataFrame do)
2. The apply method invokes on evert nested DataFrame in DataFrameGroupBy object
3. It captures the return values of the functions and collects them in a new DataFrame ( the return value).

"""

def max_emp_count(sector):
    return sector.nlargest(2,"Employees")


print(sectors.apply(max_emp_count))

"""
DeprecationWarning: DataFrameGroupBy.apply operated on the grouping columns.
This behavior is deprecated, and in a future version of pandas the grouping columns will be excluded from the operation.
Either pass `include_groups=False` to exclude the groupings or explicitly select the grouping columns after groupby to silence this warning.
"""

