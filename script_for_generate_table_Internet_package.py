from decimal import Decimal
import sqlite3
import random
import script_for_generate_table_package as package;
conn = sqlite3.connect('client_package.db')
data_packages = [];

def generate_random_internetSpeed():
    internetSpeed = round(random.uniform(10,200),2)
    return internetSpeed

def get_all_packages():
    try:
        cursor = conn.cursor();
        cursor.execute("SELECT * FROM Pakcages")
        data_packages = cursor.fetchall();
        
        for p in data_packages:
            print(p);
    finally:
        cursor.close()
        conn.close()

def get_package_id(cursor, package_id):
    cursor = conn.cursor();
    cursor.execute("SELECT ID FROM Package WHERE ID = ?",(package_id,));
    result = cursor.fetchone();
    
    return result[0] if result else None;

def get_lastIndex(cursor):
    cursor = conn.cursor();
    cursor.execute("SELECT count(ID) FROM Internet_Package");
    result = cursor.fetchone();
    
    return result[0] if result else None;

def insert_data():
    try:
        cursor = conn.cursor()
        data_to_insert = []

        for i in range(1, 15):
            internetSpeed = generate_random_internetSpeed()
            package_id = get_package_id(cursor, i)

            if package_id is not None:
                cursor.execute("INSERT INTO Internet_Package (packageID,internetSpeed) VALUES (?, ?)",
                               (package_id, internetSpeed))
            else:
                name = package.generate_random_provider();
                price = package.generate_random_price();
                
                id_from_Internet_Package = get_lastIndex(cursor);
                id_from_Internet_Package = id_from_Internet_Package +1;
                package_id = get_package_id(cursor,id);
                package_id = package_id +1;
                cursor.execute("INSERT INTO Package (ID, name, price) VALUES (?, ?, ?)",
                               (package_id, name,price))
                
                
                cursor.execute("INSERT INTO Internet_Package (ID, packageID, internetSpeed) VALUES (?,?,?)",
                               (id_from_Internet_Package,package_id, internetSpeed))

        conn.commit()
        print("Data inserted successfully.")

    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    insert_data()
