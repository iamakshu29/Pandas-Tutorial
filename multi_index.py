import pandas as pd

burger = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/bigmac.csv",parse_dates=["Date"], date_format="%Y-%m-%d").dropna(how="all")
# print(burger)
burger["Date"] = burger["Date"].astype("category")
burger["Country"] = burger["Country"].astype("category")
# print(burger.nunique())
# print(burger.info())

"""
Create a MultiIndex

1. A mutliIndex is an index with multiple levels or layers
2. Pass the "set_index()" method a list of column names to create a multi-index DataFrame. It is a COPY
3. The order of the list's values will determine the order of the levels
4. Alternatively, we can pass the read_csv function's index_col paramter a list of columns

NOTE :- we know Index must be unique to extract the further values effectively but when we don't have any column that have unique values all along
then we combine 2 or more column to make it unique and that multi columns when combine together to form an Index is called MultiIndex.


NOTE :- Try to choose the outermost index which has less unique values. df.nunique()
In this case 
Date = 33 unique   <-- Choose this first
Country = 57 unique
"""

    # 2nd point
burger2 = burger.set_index(keys = ["Date","Country"]).sort_index()
# print(burger2)

burger2 = burger.set_index(keys = ["Country","Date"]).sort_index()
# print(burger2)

    # 4th point
burger = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/bigmac.csv",parse_dates=["Date"], date_format="%Y-%m-%d",index_col=["Date","Country"]).dropna(how="all").sort_index()
# print(burger)

"""
Some methods on MultiIndex
"""
    # all indexes
# print(burger.index)
    # column name
# print(burger.index.names)
    # access first value gives tuple as object or type of data
# print(burger.index[0])



"""
Extract Index Level Values
1. The "get_level_values" method extract an Index with the values from one level in the MultiIndex.
2. Invoke the "get_level_values" on the MultiIndex, not the DataFrame itself. ie after df.index.
3. The method expects either the level's index position (0) or its name("abc").

NOTE :- can extract only one level at a time not like ("da","asda") or (1,2,3)

"""

# print(burger.index.get_level_values(0))
# print(burger.index.get_level_values("Date"))

# print(burger.index.get_level_values(1))
# print(burger.index.get_level_values("Country"))



"""
Rename Index Labels :- 
1. Invoke the "set_names" method on the MultiIndex to change one or more level names.
2. Use the names and level parameter to target a nested index at a given level
3. Alternatively, pass names a list of strings to overwrite all level names.
4. The "set_names" method return a "COPY", so replace the original index to alter the DataFrame.
"""

    # 2nd point
# burger.index = burger.index.set_names(names="Start Date",level="Date")
# burger.index = burger.index.set_names(names="Start Date",level=0)

# burger.index = burger.index.set_names(names="Start Date",level="Country")
# burger.index = burger.index.set_names(names="Countries",level=1)


    # 3rd point
burger.index = burger.index.set_names(names=["Start Date","Location"])
# print(burger)



"""
The sort_index Method on MultiIndex DataFrame.
1. using the sort_index() method, we can target all levels or specific levels of MutliIndex
2. To apply a different sort order to different levels, pass a list of Booleans.
3. Number of Booleans in a list is equals to number of levels of MultiIndex.

EXPLAINATION :- This way we can sort as per the levels like level 0 we need in Asc so we put True, level 1 we need Desc so we put False

NOTE 
It is a COPY (ie assign to DataFrame to get the correct results)
Sort in levels from left to right OR outermost to innermost OR level 0 to 1 to 2 to .....
"""

burger = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/bigmac.csv",parse_dates=["Date"], date_format="%Y-%m-%d",index_col=["Date","Country"]).dropna(how="all")
burger = burger.sort_index(ascending=[True,False])
# print(burger)


"""
Extract Rows from a MultiIndex DataFrame
1. A tuple is an immutable list. It can't be modified after creation.
2. Create a tuple with a comma between elements. The community conversation is to wrap the elements in paranthesis
3. The iloc and loc accessors are available to extract rows by index position or label
4. For the label accessor, pass a tuple to hold the labels from the index levels.

NOTE :-
we give the first value in loc for row and second for column
so to determin which 2nd value is multiIndex or which is column
we used tuple ie () and contain the multiIndex inside tuple as one parameter.
"""

burger = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/bigmac.csv",parse_dates=["Date"], date_format="%Y-%m-%d",index_col=["Date","Country"]).dropna(how="all").sort_index()

# print(burger.iloc[2]) 

# print(burger.loc["2000-04-01"])

# print(burger.loc[("2000-04-01","Britain")])

# print(burger.loc[("2000-04-01","Britain"),"Price in US Dollars"])

start = ("2000-04-01","Hungary")
end = ("2000-04-01","Poland")

# print(burger.loc[start:end])
# print(burger.loc[start:,"Price in US Dollars"])


"""
The Transpose Method
The transpose method inverts the horizontal and vertical axes of DataFrame.

"""

start = ("2018-01-01","China")
end = ("2018-01-01","Denmark")

transposed = burger.loc[start:end].transpose()
# print(transposed)



"""
The Stack Method

1. The stack() method moves the column index to row index alon with other indexes already present
2. Pandas will return a MultiIndex Series
3. Think of it like "Stacking" index levels for a MultiIndex.

NOTE :-

It became a Series Datatype as there are only rows now ..not column
only One values has now Multiple Identifier...
Example
for popualtion 8.99 has 3 Idnetifiers which are =>
Year (1960) -> country (Afghanistan) -> Population -> 8.99

"""


stats = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/worldstats.csv").dropna(how="all").sort_index()

# print(stats)
# print(stats.nunique()) 
    # This df needs to have MultiIndex as this df doesnot have a unique column to make Index alone
    # and by doing nunique we found that year has less unique levels so the outermost level will be year then Country will be second Idnex of MultiIndex DataFrame

stats = stats.set_index(keys=["year","country"]).sort_index()

# print(stats.head())
# print("\n\n\n")
# print(stats.stack())



"""
The Unstack Method

1. It moves the row index to the column index  (inverse of stack method).
2. By Default "unstack" method will move the "innermost" index
3. We can customize the moved index with the "level" parameter.
4. The "level" parameter accepts the level's index postion or its name. It can also accepts a list of postions/names.

0 is outermost left to right level goes
"""

stacked_stats = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/worldstats.csv",index_col=["year","country"]).dropna(how="all").sort_index().stack()
# print(stacked_stats.head())
# print(stacked_stats.unstack().head())
# print(stacked_stats.unstack(level=1).head())
# print(stacked_stats.unstack(level="year").head())
# print(stacked_stats.unstack(level=[1,2]).head())
# print(stacked_stats.unstack(level=["year","country"]).head())



"""
The Pivot Method

1. The "pivot()" method reshapes data from a tall format to a wide format.
2. Ask yourself which direction the data will expand in if you add more entries.
3. A tall/long format exapands down. A wide format expands out.
4. The index parameter sets the column as index of the pivoted DataFrame.
5. The column parameter sets the column whose values will be the columns in the pivoted DataFrame.
6. The values parameter sets the columns to show in the pivoted DataFrame. 
7. Pandas will populate the correct values (ie remove NaN values )based on the index and column intersections.

"""
salesmen = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/salesmen.csv",parse_dates=["Date"], date_format="%m/%d/%Y").dropna(how="all")

# print(salesmen)
# print(salesmen.pivot(index="Date",columns="Salesman",values="Revenue"))




"""
The Melt Method

1. Reverse of "pivot()" method
2. It is ideal when you have multiple columns storing the same data point.
3. The "id_vars" parameter accepts the column whose values will be repeated for every column.
4. The "var_name" parameter sets the name of the new column for the varying values (the former column names).
5. The "value_name" parameter set the new name of the values column (holding the values from the original DataFrame).

default name for var_name = variable
default for value_name = value
"""
quarter = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/quarters.csv").dropna(how="all")
# print(quarter)
# print(quarter.melt(id_vars="Salesman",var_name="Quarters",value_name="Revenue"))



"""
The pivot_table Method

1. The pivot_table() method operates similarly to the Pivot Table features in MS Excel
2. A pivot table is table whose values are aggreagations of groups of value from another table
3. The "value" parameter accepts the numeric column whose values will be aggregated
4. The "aggfunc" parameter declares the aggregation function ("the default is mean/average").
5. The "index" parameter sets the index labels of the pivot table. MultiIndexes are permitted.
6. The "columns" paramter sets the column labels of the pivot table. MultiIndexes are permitted.

"""

food = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/foods.csv").dropna(how="all")
# print(food)

pivot_table = food.pivot_table(values="Spend",index="Gender")
# print(pivot_table)
pivot_table = food.pivot_table(values="Spend",index="Gender",columns="City",aggfunc="sum")
# print(pivot_table)
pivot_table = food.pivot_table(values="Spend",index="Item",aggfunc="sum")
# print(pivot_table)
pivot_table = food.pivot_table(values="Spend",index=["Gender","Item"],columns="City",aggfunc="sum")
# print(pivot_table)
pivot_table = food.pivot_table(values="Spend",index="Item",columns=["Gender","City"],aggfunc="sum")
# print(pivot_table)
pivot_table = food.pivot_table(values="Spend",index="Item",columns=["Gender","City"],aggfunc="count")
# print(pivot_table)
pivot_table = food.pivot_table(values="Spend",index="Item",columns=["Gender","City"],aggfunc="max") # similarly min is also present
# print(pivot_table)