import pandas as pd
cars=pd.read_csv('cars.csv')
firstfive=cars.head()
Lastfive=cars.tail()
print(cars)
print(firstfive)
print(Lastfive)