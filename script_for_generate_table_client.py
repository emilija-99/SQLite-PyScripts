import sqlite3
import random

def username_generator(num):
    username = 'user' + str(num)
    return username

def generate_random_first_name():
    first_names = ['Liam', 'Noah', 'Oliver',
                   'Wiliam', 'James', 'Henry',
                   'Lucas', 'Benjamin', 'Theodore',
                   'Olivia', 'Emma', 'Charlotte',
                   'Amelia', 'Sophia', 'Isabella',
                   'Ava', 'Mia', 'Evalyn', 'Luna']

    random_first_name = random.choice(first_names)
    return random_first_name

def generate_random_last_name():
    last_names = ['Smith', 'Johnson', 'Williams',
                  'Brown', 'Jones', 'Garcia',
                  'Miller', 'Martinez', 'Lopez',
                  'Gonzalez', 'Wilson', 'Anderson',
                  'Taylor', 'Moore', 'Jackson',
                  'Martin', 'Lee', 'Harris', 'Clark']

    random_last_name = random.choice(last_names)
    return random_last_name

def insert_data():
    data_to_insert = []
    conn = sqlite3.connect('client_package.db');
    cursor = conn.cursor()

    for i in range(1,50):
        username = username_generator(i)
        first_name = generate_random_first_name()
        last_name = generate_random_last_name()
        data_to_insert.append((i,username, first_name, last_name))
   
    for i in range(len(data_to_insert)):
        print(data_to_insert[i])

    try:
        cursor.executemany('INSERT INTO Client VALUES (?, ?, ?, ?)', data_to_insert)
        conn.commit()
        print("Data inserted successfully.")
    except sqlite3.Error as e:
        print(f"Error inserting data: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    insert_data()
