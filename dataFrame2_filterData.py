import pandas as pd

"""
DataFrame 2 : Filtering Data


==> This Module's dataset + Memory Optimization
1. 'pd.to_datetime' method converts a Series to hold datetime values.
2. The 'format' parameter informs the pandas of the format that the times are stored in
3. We pass symbols designating the segments of the string. For example %m means "month", %Y means "Year" and %d means "day"
4. The 'dt' attribute reveals an object with many datetime related attributes and methods.
5. The 'dt.time' attribute extracts only the time from each value in a datetime Series.
6. The 'astype' method to convert the value in a Series to another type
7. The 'parse_dates' and 'date_format' parameters of read_csv is an alternative way to parse strings as datetimes
"""

employees = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/employees.csv")
# print(employees)

date = pd.to_datetime(employees["Start Date"],format="%m/%d/%Y")
# print(date)

    # Updating the Date Column as Pandas takes csv date as String, so first we need to convert it to date_time object and then assigned it to that columns
employees["Start Date"] = date

# print(employees)

    # when converting String to time pd.date_time show pre-defined date along with time...thats why we use dt.time to extract only time
date_time = pd.to_datetime(employees["Last Login Time"],format="%H:%M %p")
# print(date_time)

    # dt attribute gives an object related with datetime 
# print(date_time.dt)

    # dt.time extracts only time 
time = date_time.dt.time
# print(time)

   # Modifying the Time Column as Pandas takes csv time as String
employees["Last Login Time"] = time

# print(employees)

    # Just converting Senior Management to bool Type as Pandas also take Bool as a String and bool is optimized than String
# print(employees["Senior Management"].astype("bool").dtype)
employees["Senior Management"] = employees["Senior Management"].astype("bool")

    # Converting Gender to Category type to optimize memory as we have small unique values.
employees["Gender"] = employees["Gender"].astype("category")

    # Remember why we need to assigning these values to the column after changes to their datatypes ??
    # Ans :- As they made a copy not view and to make the changes permanent we need to overwrite the columns as Overriding is a View Type

# print(employees.info())

# print(employees)

    # Second Method to parse String as datetimes
employees_dateConvert = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/employees.csv",parse_dates=["Start Date"], date_format="%m/%d/%Y")
# print(employees_dateConvert.info())
# print(employees_dateConvert)



"""
Filter a DateFrame Based on A condition
1. Pandas needs a Series of Booleans to perform a Filter
2. Pass the Boolean Series inside Square brackets after the DataFrame
3. We can generate a Boolean Series using a wide variety of operations (equality, inequality, less than, greater than, inclusion etc..)

Just read the steps, they are enough to understand once you see an example :-

continue from the changes we do above from Memory Optimization

"""

    # Filter the number of Male in Gender Column for employees DataFrame
# print(employees[employees["Gender"] == "Male"])

    # Filter the number of Finacne in Team Column for employees DataFrame
check_finance = employees["Team"] == "Finance"
filtered_finance = employees[check_finance]
# print(filtered_finance)

    # Filtering If the person is in Senior Management or not
    # as we already converted the Senior Mngmt column to bool ie it already a bool series so we just need to assign in []
# print(employees[employees["Senior Management"]])


    # Filter employees having salary greater then 100000
# print(employees[employees["Salary"] > 100000])

    # Filter name which works before jan 1 1985
# print(employees[employees["Start Date"] < "1985-01-01"])

    # Filter with time before 12 PM (NOON)
    #  THis time we can't compare a time dtype column with String representation of Time like we did with Date so for that we are going to import datetime inbuilt library.
import datetime as dt
time = dt.time(12,0,0)
# print(employees[employees["Last Login Time"] < time])


"""
Filter with more than one condition with AND (&) & OR (|) operators
NOTE
use parameters () in multiple queries
"""
    # Salary between 60000 and 100000
# print(employees[(employees["Salary"] < 100000) & (employees["Salary"] > 60000)])

    # Find females in Marketing team
is_female = employees["Gender"]=="Female"
is_team = employees["Team"]=="Marketing"
# print(employees[is_female & is_team])

    # employee either in Senior Management or started before Jan 1, 1990
before_date = employees["Start Date"] < "1990-01-01"
in_mngmnt = employees["Senior Management"]
result = employees[before_date | in_mngmnt]
# print(result)

    # frist name Robert with team as client service or start date is later than 2016-06-01
first_name = employees["First Name"] == "Robert"
is_clientServices = employees["Team"] == "Client Services"
start_date = employees["Start Date"] > "2016-06-01"
result = employees[(first_name & is_clientServices) | start_date]
# print(result)

"""
isin method
it is similar like we use in SQL to counter so many OR statements   

"""

    # employess either in legal or sales or product team
# print(employees[employees["Team"].isin(["Legal","Sales","Product"])])


"""
The isnull Method and notnull Method
1. isnull return true for NaN values in Series
2. notnull return true for present values in Series

can also combine both method using & , | operators
"""

    # return all the rows having NaN in Team column
# print(employees[employees["Team"].isnull()])

    # return all the rows having values in Team column
# print(employees[employees["Team"].notnull()])


"""
The between Method
It return true if a Series values is found within its range.
Similar to like of between we use in SQL to counter so many < and > statement

the values in between method are inclusive ie they represent <= or >= not < or >
"""
    #  Salary between 60k to 100k
result = employees[employees["Salary"].between(60000,100000)]
# print(result)

    #  login time between moring 8.30 to 12 noon
result = employees[employees["Last Login Time"].between(dt.time(8,30),dt.time(12,0))]
# print(result)

"""
The duplicated Method
1. The duplicated Method return "True" if a Series value is duplicate.\
2. First Parameter of duplciated method "subset" takes the column or list of column as arguement when we apply on some column while still seeing the dataFrame
3. Pandas will mark "first" occurance of a repeated value as non duplicate by default.
    3.1 We can change this default method by using the 'keep' parameter as "first" or "last" to assign which value should be considered as the "non-duplicate value" first one or last one
4. Pass False to the 'keep' parameter to mark all occurences of repeated values as duplicates
5. use the tilde symbol (~) to invert a Series's values so, that True will become False and vice versa
"""

    # There are 2 syntax for the duplicated method
    #  1st Method is to only show the Series :- we select a particular column then apply the duplicated method on that column individually

# employees["Gender"].duplicated(keep="first")
# employees["Gender"].duplicated(keep="last")
# employees["Gender"].duplicated(keep=False)
# ~employees["Gender"].duplicated(keep=False)


    # 2nd we donot pick the column out but we still apply the duplicated method on a column and still see the whole DataFrame

# print(employees.duplicated(["Gender"])) 
   # default value of keep parameter in duplicated method is first
# print(employees.duplicated(["Gender"],keep='first')) 

    # result will give the duplicated value only ie which are True (false is only first occurance of male and female)
result = employees[employees.duplicated(["Gender"],keep='first')]
# print(result)



# print(employees.duplicated(["Gender"],keep='last'))

    # result will give the duplicated value only ie which are True (false is only last occurance of male and female)
result = employees[employees.duplicated(["Gender"],keep='last')]
# print(result)



# print(employees.duplicated(["Gender"],keep=False))

    # result will give the duplicated value only ie which are True (as keep = False so no value is False)
result = employees[employees.duplicated(["Gender"],keep=False)]
# print(result)



# print(~employees.duplicated(["Gender"],keep=False))

    # result will give the unique value only as we use Tilde ~ function which will reverse the actions
result = employees[~employees.duplicated(["Gender"],keep=False)]
# print(result)
# result above give Empty DataFrame as there is no unique value in Gender they are either Male or Female


#  Taking another example to show negation of False using First Name column ...
    # result will give the unique value only as we use Tilde ~ function which will reverse the actions
result = employees[~employees.duplicated(["First Name"],keep=False)]
# print(result)


    # 3rd Method we can also use duplicated method by taking multiple columns in a List
# print(employees.duplicated(["Gender","Team"]))



"""
The drop_duplicates Method
1. The "drop_duplicates" method deletes rows with duplicate values
2. By default, it will remove a row if all of its values of each column are shared with another row of values of each column
3. The "subset" parameter configure the columns to look for duplicate values within
4. Pass a list to "subset" parameter to look for duplicates across multiple column
"""

    #  same as above it is also can be used for single column as Series or just with complete DataFrame
drop_duplicate = employees["Gender"].drop_duplicates()
# print(drop_duplicate)

# print(employees.drop_duplicates(["Gender","Team"],keep="last"))

    # point 2 ...It will check the every row If matches with another row..then delete it
    # as there are not any 2 complete duplicate rows present that's why the result return the complete DataFrame as non of the rows are dropped
# print(employees.drop_duplicates())



"""
The unique and nunique Methods
The "unique" method on a Series returns a collection of its unique values. The method does not exist on a "DataFrame"
The "nunique" method returns a count of the number of unique values in the Series/DataFrame
The "dropna" parameter configures whether to include or exclude missing (NaN) values.
dropna = True ie drop or exclude NaN values
dropna = False ie include NaN values
"""
    # only works on Series
print(employees["Team"].unique())

    # Works on Both
    # Series
print(employees["Team"].nunique())

    # DataFrame
print(employees.nunique())
print(employees.nunique(dropna=False))



