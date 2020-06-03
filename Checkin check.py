from tkinter import *
import sqlite3

conn = sqlite3.connect('Airport.db')

c = conn.cursor()

c.execute("SELECT * FROM Passengers_On_Plane")
records = c.fetchall()
print(records)
