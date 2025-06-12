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
    ('Renault', 'LE14 NON', 'Clio', 2014, 4499),
    ('Renault', 'MA16 DFX', 'Megane', 2016, 5999),
    ('Renault', 'ND18 TFJ', 'Captur', 2018, 8999),
    ('Toyota', 'GL16 ZKA', 'Corolla', 2016, 8999),
    ('Toyota', 'BX67 XJW', 'Yaris', 2017, 7999),
    ('Toyota', 'CV68 MJT', 'Camry', 2018, 10999),
    ('Ford', 'BX18 KYL', 'Focus', 2018, 10999),
    ('Ford', 'SR69 DTJ', 'Fiesta', 2019, 9999),
    ('Ford', 'GL20 YPB', 'Mondeo', 2020, 12999),
    ('Honda', 'LE15 NQC', 'Civic', 2015, 7999),
    ('Honda', 'LN66 POX', 'Jazz', 2016, 6999),
    ('Honda', 'DY67 ANK', 'Accord', 2017, 11999),
    ('BMW', 'SR17 ZVE', '320i', 2017, 15999),
    ('BMW', 'CV68 TWB', 'X1', 2018, 18999),
    ('BMW', 'MA69 AZT', 'X3', 2019, 24999),
    ('Mercedes', 'ND19 FTU', 'A-Class', 2019, 19999),
    ('Mercedes', 'BX70 RSD', 'C-Class', 2020, 25999),
    ('Mercedes', 'LE71 GMI', 'E-Class', 2021, 29999),
    ('Nissan', 'LN14 KVF', 'Altima', 2014, 6999),
    ('Nissan', 'GL65 JEK', 'Juke', 2015, 7499),
    ('Nissan', 'SR66 UZN', 'Qashqai', 2016, 8999),
    ('Chevrolet', 'MA66 PQN', 'Malibu', 2016, 8499),
    ('Chevrolet', 'PO67 IQF', 'Spark', 2017, 6499),
    ('Chevrolet', 'DY68 EKB', 'Cruze', 2018, 7999),
    ('Hyundai', 'ND68 RFX', 'Elantra', 2018, 9999),
    ('Hyundai', 'CV69 HTA', 'i10', 2019, 7999),
    ('Hyundai', 'LE70 QIC', 'Tucson', 2020, 13999),
    ('Kia', 'BX67 UFD', 'Sportage', 2017, 7499),
    ('Kia', 'LN68 JAW', 'Rio', 2018, 6999),
    ('Kia', 'PO69 TKL', 'Ceed', 2019, 8999),
    ('Volkswagen', 'DY15 ANX', 'Golf', 2015, 8999),
    ('Volkswagen', 'ND16 UXN', 'Polo', 2016, 7999),
    ('Volkswagen', 'SR67 LOH', 'Passat', 2017, 10999),
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
    ('Alice Johnson', 'alice.johnson@email.com', '07421 765298', 'LE14 NON'),
    ('Ben Carter', 'ben.carter@email.com', '07311 123456', 'MA16 DFX'),
    ('Clara Evans', 'clara.evans@email.com', '07555 654321', 'ND18 TFJ'),
    ('David Smith', 'david.smith@email.com', '07388 654812', 'GL16 ZKA'),
    ('Ella Brown', 'ella.brown@email.com', '07900 111222', 'BX67 XJW'),
    ('Frank Green', 'frank.green@email.com', '07888 333444', 'CV68 MJT'),
    ('Grace Lee', 'grace.lee@email.com', '07912 618290', 'BX18 KYL'),
    ('Henry Adams', 'henry.adams@email.com', '07777 555666', 'SR69 DTJ'),
    ('Ivy Turner', 'ivy.turner@email.com', '07666 777888', 'GL20 YPB'),
    ('Jack White', 'jack.white@email.com', '07123 482910', 'LE15 NQC'),
    ('Kara Black', 'kara.black@email.com', '07812 345678', 'LN66 POX'),
    ('Liam Scott', 'liam.scott@email.com', '07712 876543', 'DY67 ANK'),
    ('Mia King', 'mia.king@email.com', '07912 784389', 'SR17 ZVE'),
    ('Noah Hall', 'noah.hall@email.com', '07463 789123', 'CV68 TWB'),
    ('Olivia Young', 'olivia.young@email.com', '07654 459329', 'MA69 AZT'),
    ('Paul Walker', 'paul.walker@email.com', '07538 901001', 'ND19 FTU'),
    ('Quinn Reed', 'quinn.reed@email.com', '07632 333922', 'BX70 RSD'),
    ('Ruby Fox', 'ruby.fox@email.com', '07485 992210', 'LE71 GMI'),
    ('Sam Wood', 'sam.wood@email.com', '07480 763354', 'LN14 KVF'),
    ('Tina Stone', 'tina.stone@email.com', '07645 340090', 'GL65 JEK'),
    ('Uma Patel', 'uma.patel@email.com', '07333 222111', 'SR66 UZN'),
    ('Victor Lane', 'victor.lane@email.com', '07222 333444', 'MA66 PQN'),
    ('Wendy Moss', 'wendy.moss@email.com', '07111 444555', 'PO67 IQF'),
    ('Xander Cole', 'xander.cole@email.com', '07000 555666', 'DY68 EKB'),
    ('Yara Grant', 'yara.grant@email.com', '07999 888777', 'ND68 RFX'),
    ('Zane Price', 'zane.price@email.com', '07898 777666', 'CV69 HTA'),
    ('Amy Bell', 'amy.bell@email.com', '07777 666555', 'LE70 QIC'),
    ('Brian Nash', 'brian.nash@email.com', '07676 555444', 'BX67 UFD'),
    ('Cathy Lowe', 'cathy.lowe@email.com', '07575 444333', 'LN68 JAW'),
    ('Derek Shaw', 'derek.shaw@email.com', '07474 333222', 'PO69 TKL'),
    ('Eva Hunt', 'eva.hunt@email.com', '07373 222111', 'DY15 ANX'),
    ('Finn Rose', 'finn.rose@email.com', '07272 111000', 'ND16 UXN'),
    ('Gina Pope', 'gina.pope@email.com', '07171 000999', 'SR67 LOH'),
]
print("Inserting data into CUSTOMERS table...")
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