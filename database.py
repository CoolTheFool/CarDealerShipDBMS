import sqlite3 as sqlite

connection_object = sqlite.connect("dealership.db")

cursor_object = connection_object.cursor()

table1 = """
CREATE TABLE IF NOT EXISTS CARS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    MAKE TEXT NOT NULL,
    REGISTRATION TEXT NOT NULL UNIQUE,
    MODEL TEXT NOT NULL,
    YEAR INTEGER NOT NULL,
    PRICE REAL NOT NULL
);
"""

cursor_object.execute("PRAGMA foreign_keys = ON")
cursor_object.execute(table1)  
print("Table created successfully")

cursor_object.execute("PRAGMA foreign_keys = ON")
cars = [
    ('Renault', 'RX53 YMJ', 'Clio', 2014, 4499),
    ('Renault', 'RX54 YMK', 'Megane', 2016, 5999),
    ('Renault', 'RX55 YML', 'Captur', 2018, 8999),
    ('Toyota', 'AB16 CDE', 'Corolla', 2016, 8999),
    ('Toyota', 'AB17 CDF', 'Yaris', 2017, 7999),
    ('Toyota', 'AB18 CDG', 'Camry', 2018, 10999),
    ('Ford', 'FG18 HIJ', 'Focus', 2018, 10999),
    ('Ford', 'FG19 HIK', 'Fiesta', 2019, 9999),
    ('Ford', 'FG20 HIL', 'Mondeo', 2020, 12999),
    ('Honda', 'KL15 MNO', 'Civic', 2015, 7999),
    ('Honda', 'KL16 MNP', 'Jazz', 2016, 6999),
    ('Honda', 'KL17 MNQ', 'Accord', 2017, 11999),
    ('BMW', 'PQ56 RST', '320i', 2017, 15999),
    ('BMW', 'PQ57 RSU', 'X1', 2018, 18999),
    ('BMW', 'PQ58 RSV', 'X3', 2019, 24999),
    ('Mercedes', 'UV70 WXY', 'A-Class', 2019, 19999),
    ('Mercedes', 'UV71 WXZ', 'C-Class', 2020, 25999),
    ('Mercedes', 'UV72 WXA', 'E-Class', 2021, 29999),
    ('Nissan', 'ZA14 BCD', 'Altima', 2014, 6999),
    ('Nissan', 'ZA15 BCE', 'Juke', 2015, 7499),
    ('Nissan', 'ZA16 BCF', 'Qashqai', 2016, 8999),
    ('Chevrolet', 'CV16 DEF', 'Malibu', 2016, 8499),
    ('Chevrolet', 'CV17 DEG', 'Spark', 2017, 6499),
    ('Chevrolet', 'CV18 DEH', 'Cruze', 2018, 7999),
    ('Hyundai', 'HY18 JKL', 'Elantra', 2018, 9999),
    ('Hyundai', 'HY19 JKM', 'i10', 2019, 7999),
    ('Hyundai', 'HY20 JKN', 'Tucson', 2020, 13999),
    ('Kia', 'KX17 MNO', 'Sportage', 2017, 7499),
    ('Kia', 'KX18 MNP', 'Rio', 2018, 6999),
    ('Kia', 'KX19 MNQ', 'Ceed', 2019, 8999),
    ('Volkswagen', 'FJ15 XYZ', 'Golf', 2015, 8999),
    ('Volkswagen', 'FJ16 XYY', 'Polo', 2016, 7999),
    ('Volkswagen', 'FJ17 XYX', 'Passat', 2017, 10999),
]

for car in cars:
    cursor_object.execute(
        "INSERT INTO CARS (MAKE, REGISTRATION, MODEL, YEAR, PRICE) VALUES (?, ?, ?, ?, ?)", car)
connection_object.commit()
print("Data Inserted successfully")


cursor_object.execute("""
    DELETE FROM CARS 
    WHERE ID NOT IN (
                    SELECT MIN(ID)
                    FROM CARS
                    GROUP BY MAKE, REGISTRATION, MODEL, YEAR, PRICE)
                    
                      
                      """)
connection_object.commit()
print("Duplicate entries removed successfully")
data = cursor_object.execute("SELECT * FROM CARS").fetchall()

for row in data:
    print(row)
   
table2 = """
CREATE TABLE IF NOT EXISTS CUSTOMERS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME TEXT NOT NULL,
    EMAIL TEXT NOT NULL,
    PHONE TEXT NOT NULL,
    REGISTRATION TEXT NOT NULL,
    FOREIGN KEY (REGISTRATION) REFERENCES CARS(REGISTRATION) 
);
"""
print("Creating CUSTOMERS table...")
cursor_object.execute(table2)

customers = [
    ('Alice Johnson', 'alice.johnson@email.com', '07421 765298', 'RX53 YMJ'),
    ('Ben Carter', 'ben.carter@email.com', '07311 123456', 'RX54 YMK'),
    ('Clara Evans', 'clara.evans@email.com', '07555 654321', 'RX55 YML'),
    ('David Smith', 'david.smith@email.com', '07388 654812', 'AB16 CDE'),
    ('Ella Brown', 'ella.brown@email.com', '07900 111222', 'AB17 CDF'),
    ('Frank Green', 'frank.green@email.com', '07888 333444', 'AB18 CDG'),
    ('Grace Lee', 'grace.lee@email.com', '07912 618290', 'FG18 HIJ'),
    ('Henry Adams', 'henry.adams@email.com', '07777 555666', 'FG19 HIK'),
    ('Ivy Turner', 'ivy.turner@email.com', '07666 777888', 'FG20 HIL'),
    ('Jack White', 'jack.white@email.com', '07123 482910', 'KL15 MNO'),
    ('Kara Black', 'kara.black@email.com', '07812 345678', 'KL16 MNP'),
    ('Liam Scott', 'liam.scott@email.com', '07712 876543', 'KL17 MNQ'),
    ('Mia King', 'mia.king@email.com', '07912 784389', 'PQ56 RST'),
    ('Noah Hall', 'noah.hall@email.com', '07463 789123', 'PQ57 RSU'),
    ('Olivia Young', 'olivia.young@email.com', '07654 459329', 'PQ58 RSV'),
    ('Paul Walker', 'paul.walker@email.com', '07538 901001', 'UV70 WXY'),
    ('Quinn Reed', 'quinn.reed@email.com', '07632 333922', 'UV71 WXZ'),
    ('Ruby Fox', 'ruby.fox@email.com', '07485 992210', 'UV72 WXA'),
    ('Sam Wood', 'sam.wood@email.com', '07480 763354', 'ZA14 BCD'),
    ('Tina Stone', 'tina.stone@email.com', '07645 340090', 'ZA15 BCE'),
    ('Uma Patel', 'uma.patel@email.com', '07333 222111', 'ZA16 BCF'),
    ('Victor Lane', 'victor.lane@email.com', '07222 333444', 'CV16 DEF'),
    ('Wendy Moss', 'wendy.moss@email.com', '07111 444555', 'CV17 DEG'),
    ('Xander Cole', 'xander.cole@email.com', '07000 555666', 'CV18 DEH'),
    ('Yara Grant', 'yara.grant@email.com', '07999 888777', 'HY18 JKL'),
    ('Zane Price', 'zane.price@email.com', '07898 777666', 'HY19 JKM'),
    ('Amy Bell', 'amy.bell@email.com', '07777 666555', 'HY20 JKN'),
    ('Brian Nash', 'brian.nash@email.com', '07676 555444', 'KX17 MNO'),
    ('Cathy Lowe', 'cathy.lowe@email.com', '07575 444333', 'KX18 MNP'),
    ('Derek Shaw', 'derek.shaw@email.com', '07474 333222', 'KX19 MNQ'),
    ('Eva Hunt', 'eva.hunt@email.com', '07373 222111', 'FJ15 XYZ'),
    ('Finn Rose', 'finn.rose@email.com', '07272 111000', 'FJ16 XYY'),
    ('Gina Pope', 'gina.pope@email.com', '07171 000999', 'FJ17 XYX'),
]

for cust in customers:
    cursor_object.execute(
        "INSERT INTO CUSTOMERS (NAME, EMAIL, PHONE, REGISTRATION) VALUES (?, ?, ?, ?)", cust)

connection_object.commit()
print("CUSTOMERS table created and data inserted successfully.")

connection_object.commit()
print("Bulk cars and customers inserted successfully.")

cursor_object.execute("PRAGMA foreign_keys = ON") 

cursor_object.execute("""
    DELETE FROM CUSTOMERS 
    WHERE ID NOT IN (
                    SELECT MIN(ID)
                    FROM CUSTOMERS
                    GROUP BY NAME, EMAIL, PHONE, REGISTRATION)
                      """)


connection_object.commit()
print("Duplicate entries in CUSTOMERS table removed successfully")  
data_customers = cursor_object.execute("SELECT * FROM CUSTOMERS").fetchall()
for row in data_customers:
    print(row)

def close_connection():
    """Close the database connection."""
    if connection_object:
        connection_object.close()
        print("Database connection closed.")
    else:
        print("No database connection to close.")