import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sqlite3 

connection = sqlite3.connect("dealership.db")

cars_df = pd.read_sql_query(
    "SELECT * FROM cars", connection)
cars_df.to_csv("cars_data.csv", index=False)
print("Cars data exported to CSV successfully")
customers_df = pd.read_sql_query(
    "SELECT * FROM customers", connection)
customers_df.to_csv("customers_data.csv", index=False)
print("Customers data exported to CSV successfully")

connection.close()
average_price = cars_df['PRICE'].mean()
w = cars_df['average_price'] = average_price
x = cars_df['PRICE']
y = cars_df['YEAR']
z = cars_df['MAKE']

plt.bar (z, x, color='blue', label='Average Price')
plt.xlabel('Car Make')  
plt.ylabel('Average Price')
plt.title('Average Price of Cars by Make')  
plt.show()
plt.scatter(x, y, c='red', label='Price vs Year')   
plt.xlabel('Price')
plt.ylabel('Year')  
plt.title('Price vs Year of Cars')
plt.legend()
plt.show()