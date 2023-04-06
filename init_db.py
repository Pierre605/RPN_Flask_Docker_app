import sqlite3

DATABASE = 'app.db'
db = sqlite3.connect(DATABASE)

cursor = db.cursor()

# Creation of table "operations". If it existed already, we delete the table and create a new one
cursor.execute('DROP TABLE IF EXISTS operations')
cursor.execute("""CREATE TABLE operations (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            query VARCHAR(200) NOT NULL, result VARCHAR(200), sent datetime)""")


# We save our changes into the database file
db.commit()

# We close the connection to the database
db.close()
