from tkinter import *
import sqlite3


def submit():
    conn = sqlite3.connect('Airport.db')

    c = conn.cursor()



    c.execute("INSERT INTO Booking VALUES (:Booking_ID, :Passenger_ID, :Flying_From, :Flying_Too, :IATA_Code, :Flight_ID, :Airline_Code)",
    {
        'Booking_ID': Booking_ID.get(),
        'Passenger_ID': Passenger_ID.get(),
        'Flying_From': Flying_From.get(),
        'Flying_Too': Flying_Too.get(),
        'IATA_Code': IATA_Code.get(),
        'Flight_ID': Flight_ID.get(),
        'Airline_Code': Airline_Code.get()


    })

    conn.commit()

    conn.close()

    Booking_ID.delete(0,END)
    Passenger_ID.delete(0, END)
    Flying_From.delete(0, END)
    Flying_Too.delete(0, END)
    IATA_Code.delete(0, END)
    Flight_ID.delete(0, END)
    Airline_Code.delete(0, END)

def query():
    conn = sqlite3.connect('Airport.db')

    c = conn.cursor()

    c.execute("SELECT * FROM Booking")
    records = c.fetchall()
    print(records)

    print_records = ''
    for record in records:
        print_records += str(record[0] + " // " + str(record[1]) + " // " + str(record[2]) + " // " + str(record[3]) + " // " + str(record[4]) + " // " + str(record[5]) + " // " + str(record[6]) + "\n")

    query_label = Label(root, text=print_records)
    query_label.grid(row=9, column=0,columnspan=2)



    conn.commit()

    conn.close()

root = Tk()
root.title('Add Booking')
root.geometry("400x400")


Booking_ID = Entry(root, width=30)
Booking_ID.grid(row=0, column=1, padx=20)

Passenger_ID = Entry(root, width=30)
Passenger_ID.grid(row=1, column=1)

Flying_From = Entry(root, width=30)
Flying_From.grid(row=2, column=1)

Flying_Too = Entry(root, width=30)
Flying_Too.grid(row=3, column=1)

IATA_Code = Entry(root, width=30)
IATA_Code.grid(row=4, column=1)

Flight_ID = Entry(root, width=30)
Flight_ID.grid(row=5, column=1)

Airline_Code = Entry(root, width=30)
Airline_Code.grid(row=6, column=1)


Booking_ID_Label = Label(root, text="Booking ID")
Booking_ID_Label.grid(row=0, column=0)

Passenger_ID_label = Label(root, text="Passenger ID")
Passenger_ID_label.grid(row=1, column=0)

Flying_From_label = Label(root, text="Flying From")
Flying_From_label.grid(row=2, column=0)

Flying_Too_label = Label(root, text="Flying To")
Flying_Too_label.grid(row=3, column=0)

IATA_Code_label = Label(root, text="IATA Code")
IATA_Code_label.grid(row=4, column=0)

Flight_ID_label = Label(root, text="Flight ID")
Flight_ID_label.grid(row=5, column=0)

Airline_Code_label = Label(root, text="Airline Code")
Airline_Code_label.grid(row=6, column=0)

submit_btn = Button(root, text="Add Record To Database", command = submit)
submit_btn.grid(row=7, column=0, columnspan=2, pady=10)

query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=8, column=0, columnspan=2, pady=10, padx=10, ipadx=137)



root.mainloop()