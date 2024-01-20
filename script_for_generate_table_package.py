import sqlite3
import random

def generate_random_provider():
    providers = ['Fios', 'Cox', 'Lomen',
                  'Sparklight', 'MTS', 'VIP',
                  'Yettel', 'Spectrum', 'Metronet',
                  'AT&T', 'XFinity', 'T-Mobile',
                  'Kinetic', 'Mediacom', 'SBB']

    random_provider = random.choice(providers)
    return random_provider

def generate_random_price():
    random_price = round(random.uniform(10,80),2)
    return random_price

def insert_data():
    data_to_insert = []
    conn = sqlite3.connect('client_package.db')
    cursor = conn.cursor()

    for i in range(1,15):
        name = generate_random_provider()
        price = generate_random_price()
        data_to_insert.append((i, name, price))
   
    for i in range(len(data_to_insert)):
        print(data_to_insert[i])

    try:
        cursor.executemany('INSERT INTO Package VALUES (?,?, ?)', data_to_insert)
        conn.commit()
        print("Data inserted successfully.")
    except sqlite3.Error as e:
        print(f"Error inserting data: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    insert_data()
