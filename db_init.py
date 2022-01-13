# Initial the sqLite database this function will run before the database
import sqlite3
# Set the name of the database as datbase.db  after the execute you will see a databased.db in the folder
connection = sqlite3.connect('database.db')
# read the sql file to create the table 'urls'
with open('schema.sql') as f:
    connection.executescript(f.read())

connection.commit()
connection.close()
