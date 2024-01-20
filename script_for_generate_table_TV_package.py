from decimal import Decimal
import sqlite3
import random
import script_for_generate_table_package as package;
conn = sqlite3.connect('client_package.db')
data_packages = [];
def generate_random_channelCount():
    channelCount = random.randint(1, 200)
    return channelCount;


def get_lastIndex(cursor):
    cursor = conn.cursor();
    cursor.execute("SELECT count(ID) FROM TV_Package");
    result = cursor.fetchone();

def get_all_packages():
    try:
        cursor = conn.cursor();
        cursor.execute("SELECT * FROM Pakcage")
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
    
def insert_data():
    try:
        cursor = conn.cursor()

        for i in range(1, 15):
            channelCount = generate_random_channelCount()
            package_id = get_package_id(cursor, i)

            if package_id is not None:
                cursor.execute("INSERT INTO TV_Package (packageID, channelCount) VALUES (?, ?)",
                               (package_id, channelCount))
            else:
                
                price = package.generate_random_price();
                name = package.generate_random_provider();
                id_from_TV_Package = get_lastIndex(cursor);
                id_from_TV_Package = id_from_TV_Package +1;
                package_id = get_package_id(cursor,id);
                package_id = package_id +1;
                cursor.execute("INSERT INTO Package (ID, name, price) VALUES (?, ?, ?)",
                               (package_id, name, price))
                
                
                cursor.execute("INSERT INTO TV_Package (ID, packageID, channelCount) VALUES (?, ?, ?)",
                               (id_from_TV_Package, package_id, channelCount))

        conn.commit()
        print("Data inserted successfully.")

    except sqlite3.Error as e:
        print(f"Error inserting data: {e}")

    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    insert_data()
