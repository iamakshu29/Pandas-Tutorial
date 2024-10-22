"""
The Slice Function is one of the most important function used in Pandas to extract the data
from DataFrame with less code 
To Understand this we will see some examples 

Read this file after you finish series.py for better understanding :- 

"""

#  String
s = "Akshat Verma"
print(s[0:4])
# include 0th index till 4-1 index   0-A,1-k,2-s,3-h,4-a => 0 to 3rd posi => Aksh

s = "Akshat Verma"
print(s[0:12:2]) 
# 0th posi to 11th posi jumping to 2nd char.. 

s = [1,2,3,4,5]
print(s[0:3])
# oth posi to 2nd posi

# Now for Pandas to get the locations we have 2 methods
# iloc or columns and loc
# iloc takes the index positions whereas loc takes the index label

# iloc or columns in slice works same as normal slicing => start to end-1
# loc takes the actual label ie start to end included... (this is the main difference)

# Import pandas package
import pandas as pd

# Define a dictionary containing employee data
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
		'Age':[27, 24, 22, 32],
		'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
		'Qualification':['Msc', 'MA', 'MCA', 'Phd']}

# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)
print(df, "\n\n")

#  we can't use columns name in iloc so for column also we use the index or positions
print(df.iloc[0:2, 0:3], "\n\n")

# loc accepts the following labels not as indexes
print(df.loc[0:2, ['Name','Qualification','Address']],"\n\n")

# here columns are show on the postion basis like iloc => 0th pos to 2nd pos
print(df[df.columns[0:3]])