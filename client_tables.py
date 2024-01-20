import sqlite3

def create_tables():
    try:
        conn = sqlite3.connect('client_package.db')
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Client (
                ID INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                firstName TEXT NOT NULL,
                lastName TEXT NOT NULL
            )
        ''')

        conn.commit()
        print("Tables created successfully.")

    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")

    finally:
            conn.close()

if __name__ == "__main__":
    create_tables()
