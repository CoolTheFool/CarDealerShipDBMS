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
average_price = cars_df.groupby('MAKE')['PRICE'].mean()
cars_df['average_price'] = average_price
x = cars_df['PRICE']
y = cars_df['YEAR']
z = cars_df['MAKE']


plt.figure(figsize=(10, 6))
average_price.sort_values().plot(kind='bar', color='skyblue', label='Average Price per Make')
plt.xlabel('Car Make')  
plt.ylabel('Average Price')
plt.title('Average Price of Cars by Make')  
plt.tight_layout()
plt.xticks(rotation=45)
plt.show()

sorted_cars  = cars_df.sort_values(by='PRICE', ascending=True)
plt.figure(figsize=(12, 6))
plt.bar (sorted_cars['MAKE'], sorted_cars['PRICE'], color='green', label='Price by Make')
plt.xlabel('Car Make')  
plt.ylabel('Price')
plt.title('Price of Cars by Make')
plt.tight_layout()
plt.xticks(rotation=90)
plt.legend()
plt.show()


plt.figure(figsize=(10, 6))
plt.scatter(x, y, c='red', label='Price vs Year')   
plt.xlabel('Price')
plt.ylabel('Year')  
plt.title('Price vs Year of Cars')
plt.legend()
plt.tight_layout()  
plt.grid(True)
plt.show()