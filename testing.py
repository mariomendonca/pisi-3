import pandas as pd
import matplotlib.pyplot as mp
 
# data to be plotted
data = [["New York", 8.6, 20],
        ["Chicago", 2.7, 20],
        ["Los Angeles", 3.9, 20],
        ["Philadelphia", 1.5, 20],
        ["Houston", 2.1, 20]]
 
# form dataframe from data
df = pd.DataFrame(data, columns=["City", "Population(million)", "Year(2020)"])
 
# plot multiple columns such as population and year from dataframe
df.plot(x="City", y=["Population(million)", "Year(2020)"],
        kind="line", figsize=(10, 10))
 
# display plot
mp.show()