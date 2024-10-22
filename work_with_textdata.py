import pandas as pd

city = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/chicago.csv")
# print(city)

# print(city.info())
# print(city.nunique())

city["Department"] = city["Department"].astype("category")
# print(city.info())

"""
Common String Method
1. A Series has a special "str" attributes that exposes an object with string methods.
2. Access the "str" attribute then invoke the string method on nested object..mostly same as string

they are COPY 
"""

    # Common String Methods
# print("akshat".upper())
# print("Akshat".lower())
# print("pandas python course".title())

to_lower = city["Position Title"].str.lower()
city["Position Title"] = to_lower
# print(city)

to_title = city["Position Title"].str.title()
city["Position Title"] = to_title
# print(city)

to_upper = city["Position Title"].str.upper()
city["Position Title"] = to_upper
# print(city)

    # lstrip for left and rstrip for right to remove whitespaces
to_strip = city["Position Title"].str.strip()
city["Position Title"] = to_strip
# print(city)

to_replace = city["Department"].str.replace("MGMNT","MANAGEMENT")
city["Department"] = to_replace
# print(city)

    # Chaining them
to_change = city["Position Title"].str.replace("OFFICER","COMMISSIONER").str.title()
city["Position Title"] = to_change
# print(city)


"""
Filtering with String Methods
1. The str.contains method checks whether a substring exists anywhere in the String
2. The str.startswith method checks whether a substring exists at the start of the String
3. The str.endswith method checks whether a substring exists at the end of the String

na=False "paramter" will assume false to NaN values or else use dropna(how = "all") while read_csv
"""

city = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/chicago.csv")

is_contains = city["Position Title"].str.lower().str.contains("mission", na=False)
# print(city.loc[is_contains])

is_startswith = city["Position Title"].str.lower().str.startswith("depu", na=False)
# print(city.loc[is_startswith])

is_endswith = city["Position Title"].str.lower().str.endswith("hief", na=False)
# print(city.loc[is_endswith])


"""
String Methods on Index and Columns
1. Use the index and columns attributes to access the DataFrame index/column labels
2. These objects support string methods via their own "str" attribute.

"""
city = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/chicago.csv",index_col="Name").dropna(how="all").sort_index()

    # As to access Name as index so removing white spaces first
city.index = city.index.str.strip().str.title()
city.columns = city.columns.str.upper()

# print(city)



"""
The split Method
1. The str.split methods splits a string by the occurence of a delimiter. Pandas return a Series of lists
2. Use the str.get method to access a nested list element by its index postion.

"""

city = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/chicago.csv").dropna(how="all")

split_postion  = city["Position Title"].str.split(" ")

# print(split_postion)
# print(split_postion.str.get(0))
# print(split_postion.str.get(1))

    # Find the most common first name among Employees
split_name  = city["Name"].str.title().str.split(", ").str.get(1)
split_name_2 = split_name.str.strip().str.split(" ").str.get(0)
# print(split_name_2)
# print(split_name_2.value_counts())


"""
The expand and n Parameters of split Method
1. The "expand" parameter returns a datframe instead of Series of lists. value is False by default
2. The "n" paramter limits the number of splits

"""

city = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/chicago.csv").dropna(how="all")

# print(city)

    # Series of Lists converted to DataFrame
splitted_name = city["Name"].str.split(",",expand=True)
# print(splitted_name)

    # Assigning those column to dataFrame
city[["Last Name","First Name"]] = splitted_name
# print(city)


splitted_postion_1 = city["Position Title"].str.split(" ",expand=True)
    # as we can see there are 9 column it means there may be a title consisting of 9 words present in DataFrame
# print(splitted_postion_1)

    # So to limit the number of SPlits we use n parameter
splitted_postion_2 = city["Position Title"].str.split(" ",expand=True,n=1)
    # Now there are only two columns splitted by single space in between
# print(splitted_postion_2)

    # Assigning the cols to dataframe
city[["Primary Postion","Secondary Postion"]] = splitted_postion_2
# print(city)




