import sqlite3

# Establish a connection and a cursor
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# Query All Data on a condition
cursor.execute("SELECT * FROM events WHERE date='2088.10.15'")
rows = cursor.fetchall()
print(rows)

# Query Certain Columns on a condition
cursor.execute("SELECT band, date FROM events WHERE date='2088.10.15'")
rows = cursor.fetchall()
print(rows)

# Insert New Rows
new_rows = [('Cats', 'Cat City', '2088.10.16'),
            ('Hens', 'Hen City', '2088.10.16')]
cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
connection.commit()

# Query ALl Data
cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print(rows)