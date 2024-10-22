# We installed 3 dependencies or library 
# python -m pip install pandas then bottleneck then numexpr

import pandas as pd

"""

Series :- It is a single column of data, it combines the best features of list and a dictionary
It maintains the original order as List with an identifier as Dict (BY DEFAULT)
It takes List as an input 
List = [values separated by commas of any data type]
x = [1,2,3], y = ["apple", "banana", "guava"], z = [True, False,True],a=[1,'a',True]

"""

# print(pd.Series([1,2,3,4,'a',True]))

"""
Creating Series from Dictionary (This is replace the index with the Key name)

"""
food = {
    "Carbs" : "Rice",
    "Fats" : "Nuts",
    "Protein": "Paneer"
}
# print(pd.Series(food))

"""
Using Method on Series 

"""
num = [2,3,4,5]
y = pd.Series(num)
# print("\nMean is", y.mean(),"\nSum is" , y.sum(), "\nCount is" , y.count())

"""
Using Attributes (Same as Method but without () )

"""
# print(y.size,"\n",y.is_unique,"\n",y.values,"\n",y.index)

#<= shape attribute gives row and cols
# print(y.shape) 

"""
Parameters in Series Function
==> pd.Series(data,index)

we can also put another List in place of index ,If we don't want to use dict Key as Index
Index is shown first in output but it is the second arguemnt of Series Function.

"""
fruits = ["apple","mango","banan"]
days = ["monday","tuesday","wednesday"]

# print(pd.Series(fruits,days))

"""
Import Series with pd.read_csv Function

1. Pandas ships with many different read_ function for different types of files
2. The read_csv fucntion accepts many different parameters, first one specifies the file name/path
3. read_csv function will import the dataset as a DataFrame, a 2-dim table not a Series
4. The usecols parameter accepts a list of the column(s) to import ==> pd.read_csv("",usecols["col1","col2",...])

5. The squeeze method converts a DataFrame to a Series ==> pd.read_csv("").squeeze()
(Works Only If the DataFrame has only one column imported at that time) 
(If Not then it can be done using usecols, by only including one column in list to import)
==> pd.read_csv("",usecols["colname"]).squeeze()

6. index_col to convert any column as an Index. Also, this can be used with squeeze to convert dataFrame into Series. Because of this, we can view 2 columns at once even in a Series
and perform different operations like Sort,max,min

To read a path use this "/" not "\"

"""
google_file = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/google_stock_price.csv",usecols=["Price"]).squeeze("columns")
poke_file = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/pokemon.csv",usecols=["Name"]).squeeze("columns")
poke_file_2 = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/pokemon.csv",index_col="Name").squeeze("columns")
# print(google_file)
# print(poke_file)
# print(poke_file_2)

"""
How to know it shows Series after using squeeze method
Output 
when Dataframe => it shows number of Rows and Columns at last
When Series => it shows Column Name as Name:colname, Length:, dtype:

"""

"""
head and tail Method
return the number of rows from the beginnin and end respectively
default number of rows is 5 for both 
"""
# print(poke_file.head())
# print(poke_file.head(10))
# print(poke_file.tail(10))

"""
Python's Built in Functions
len = return length of Series
type = return the object type
list = converts the Series into List
dict = convers Series in dictionary
sorted = converts Series to sorted list
max/min = return the maximum and minimum values in Series

We can use the combination of methods and functions like convert poke_file but show only first 5 => dict(poke_file.head())

"""
# print(len(poke_file), "\n", type(poke_file), "\n", list(poke_file), "\n", dict(poke_file.head()), "\n", sorted(google_file.head(10)), "\n", max(google_file))

"""
1. in keyword
    It checks the object is present or not by returning a bool value
    by default in Series 'in' keyword check in 'index' only 
    so to check in value we need to use .values attribute

2. sort_values Methods
    use to sort the Series by its values 

3. sort_index Methods
    use to sort the Series by its index
    As we know index is always sorted So,
    It is used in those cases where we can make one of the column of dataFrame as an Index then use Squeeze to convert DataFrame to Series in this way we can see two column of 
    a DataFrame.

"""

# print("Bulbasaur" in poke_file)
# print("Bulbasaur" in poke_file.values)

# print(poke_file.sort_values().head(10))
# print(poke_file.sort_values(ascending=False).head(10))

# print(poke_file_2.sort_index().head(10))
# print(poke_file_2.sort_index(ascending=False).head(10))


"""
Extract Series value by Index Postion
1. Use the iloc[] accessor to extract a Series value by its index postion.
2. iloc = index location
3. Multiple Value will return the results in a new Series. ie iloc[[13,4,25]]
4. Python Slics is also supported with Series object.
    a. use : for range => iloc[11:21]

Extract Series value by Index Label
when you have a custom label in a Series instead of index then we use 
1. loc accessor to extract a Series value by its index labl.
2. Pass a list of labels to extract multiple values
3. If one index label is not exist, Pandas raise an error.

"""

# print(poke_file.iloc[500])
# print(poke_file.iloc[[500,342,232]])
# print(poke_file.iloc[50:64])

# using poke_file_2 as it contains "Name" column in place of index
# print(poke_file_2.loc["Dragonite"])
# print(poke_file_2.loc[["Bulbasaur","Charizard","Pikachu","Snorlax","Mew"]])

"""
The get Method on Series
1. get method extracts a Series value by index label. It is an alternative option to square brackets.
2. get method's second arguement we can set the fallback value to return if the label/postion does not exist.
3. Default value of 2nd args is None 
4. It does not gives error like iloc[] and loc[]
5. Use with index label only as get with Index postion is deprecated so use iloc[] for index postion

"""
# print(poke_file_2.get("Pikachu")) # found
# print(poke_file_2.get("Digimon")) # not found with default value
# print(poke_file_2.get("Digimon","Errr Not Found Try another name")) # not found with replaced value
# print(poke_file_2.get(["Pikachu","Hitmonlee","Digimon"],"One of the name is not present"))

"""
Overwrite a Series Value
1. Use the iloc/loc to access the target index label/postion , then assign it with a new value using '='.
2. You can also assign Multiple Value at once
3. SeriesName.iloc[]/loc[] = "New Value"

"""
# creating new variables for Overwriting values, so that we can use poke_file and poke_file_2 in course further
poke_file_3 = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/pokemon.csv",usecols=["Name"]).squeeze("columns")
poke_file_4 = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/pokemon.csv",index_col="Name").squeeze("columns")

poke_file_3.iloc[1] = "Power Rangers"
poke_file_4.loc["Jigglypuff"] = "Singing"

# print(poke_file_3.iloc[1])
# print(poke_file_4.loc["Jigglypuff"])

# Overwriting Mutliple Values
poke_file_3.iloc[[2,3,4]] = ["Idaten Jump","Astroman","Beyblade"]
poke_file_4.loc[["Pikachu","Raichu","Squirtle"]] = ["Running","Dancing","Crying"]

# print(poke_file_3.iloc[[2,3,4]])
# print(poke_file_4.loc[["Pikachu","Raichu","Squirtle"]])
# print(poke_file_2.head())

"""
Copy and View 
1. A copy is duplicate/replica of an object.
    Changes to copy do not modify changes to actual object.
2. A view is different way of looking at the same data.
    Changes to view do modify the changes to actual object.
use copy method just after the object you want to create a copy of.
like u want to create a copy of series then pd.Series().copy()

"""

# Example of View
# when we Overwrite the poke_series the poke_df also modified with the new values
poke_df = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/pokemon.csv",usecols=["Name"]) #dataframe
poke_series = poke_df.squeeze("columns") # converting df to Series

# print(poke_df.head(3))

poke_series.iloc[2] = "kuch bhi" # Overwriting
# print("\n", poke_series.head(3))

# print(poke_df.head(3))

# Using Copy Method
poke_df = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/pokemon.csv",usecols=["Name"]) #dataframe
poke_series = poke_df.squeeze("columns").copy() # converting df to Series

# print(poke_df.head(3))

poke_series.iloc[2] = "kuch bhi" # Overwriting
# print("\n", poke_series.head(3))

# print(poke_df.head(3))


"""
Math Methods on Series Objects
count,sum,product,mean,std,max,min,median,mode.
describe = gives the summary of data sets having mostly all methods above

"""
# print(google_file.count(), " ", google_file.sum(), " ", google_file.product(), " ", google_file.mean(), " ", google_file.std(), " ", google_file.max(), " ", google_file.min()
#       ," ", google_file.median())
# print(google_file.mode())
# print(google_file.describe())

"""

Broadcasting :-
Applying Mathematical Operations to every value in a Series
add,sub,mul,div

# These methods does not overwrite the values in Series and due to this original DataFrame is not altered
as Broadcasting methods like .add(), .mul() returns a new series instead of Modifying the Original One.
That why we do not need to use .copy() method in google_series

"""

x = pd.Series([1,2,3,4])
# print(x.add(3))

google_df = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/google_stock_price.csv",usecols=["Price"])
google_series = google_df.squeeze("columns")

# print(google_series.head(5))
# print(google_series.add(10).head(5))
# print(google_series.sub(10).head(5))
# print(google_series.mul(3).head(5))
# print(google_series.div(2).head(5))

"""
The value_counts Method
The value_counts method returns the number of times each unique value occurs in the Series
The normalize parameter returs the relative frequencies/percentages of the values instead of counts.
"""

# print(poke_file_2.value_counts())

    # Ascending Order(default False..change to True to get values in Ascending Order)
# print(poke_file_2.value_counts(ascending=True)) 

    # Normalize Parameter (default False..change to True to get frequencies or percentage)
# print(poke_file_2.value_counts(True)) 


"""
The apply Method
The apply method accepts a function as an arguement. It invokes that function on every Series value
It takes uninvoked function as arguement..jsut the name, no matter its predefined or custom function
"""

    #pre-defined
# print(poke_file.apply(len).head(10))

    #custom function
def count_of_a(pokemon):
    return pokemon.count("a")

# print(poke_file.apply(count_of_a).head(10))

"""
The map Method
The map method 'maps' or connects each Series values to another value
We can pass the method a dictionary or a Series. Both types connects keys to values
The map method uses our arguement to connect or bridge the values together.

In other words we can say the values of Series act as Foreign Key so that we can join the index with the value of another dataset

"""
poke_powers = {
    "Grass":10,
    "Fire":15,
    "Water":15,
    "Fairy, Fighting":20,
    "Grass, Psychic":50
}

    #now, we map the value sof poke_file_2 which are pokemon types to the poke_powers dictionary to get the values.
    # the values which cannot be matched or mapped will return NaN ie Not a Number
# print(poke_file_2.map(poke_powers).head())

    # it can be any type not neessary a dictionary, using a Series below
poke_powers_list = pd.Series(poke_powers)
# print(poke_file_2.map(poke_powers).head())