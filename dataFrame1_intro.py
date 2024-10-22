"""
Methods and Attributes between Series and DataFrames
A DF is 2-dim table consist of rows and cols.
Pandas use 'NaN' designation for cells that have a missing value. Most Operation on 'NaN' will produce 'NaN' values
The DF and Series have common and exclusive method/attributes.
The 'hasnans' attribute exists only a Series. The 'columns' attribute exist only on a DataFrame.
The 'info' method returns a summary of the pandas object.

Common
1. head/tail methods
2. .index/.values attributes
3. shape attribute ..it gives you size of Series or DataFrame ie cols and rows
4. dtypes attriute...datatype
5. axes attriute ....give as row index and column index (in DataFrame)
6. info method....give summary related to both..like null-values, data type and more.

Exclusive to Series
1. hasnans attribute...any missing value or not....returns Bool

Exclusive to DataFrame
1. columns attribute...give all the cols name in a list.

There are so many other common and exclusive method...not gonna remember all.

"""

import pandas as pd

nba_df = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/nba.csv")
y = pd.Series([2,3,4,5,6])

# print(nba_df.head(10))
# print(y.head())

# print(nba_df.index)
# print(nba_df.values)

# print(y.index)
# print(y.values)

# print(nba_df.shape)
# print(y.shape)

# print(nba_df.dtypes)
# print(y.dtypes)

# print(nba_df.axes)
# print(y.axes)

# print(nba_df.info())
# print(y.info())

# print(nba_df.columns)
# print(y.hasnans)


"""
Differences between Shared Methods.
The sum method adds a Series's values
On a DF, the sum method defaults to adding the values by traversing the index (row values)
The 'axis' parameter customizes the direction that we add across. Pass "columns" or 1 to add "across" the columns.

axis = 0 || rows || nothing (bydefault 0) => Columns are heading 
axis = 1 || columns                       => Index is heading
"""

# print(y.sum())

    # If all cols don't have the number, some have string and all then,
    # we include usecols to get those cols which have number have then use sum() method
nba_file = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/nba.csv",usecols=["Weight"])

# print(nba_file.sum())



#  here we take another Data Frame which have all value as numbers except date..so we make date as index and then do sum on it
revenue_df = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/revenue.csv",index_col=["Date"])
# print(revenue_df.head(10))

# print(revenue_df.sum()) 
    # is same as
# print(revenue_df.sum(axis = "rows"))
    # is same as
# print(revenue_df.sum(axis = 0))

# print(revenue_df.sum(axis = "columns"))
    # is same as
# print(revenue_df.sum(axis = 1))


"""
Selecting a column from a DataFrame
we can use attribute syntax (df.column_name) to select a column from a DataFrame. The syntax will not work if the column name has spaces.
we can also use square braket suntax (df["column name"]) which will work for any name..
Pandas extracts a column from a DataFrame as Series
The Series is a view, so changes to series will affect the DataFrame.
Pandas will display a warning if you mutate the Series. Use the copy() method to create a duplicate.

"""

revenue_df2 = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/revenue.csv")
rev = revenue_df2["New York"].copy()

# print(rev)

    # can also overwrite value that's why we use copy method so that it doesnot modify the Original DataFrame
rev.iloc[2]=99999
# print(rev)

    # original value not modified
# print(revenue_df2)


"""
Selecting Multiple columns from a DataFrame
df[["","",""]] => Order is followed
also it gives a copy of original data not a view.

"""

# using nba_df
# print(nba_df[["Name","Team","Salary"]].head(10))


"""
Adding a new column to DataFrame
It is a view as we are adding new columns to original dataFrame we want to modify the df...
you can use .copy() method if you don't want to overwrite the original DF

Syntax 
1. just select the new column and assign the values
df["New Col"] = "abcd"  
( New Columns will add at the end 
same value is assigned across the column till the end)

2. To add it to specific location, we use insert method
df.insert(loc=index,column="",value=)


NOTE :-
1. If you assign a single string or value it will be copied in all the rows 
2. You are going to mostly do some calculation from an existed column or calculation for 2 or 3 cols 
and give the result to that new column..

"""

nba_df2 = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/nba.csv")
# print(nba_df2.head(10))

# New Column at the end of Table

nba_df2["Sport"] = 10
# print(nba_df2.head(10))

new_sal = nba_df2["Salary"].mul(2)

nba_df2["New Salary"] = new_sal
# print(nba_df2.head(10))


# New Column at specific Postion
new_sal = nba_df2["Salary"].div(2)
nba_df2.insert(loc=2,column="Salary After Tax",value=new_sal)
# print(nba_df2.head(10))

"""
Drop Rows with Missing Values
-> Pandas uses 'NaN' designation for cells that have a missing value
1. The "dropna" method deletes rows with missing values. It default behavior is to remove a row if it has any missing values.
    Pass the "how" parameter an arguement of "all" to delete rows only where all value are 'NaN' whereas its default is any ie any value is NaN it will delete the row
    The subset parameter customizes/limits the columns that pandas will use to drop rows with missing values.

It does COPY not VIEW.
"""

# print(nba_df)

    # both gives the same result, as default value of how param is 'any'
# print(nba_df.dropna())
# print(nba_df.dropna(how="any"))

    # remove only those cols who has all values = NaN
# print(nba_df.dropna(how="all"))

    # selecting specifically 1 col or mutliple columns...remove the row if any of the value of these col is NaN
# print(nba_df.dropna(subset=["Salary"]))
# print(nba_df.dropna(subset=["Salary","College"]))


"""
Fill in Missing Values with fillna Method
The 'fillna' method replace missing NaN values with its arguement
The 'fillna' method is available on both DataFrames and Series
An extracted Series is a VIEW on the original DataFrame but the fillna method returns a COPY.

To make changes to original DF we can overwrite the value to that column

"""
nba_df2 = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/nba.csv").dropna(how='all')
# print(nba_df2)

    # Fill all NaN with value 0
# print(nba_df.fillna(0))

    # Fill only the salary column NaN with 0
# print(nba_df2["Salary"].fillna(0))

    # Overwriting the salary column with filled values to original DF as fillna is copy
fill_salary = nba_df2["Salary"].fillna(0)
nba_df2["Salary"] = fill_salary

# print(nba_df2)


"""
The astype Method 1
The 'astype' method converts a Series's value tp a specified type
Pass in the specified type as either a string or the core Python data type.
Pandas connot convert NaN values to numeric types, so we need to eliminate/replace them before we perform the conversion.
Pandas automatically convert an Integer in csv to Float If there is any NaN present in between them that's why we can't change the datatype without removing the NaN values.
The 'dtypes' attribute returns a Series with the DataFrame's columns and their types.
'astype' method returns a copy

"""

nba_df2 = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/nba.csv").dropna(how='all')

    # filling the NaN values.   
nba_df2["Salary"] = nba_df2["Salary"].fillna(0)

# print(nba_df2.dtypes)

    # astype returns a copy so to modify data frame we need to overwrite it which is a View and also change the DF too
dtype_salary = nba_df2["Salary"].astype("int")
nba_df2["Salary"] = dtype_salary
# print(nba_df2.dtypes)

"""
The astype Method 2
The 'category' type is ideal for columns with a limited number of unique values like Blood Type, Gender
The 'nunique' method will return a Series with the number of uniques value in a Series
With categories pandas does not create a separate value in memory for each 'cell' Rather the cells point to a single copy for each unique value.
This also helps us to reduce memory

"""

# print(nba_df2["Team"].nunique())
# print(nba_df2.nunique())
# print(nba_df2.info())
# print(nba_df2.dtypes)

    # we can see have 30 in team and 7 in postion uniques value out of 500+ result so this is a good column to convert type as 'category'
dtype_team = nba_df2["Team"].astype("category")
dtype_postion = nba_df2["Position"].astype("category")

nba_df2["Team"] = dtype_team
nba_df2["Position"] = dtype_postion

    # you can see the memory used is less when using category type 
# print(nba_df2.info())
# print(nba_df2.dtypes)

"""
Sort a DataFrame with the sort_values Method 1
1. 'sort_values' method sorts a DataFrame by the values in one or more columns.
2. first parameter (by) expects the column(s) to sort by
3. If sorting by a single column, pass a string with its name
4. If sorting multiple columns, pass a list of values with column names.
5. The parameter (ascending) customizes the sort order with bool value..
6. The parameter(na_postion) customizes, where pandas places NaN values..
7. we can also set the order of Ascending or descending by assigning a list of bool to 'ascending' parameter

NOTE
The first value in list of by parameter we sort first then second value ...for a single row.

8. 'sort_index' method will sort the dataframe by index. (ascending) parameter is true by default.
"""

nba_df = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/nba.csv")

    #  1st n 2nd n 3rd point
# print(nba_df.sort_values(by="Weight"))

    #  4th n 5th point
# print(nba_df.sort_values(by=["Weight","Salary","Height"],ascending=False))

    #  4th n 6th point
# print(nba_df.sort_values(by=["Name","Salary"],na_position="last").tail(10))

    #  4th n 5th n 6th point
# print(nba_df.sort_values(by="Salary",na_position="first",ascending=False).head(10))

    #  7th point
# print(nba_df.sort_values(by=["Team","Name"],ascending=[False,True]))

    #  8th point
# print(nba_df.sort_index(ascending=False))


"""
Rank Values with rank Method
The rank method assigns a numeric ranking to each Series value
Pandas will assign the same rank to equal values and create a 'gap of numbers' in the datasets for the ranks.
after giving the rank we can assign the ranks to a new column.
"""

# first remove the NaN
nba_df = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/nba.csv").dropna(how="all")
nba_df["Salary"] = nba_df["Salary"].fillna(0)

    # ascending false as we want the higher salary to be rank 1
rank = nba_df["Salary"].rank(ascending=False)
# print(rank)

    #  assigning to new column
nba_df["Rank"] = rank

# print(nba_df.sort_values(by="Salary",ascending=False))
