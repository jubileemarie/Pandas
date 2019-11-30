import pandas as pd
cars=pd.read_csv('cars.csv')
A=cars.iloc[0:5,0::2]
print(A)
B=cars.loc[cars['Model']=='Mazda RX4']
print(B)
C=cars.loc[cars['Model']=='Camaro Z28',['Model','cyl']]
print(C)
D=cars.loc[cars['Model'].isin(['Mazda RX4 Wag','Ford Pantera L','Honda Civic']),['Model','cyl','gear']]
print(D)