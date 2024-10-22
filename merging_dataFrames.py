import pandas as pd

foods = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/restaurant_foods.csv").dropna(how="all")
customers = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/restaurant_customers.csv").dropna(how="all")
week1 = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/restaurant_week_1_sales.csv").dropna(how="all")
week2 = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/restaurant_week_2_sales.csv").dropna(how="all")
# print(foods)
# print(customers)
# print(week1)
# print(week2)


"""
The pd.concat Function I

The concat function concatenates one DF to end of the another
The original index labels will be kept by default. Set ignore_index = True to generate a new Index.
The keys parameter creates a MultiIndex using the specified keys/labels..

"""
concat1 = pd.concat([week1,week2])
    # The length of week1 and week2 is 250 so concat result will be 500 but when executed you can see the index ending at 249 only
    # It is because the week2 DF starts with index 1, just after the week1 DF ends at 249 index ie concat does not continue the index it just put 2 DF together with the index not merged
# print(concat1)


concat1 = pd.concat([week1,week2],ignore_index=True)
    # generating 1 common index  0 to 499
# print(concat1)


concat1 = pd.concat([week1,week2],keys=["week 1","week 2"]).sort_index()
    # even if we sort the index we can easily specified which ID is from week 1 or week 2 with help of keys parameter
# print(concat1)




"""
The pd.concat Function II

Pandas will include all cols that exist in DF..If there are no matching values it returns NaN values
we can pass the "axis" parameter an arguement of "columns" to concatenate on the column axis.

while using this both column name show differently unlike in the DF having same columnn name to merge on the column name coincide on each other.
NOTE we can further remove 1 column for our convenience...

NOTE :
we know the concat function adds the second DF at the end of it...but we can decide at which end it add the another DF
ie
1. if we want to concat the data after the end of index or we can say below then put axis = "index" which is default behaviour
2. if we want to concat the data after the end of columns or we can say to the right of DF then put axis = "columns"
3. This axis is mostly or should be used in that tupe of DF where the name of columns doesn't match or same.
"""

concat1 = pd.concat([foods,customers],axis="index") # default behaviour
# print(concat1)

concat1 = pd.concat([foods,customers],axis="columns")
# print(concat1)



"""
Joins

Left Joins
take the left table as a base or foundation on which the new table is formed 
by taking the common value present in both table and giving the value from right table merge with the left table 
as per the common values
 if the common value is not present it return NaN

df1.merge = foundation of new table formed after merge
(df2,how,on) = the table which is going to merge with df1 as per the common values
how = type of join
on = common values

"""

# print(week1.merge(foods,how="left",on="Food ID"))


"""
The left_on and right_on parameters
they are the parameters of designated column names from Each to DF to use in the merger

NOTE :- 
it is simply used when we want to merge two DF based on the same type of column but they don't have same column name
1. we can simply rename the column of 1 DF matches with the 2nd DF to merge it using "on" parameter.
2. we use the two column name on which merge is based by using left_on and right_on parameter.
"""

# print(week2.merge(customers,how="left",left_on="Customer ID",right_on="ID").drop("ID",axis="columns"))



"""
Inner join
merge two DF together based on values which is only found in both tables..

below results show the food id of those customers who came to eat in both weeks
"""

# print(week1.merge(week2,how="inner",on="Customer ID"))

# print(week1.merge(week2,how="inner",on="Customer ID",suffixes=[" - week1"," - week2"]))



"""
Inner join II
We can pass multiple args to the "on" parameter of the "merge" method. Pandas will require matches in both columns across the DataFrames..

below table shows the result of those customers who eat same food in both weeks
"""

# print(week1.merge(week2,how="inner",on=["Customer ID","Food ID"]))


"""
Full/Outer Join
A full/outer joins values that are found in either DataFrame or both DataFrames
Pandas does not mind if a value exists in one DF but not the other.
If a value does not exist in either one DF, it will have a NaN
use "indicator" parameter = True to tell if the value found in both or either 1 of DFs

below table shows the result of those ustomer who came both in 1 one or 2nd or both
"""
merged = week1.merge(week2, how="outer", on="Customer ID",suffixes=[" - week1"," - week2"],indicator=True)
print(merged)
print(merged["_merge"].value_counts())