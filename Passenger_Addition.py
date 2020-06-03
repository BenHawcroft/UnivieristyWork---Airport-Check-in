from tkinter import *
import sqlite3


def submit():
    conn = sqlite3.connect('Airport.db')

    c = conn.cursor()



    c.execute("INSERT INTO Passenger VALUES (:Passenger_ID, :f_name, :l_name, :Gender, :Disability)",
    {
        'Passenger_ID': Passenger_ID.get(),
        'f_name': f_name.get(),
        'l_name': l_name.get(),
        'Gender': Gender.get(),
        'Disability': Disability.get()
    })

    conn.commit()

    conn.close()

    Passenger_ID.delete(0,END)
    f_name.delete(0, END)
    l_name.delete(0, END)
    Gender.delete(0, END)
    Disability.delete(0, END)

def query():
    conn = sqlite3.connect('Airport.db')

    c = conn.cursor()

    c.execute("SELECT * FROM Passenger")
    records = c.fetchall()
    print(records)

    print_records = ''
    for record in records:
        print_records += str(record[1] + " " + str(record[2]) + "\n")

    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0,columnspan=2)



    conn.commit()

    conn.close()

root = Tk()
root.title('Add Customer')
root.geometry("400x400")


Passenger_ID = Entry(root, width=30)
Passenger_ID.grid(row=0, column=1, padx=20)

f_name = Entry(root, width=30)
f_name.grid(row=1, column=1)

l_name = Entry(root, width=30)
l_name.grid(row=2, column=1)

Gender = Entry(root, width=30)
Gender.grid(row=3, column=1)

Disability = Entry(root, width=30)
Disability.grid(row=4, column=1)


Passenger_ID_label = Label(root, text="Passenger ID")
Passenger_ID_label.grid(row=0, column=0)

f_name_label = Label(root, text="First Name")
f_name_label.grid(row=1, column=0)

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=2, column=0)

Gender_label = Label(root, text="Gender")
Gender_label.grid(row=3, column=0)

Disability_label = Label(root, text="Disability")
Disability_label.grid(row=4, column=0)

submit_btn = Button(root, text="Add Record To Database", command = submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10)

query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)



root.mainloop()