from decimal import Decimal
import sqlite3
import random
import script_for_generate_table_package as package;
import script_for_generate_table_TV_package as tv;
import script_for_generate_table_Internet_package as internet;
conn = sqlite3.connect('client_package.db')

def generate_random_channelCount():
    return random.randint(1, 200)

def get_package_id(cursor, package_id):
    cursor.execute("SELECT ID FROM Package WHERE ID = ?",(package_id,))
    result = cursor.fetchone()
    return result[0] if result else None


def get_tv_package_id(cursor, package_id):
    cursor.execute("SELECT ID FROM TV_Package WHERE ID = ?",(package_id,))
    result = cursor.fetchone()
    return result[0] if result else None 

def get_internet_package_id(cursor, package_id):
    cursor.execute("SELECT ID FROM Internet_Package WHERE ID = ?",(package_id,))
    result = cursor.fetchone()
    return result[0] if result else None 

def get_lastIndex(cursor):
    cursor = conn.cursor();
    cursor.execute("SELECT count(ID) FROM Internet_Package");
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
                
                TV_ID = get_tv_package_id(cursor, package_id)
                INTERNET_ID = get_internet_package_id(cursor, package_id)

                cursor.execute("INSERT INTO Combined_Package (ID, TV_ID, INTERNET_ID) VALUES (?, ?, ?)",
                               (i, TV_ID, INTERNET_ID))
            else:
                provider = package.generate_random_provider();
                price = package.generate_random_price();
                channelCount = tv.generate_random_channelCount();
                internetSpeed = internet.generate_random_internetSpeed();
                
                
                cursor.execute("INSERT INTO Package (name, price) VALUES (?, ?)",
                               (provider,price))
                cursor.execute("INSERT INTO TV_Package (packageID, channelCount) VALUES (?, ?)",
                               (i, channelCount))
                cursor.execute("INSERT INTO Internet_Package (packageID, internetSpeed) VALUES (?, ?)",
                               (i, internetSpeed))
                
                TV_ID = tv.get_lastIndex(cursor);
                INTERNET_ID = internet.get_lastIndex(cursor)

               
                cursor.execute("INSERT INTO Combined_Package (TV_ID, INTERNET_ID) VALUES (?, ?)",
                               (TV_ID, INTERNET_ID))

        conn.commit()
        print("Data inserted successfully.")

    except sqlite3.Error as e:
        print(f"Error inserting data: {e}")

    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    insert_data()