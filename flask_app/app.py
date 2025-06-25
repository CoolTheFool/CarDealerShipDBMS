import os
from flask import Flask, render_template
import sqlite3
import matplotlib.pyplot as plt
import numpy as np  
import pandas as pd

def generate_graphs():
    try:
        output_dir = os.path.join("static", "graphs")
        os.makedirs(output_dir, exist_ok=True)

        connection = sqlite3.connect( r"C:\Users\NM041\OneDrive\Documents\GitHub\CarDealerShipDBMS\dealership.db")
        cars_df = pd.read_sql_query("SELECT * FROM cars", connection)

        # ---- GRAPH 1: Average Price by Make ----
        average_price = cars_df.groupby('MAKE')['PRICE'].mean()
        plt.figure(figsize=(10, 6))
        average_price.sort_values().plot(kind='bar', color='skyblue')
        plt.xlabel('Car Make')
        plt.ylabel('Average Price')
        plt.title('Average Price of Cars by Make')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, "avg_price_per_make.png"))
        plt.close()

        # ---- GRAPH 2: Price by Make ----
        sorted_cars = cars_df.sort_values(by='PRICE', ascending=True)
        plt.figure(figsize=(12, 6))
        plt.bar(sorted_cars['MAKE'], sorted_cars['PRICE'], color='green')
        plt.xlabel('Car Make')
        plt.ylabel('Price')
        plt.title('Price of Cars by Make')
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, "price_by_make.png"))
        plt.close()

        # ---- GRAPH 3: Price vs Year ----
        plt.figure(figsize=(10, 6))
        plt.scatter(cars_df['PRICE'], cars_df['YEAR'], c='red')
        plt.xlabel('Price')
        plt.ylabel('Year')
        plt.title('Price vs Year of Cars')
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, "price_vs_year.png"))
        plt.close()
    except Exception as e:
        print(f"An error occurred while generating graphs: {e}")    
    finally: 
        connection.close()
app = Flask(__name__)

DB_PATH = r"C:\Users\NM041\OneDrive\Documents\GitHub\CarDealerShipDBMS\dealership.db"

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # This allows us to access columns by name
    return conn
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sales')
def sales():
    
    return render_template('sales.html')

@app.route('/cars')
def cars():
    conn = get_db_connection()
    conn.row_factory = sqlite3.Row  # This allows us to access columns by name


    cars= conn.execute('SELECT * FROM CARS').fetchall()
    customers = conn.execute('SELECT * FROM CUSTOMERS').fetchall()
    conn.close()
    return render_template('cars.html', cars=cars, customers=customers)
@app.route('/contacts')
def contacts():
    return render_template('contacts.html')
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    generate_graphs()  # Generate graphs before starting the app
    app.run(debug=True)