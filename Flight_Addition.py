from tkinter import *
import sqlite3


def submit():
    conn = sqlite3.connect('Airport.db')

    c = conn.cursor()



    c.execute("INSERT INTO Flights VALUES (:Flight_ID, :Flying_From, :Flying_To, :AirLine_Code, :Take_Off_Time)",
    {
        'Flight_ID': Flight_ID.get(),
        'Flying_From': Flying_From.get(),
        'Flying_To': Flying_To.get(),
        'AirLine_Code': AirLine_Code.get(),
        'Take_Off_Time': Take_Off_Time.get()
    })

    conn.commit()

    conn.close()

    Flight_ID.delete(0,END)
    Flying_From.delete(0, END)
    Flying_To.delete(0, END)
    AirLine_Code.delete(0, END)
    Take_Off_Time.delete(0, END)

def query():
    conn = sqlite3.connect('Airport.db')

    c = conn.cursor()

    c.execute("SELECT * FROM Flights")
    records = c.fetchall()
    print(records)

    print_records = ''
    for record in records:
        print_records += str(record[0] + " // " + str(record[1]) + " // " + str(record[2]) + " // " + str(record[3]) + " // " + str(record[4]) + "\n")

    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0,columnspan=2)



    conn.commit()

    conn.close()

root = Tk()
root.title('Add Flight')
root.geometry("400x400")


Flight_ID = Entry(root, width=30)
Flight_ID.grid(row=0, column=1, padx=20)

Flying_From = Entry(root, width=30)
Flying_From.grid(row=1, column=1)

Flying_To = Entry(root, width=30)
Flying_To.grid(row=2, column=1)

AirLine_Code = Entry(root, width=30)
AirLine_Code.grid(row=3, column=1)

Take_Off_Time = Entry(root, width=30)
Take_Off_Time.grid(row=4, column=1)

Flight_ID_label = Label(root, text="Flight ID")
Flight_ID_label.grid(row=0, column=0)

Flying_From_label = Label(root, text="Flying From")
Flying_From_label.grid(row=1, column=0)

Flying_To_label = Label(root, text="Flying Too")
Flying_To_label.grid(row=2, column=0)

AirLine_Code_Label = Label(root, text="Airline Code")
AirLine_Code_Label.grid(row=3, column=0)

Take_Off_Time_Label = Label(root, text="Take Off Time")
Take_Off_Time_Label.grid(row=4, column=0)

submit_btn = Button(root, text="Add Record To Database", command = submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10)

query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)



root.mainloop()