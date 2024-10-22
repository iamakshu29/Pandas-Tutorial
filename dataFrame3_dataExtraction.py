import pandas as pd

james = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/jamesbond.csv")
# print(james.head())


"""
The set_index and reset_index Methods
pandas uses inbdex/values when merging different objects together
The set_index() method sets an existing column as the index of the DataFrame
The reset_index() method sets the standard ascending numeric index of the DataFrame

drop parameter in reset_index(drop=?)
by default it is False ie it did not drop the column which was index before.
If it is True ie it drop the column which was index before.

Take the Primary key or the column having Unique value to set_index()

NOTE There is question arise that why use set_index when you can use the index_col as paramter in pd.read_csv
In summary:
1. Use index_col when reading data from a file to directly set the index.
2. Use set_index to modify the index of an existing DataFrame.
3. Also we use set_index() in that situation where we just get a dataFrame name...we are not in situation of using pd.read_csv it already done for us...

Also we can't reset the index using reset_index() after we set it using index_col as the only DataFrame we have that time is the one having already index as one of its column.
But in set_index() we first have dataFrame with index 0,1,2 then we modify it accordingly that why we can go back using reset_index() when using set_index()

It is a COPY Method 
"""

    # if we do like this then there is another dataframe setIndex will made whose index is film
    # thats why we get error while we perform reset_index() method on james because we set the index and make a new DF name setIndex but we think we did this on James df only
    # and we know its a copy functio ie it does not change the data type so we have to assign the newly set method to it
# setIndex = james.set_index("Film").head()   <-- wrong assigned to diff df name setIndex

    # use set_index() and assign it to that dataFrame which u want to use

james = james.set_index("Film") # assign as it is a COPY
# print(james)
# print(james.reset_index().head())
# print(james.reset_index(drop=True).head())


"""
Retrieve Rows by Index Position with iloc Accessor on a DataFrame
The iloc accessor retrieves one or more rows by index postion
Provide a pair of square brackets after the accessor
iloc accepts single values, List and Slices

for slice in iloc accessor...the ending index is exclusive
"""
james = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/jamesbond.csv")
# print(james.iloc[1])
# print(james.iloc[[5,10]])
# print(james.iloc[5:10]) # 5 to 9
# print(james.iloc[0:10]) # start ie from 0 to 9
# print(james.iloc[10:]) #start from 10 till end


"""
Retrieve Rows by Index Position with loc Accessor on a DataFrame
The loc accessor retrieves one or more rows by index label
Provide a pair of square brackets after the accessor

for slice in loc accessor...the ending index is inclusive

"""

    # Taking Film as index
james = james.set_index("Film")
# print(james)
# print(james.loc["Goldfinger"])
# print(james.loc["Casino Royale"])# give 2 ans as there are 2 rows with same Index film.
# print(james.loc[["Goldfinger","Thunderball"]])
# print(james.loc["Diamonds Are Forever" : "Moonraker"])


    # The below statements will give error as there are 2 Casino Royal named Film present in DataFrame..Pandas don't know which film to end with in 1st statement
    # and which one to start with in 2nd Statement. So instead of giving wrong answer it gives error.
# print(james.loc[: "Casino Royale"])
# print(james.loc["Casino Royale" : ])



"""
Second arguements to loc and iloc Accessors
The second value inside the square brackets targets the columns
The iloc requires numeric positions for rows and columns
THe loc requires labels for rows and columns
"""
print("\n")
james = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/jamesbond.csv",index_col="Film").sort_index()
# print(james.loc["Diamonds Are Forever","Director"])
# print(james.loc[["Octopussy", "GoldenEye"],"Director"])
# print(james.loc[["Octopussy", "GoldenEye"],"Director":"Budget"])
# print(james.loc["GoldenEye":"Octopussy","Director":"Budget"])
# print(james.loc["GoldenEye":"Octopussy",["Actor","Director","Budget","Bond Actor Salary"]])


# print(james)
# print(james.iloc[0,1])
# print(james.iloc[0:4,4])
# print(james.iloc[0:4,0:5])
# print(james.iloc[0:4,[4,5,2]])
# print(james.iloc[[0,2,4],[4,5,2]])
# print(james.iloc[:7,:3])


"""
Overwrite a value
Just find the location commonly using loc[] and assign the value simple
it is a VIEW



Overwriting Multiple Values
.replace() is a COPY so we need to assign it to DF to make changes permanent
"""

james_new = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/jamesbond.csv",index_col="Film").sort_index()
james_new.loc["A View to a Kill","Director"] = "Akshat Verma"
# print(james_new.head())
# print(james_new.loc["A View to a Kill","Director"])


    # Overwriting Multiple Value with .replace() method
james_new = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/jamesbond.csv",index_col="Film").sort_index()

    # This will replace Seaon Connery to Akshat Verma in every column it finds the value
james_new  = james_new.replace("Sean Connery","Akshat Verma")
# print(james_new)

    # To make changes in specific column 
james_new = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/jamesbond.csv",index_col="Film").sort_index()
    #  if wee do this the DF will converted into a Series (ie with one column of Actor only)
# james_new  = james_new["Actor"].replace("Sean Connery","Akshat Verma")

    # DO this instead of that as we traversing to particular col and then update that specific col by assigning the replaced value.
james_new['Actor'] = james_new['Actor'].replace("Sean Connery","Akshat Verma")
# print(james_new)




"""
Replace Index or Columns in a DataFrame

1. The rename() method accepts a dictionary for either its columns or index parameters
2. The dictionary "keys" represent the existing names and the values represent the new names as "values"
3. We can replace all column by overwriting the DataFrame's columns attribute.

It is a COPY

"""

james = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/jamesbond.csv",index_col="Film").sort_index()

# print(james.head())
james = james.rename(columns={"Year":"Saal","Actor":"Hero","Director":"Nirdeshak"})
james = james.rename(index={"A View to a Kill":"Dhoom","Casino Royale":"Don No. 1","Die Another Day":"Devdas"})
# print("\n" , james.head())

james = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/jamesbond.csv",index_col="Film").sort_index()

cols = {"Year":"Year of Release","Box Office":"Revenue"}
rows = {"A View to a Kill" : "Housefull","Casino Royale":"Bhool Bhoolaiya"}

james = james.rename(index=rows,columns=cols)
# print("\n" , james.head(3))


    # you can overwrite the column attribute as mentioned in pt 3. Optimally, Use this when you want to overwrite all values of column.
james.columns = ["hi","hello","why","when","where","what"]
# print("\n" , james.head(3))



"""
Delete Columns or Rows from a DataFrame.
1. The drop() method deletes one or more rows/columns from a DataFrame. it is a COPY
2. Pass the "index" or "columns" parameters, a list of the column names to remove.
3. The pop() method removes and returns a single Series ( it mutates the DataFrame in the process)... It is a VIEW
4. Python's del keyword also removes a single Series

"""
james = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/jamesbond.csv",index_col = "Film")

# print(james.head())

    # you can drop column or index by single args or List of args
james = james.drop(index=["Goldfinger","Thunderball"],columns="Year")

# print("\n" , james.head())

    # .pop() return the series and delete it from the DataFrame, its a VIEW
# print("\n" , james.pop("Actor").head())
# print("\n" , james.head())


    # del keyword
del james["Bond Actor Salary"]
# print("\n" , james.head())



"""
Create Random Sample with sample() Method
Customize the axis to extract random columns

"""
james = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/jamesbond.csv",index_col = "Film").sort_index()
# print(james.sample())
# print(james.sample(n=4))
    # by default axis = "rows"
# print(james.sample(axis="columns",n=2))


"""
The nsmallest and nlargest Methods
The nlargest / nsmallest() method returns a specified number of rows with the largest / smallest values from a given column.
These methods are more effcicient than sorting the entire DataFrame.

Only work on Numberic Columns like salary , number etc..not on Names, Company 

"""
    # for dataframe
# print(james.nlargest(n=4,columns=["Budget","Box Office"]), "\n" ,  james.nsmallest(n=4,columns="Budget"))

    # for Series or a Single Column
# print(james["Box Office"].nlargest(4), "\n\n" ,  james["Box Office"].nsmallest(4))


"""
Filtering with the where Method
1. Similar to square brackets or "loc" the where() method filters the original DataFrame with a Boolean Series
2. Pandas will populate rows that do "not" match the critera with "NaN" values
3. Leaving in the "NaN" values can be advantageous for certain merge and visualization operations.

"""

james = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/jamesbond.csv",index_col = "Film").sort_index()

    # returns Boolean
find_Sean = james["Actor"] == "Sean Connery" 

    # 1st method
# print(james[find_Sean])
    # 2nd method
# print(james.loc[find_Sean])
    # 3rd method it shows the rows in which value matches else it do NaN
# print(james.where(find_Sean))



"""
The apply Method with DataFrames
The apply() method invokes a function on every column or every row in the DataFrame
Pass the uninvoked function as the first to the apply() method
Pass the "axis" paramter, an argument of "columns" to invoke the function on every row
Pandas will pass in the row's values as a "Series" object. We can use accessors like "loc" and ""iloc" to extract the column's values for that row.

"""

james = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/jamesbond.csv",index_col = "Film").sort_index()

# find_len = james["Actor"].apply(len)
# print(find_len)


"""
Lets make a Movie Ranking System
    80s movie -> "Greate 80s Flick"
    Pierce Borsan -> "The best bond ever"
    Budget > 100 -> "Expensive movie, fun"
    Others -> "No comment"

"""
def movie(row):
    year = row.loc["Year"]
    actor = row.loc["Actor"]
    budget = row.loc["Budget"]

    if year >= 1970 and year < 1989:
        return "Designation"
    
    if actor == "Pierce Brosnan":
        return "The best Bond ever!"
    
    if budget > 100:
        return "Expensive movie, fun"
    
    return "No Comment"
    
# print(james.apply(movie,axis="columns"))