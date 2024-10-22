import pandas as pd
import matplotlib.pyplot as plt

"""
The plot method

It renders a line chart which is ideal for showing trends
The plot method includes all numeric DataFrame columns by default. We can choose a subset with y parameter
Matplotlib will use the index values for the x-axis and the value for y-axis
Matplotlib will figure out reasonable intervals for the date index (days, month, years, etc). These options are customizable.

"""

ibm = pd.read_csv("C:/Users/verma/Downloads/pandas/pandas/Complete/ibm.csv",parse_dates=["Date"],index_col="Date")
print(ibm)
# ibm.plot()

# ibm.plot(y="Close")
    # OR
# ibm["Close"].plot()

"""
Modifying Plot Asthetics

The plt.style.available attribute returns a list of all available styles
Use the plt.style.use method and pass in a sample style string
The next charts/graphs you render will implement that style..

"""

# print(plt.style.available)
# plt.style.use("grayscale")
# ibm.plot(y="Close")


"""
Bar Charts

A bar chart use bars to represent occurance of values/categories
We can customize the type of plot that matplotlib renders with the kind parameter
Pass bar for a bar graph and barh for horizontal bar graph
"""
def rank_perf(stock):
    if stock <= 50:
        return "Poor"
    elif stock > 50 and stock <= 100:
        return "Satisfactory"
    else:
        return "Excellent"

value = ibm["Close"].apply(rank_perf).value_counts()
print(value)
# value.plot()
# value.plot(kind="bar")
# value.plot(kind="barh")

plt.style.use("fivethirtyeight")
# value.plot(kind="pie")
value.plot(kind="pie",legend=True)



plt.show()


