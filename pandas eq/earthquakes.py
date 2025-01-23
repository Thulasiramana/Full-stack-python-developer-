import pandas as pd
data=pd.read_csv("C:/Users/thula/OneDrive/Desktop/pandas eq/earthquakes.csv")
print(data.head(2))


# Year with the highest number of recorded earthquakes.

year_counts=data.year.value_counts()
time_occurs=year_counts.max()
max_year=year_counts.idxmax()
print(f"in the year of {max_year} the earthquakes occurs for {time_occurs} so it has highest ammount of all of this  ")

death=data["deaths"].max()
area=data[data.deaths==death]["area"].values[0]
year=data[data.deaths==death]["year"].values[0]

print(f"the deadliest earthquake in the year of {year} , and in the location of {area}, the death rate is {death}")

# Average Richter scale value of earthquakes per year.

richer=data.groupby("year")["richter"].mean()
dic={
    "year":richer.index,
    "richer":richer.values
}
dic_csv=pd.DataFrame(dic)

region=data.groupby("region")["deaths"].sum().reset_index()

#maximum region that occurs more death rates 
max_reg=region.max()
print(max_reg)
print(f"this region occurs most death :{max_reg[0]} , death rate : {max_reg[1]}")