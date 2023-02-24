import pandas as pd
import matplotlib.pyplot as plt
import datetime

oil = pd.read_csv("crudeoil.csv")
fx = pd.read_csv("usdbrl.csv")

plt.figure(figsize=(10,10))
plt.scatter(oil["Price"], fx["Price"], color="red")
plt.title("USD BRL exchange rate over crude oil future price index (2000 - 2023)",size=12)
plt.ylabel("USD BRL",size = 12)
plt.xlabel("crude oil futures", size =12)
plt.savefig("usdbrl_oilprice_scatter.png")

plt.figure(figsize=(10,10))
plt.plot(oil["Date"], oil["Price"]/oil["Price"][0], color="black", label = "oilprice")
plt.plot(fx["Date"], fx["Price"]/fx["Price"][0], color="green", label = "exchangerate")
plt.title("Exchange rate USDBRL index and crude oil futures index over time (2000 - 2023)",size=12)
plt.xlabel("Time (Jan 2000 to Feb 2023)", size =12)
plt.ylabel("Index value", size = 12)
plt.legend()
plt.savefig("usdbrl_oil_timeseries.png")