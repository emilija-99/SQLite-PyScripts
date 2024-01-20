import sqlite3

def create_tables():
    try:
        conn = sqlite3.connect('client_package.db')
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Package (
                ID INTEGER PRIMARY KEY ,
                name TEXT NOT NULL,
                price DECIMAL(10, 2) NOT NULL
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS TV_Package (
                ID INTEGER PRIMARY KEY ,
                packageID INTEGER REFERENCES Package(ID),
                channelCount INTEGER
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Internet_Package (
                ID INTEGER PRIMARY KEY ,
                packageID INTEGER REFERENCES Package(ID),
                internetSpeed INTEGER
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Combined_Package (
                ID INTEGER PRIMARY KEY ,
                TV_ID INTEGER REFERENCES TV_Package(ID),
                INTERNET_ID INTEGER REFERENCES Internet_Package(ID)
            )
        ''')

        conn.commit()
        print("Tables created successfully.")

    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")

    finally:
            cursor.close()
            conn.close()

if __name__ == "__main__":
    create_tables()
