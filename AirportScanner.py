import tkinter
from tkinter import *
from tkinter import messagebox
import cv2
import PIL.Image, PIL.ImageTk
import time
import pyzbar.pyzbar as pyzbar
import os
import sqlite3
import random
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as etree




class App:
    def __init__(self, window, window_title, video_source=0):
       self.window = window
       self.window.title(window_title)
       self.video_source = video_source
        # open video source (by default this will try to open the computer webcam)
       self.vid = MyVideoCapture(self.video_source)
       # Create a canvas that can fit the above video source size
       self.canvas = tkinter.Canvas(window, width = self.vid.width, height = self.vid.height)
       self.canvas.grid(row=0, column=0, sticky='n')

       # Button that lets the user take a snapshot
       self.btn_snapshot=tkinter.Button(window, text="Snapshot", width=50, command=self.snapshot)
       self.btn_snapshot.grid(row=1, column=0, sticky='n')

       frame1 = Frame(self.window)
       frame1.grid(row=0,column=1, sticky='n')






       self.Booking_ID_Label=Label(frame1, text="Booking ID")
       self.Booking_ID_Label.grid(row=0,column=0, sticky='n')
       self.Booking_ID_Entry=Entry(frame1, width=30)
       self.Booking_ID_Entry.grid(row=0,column=1, sticky='n')


       self.Passenger_ID_Label=Label(frame1, text="Passenger ID")
       self.Passenger_ID_Label.grid(row=1,column=0, sticky='n')
       self.Passenger_ID_Entry=Entry(frame1, width=30)
       self.Passenger_ID_Entry.grid(row=1,column=1, sticky='n')

       self.First_Name_Label = Label(frame1, text="First Name")
       self.First_Name_Label.grid(row=2, column=0, sticky='n')
       self.First_Name_Entry = Entry(frame1, width=30)
       self.First_Name_Entry.grid(row=2, column=1, sticky='n')

       self.Last_Name_Label = Label(frame1, text="Last Name")
       self.Last_Name_Label.grid(row=3, column=0, sticky='n')
       self.Last_Name_Entry = Entry(frame1, width=30)
       self.Last_Name_Entry.grid(row=3, column=1, sticky='n')

       self.Flying_From_Label=Label(frame1, text="Flying From")
       self.Flying_From_Label.grid(row=4,column=0, sticky='n')
       self.Flying_From_Entry=Entry(frame1, width=30)
       self.Flying_From_Entry.grid(row=4,column=1, sticky='n')

       self.Flying_to_Label=Label(frame1, text="Flying To")
       self.Flying_to_Label.grid(row=5,column=0, sticky='n')
       self.Flying_to_Entry=Entry(frame1, width=30)
       self.Flying_to_Entry.grid(row=5,column=1, sticky='n')

       self.IATA_Code_Label=Label(frame1, text="IATA Code")
       self.IATA_Code_Label.grid(row=6,column=0, sticky='n')
       self.IATA_Code_Entry=Entry(frame1, width=30)
       self.IATA_Code_Entry.grid(row=6,column=1, sticky='n')

       self.Flight_ID_Label=Label(frame1, text="Flight ID")
       self.Flight_ID_Label.grid(row=7,column=0, sticky='n')
       self.Flight_ID_Entry=Entry(frame1, width=30)
       self.Flight_ID_Entry.grid(row=7,column=1, sticky='n')

       self.Airline_ID_Label=Label(frame1, text="Airline ID")
       self.Airline_ID_Label.grid(row=8,column=0, sticky='n')
       self.Airline_ID_Entry=Entry(frame1, width=30)
       self.Airline_ID_Entry.grid(row=8,column=1, sticky='n')

       self.Weight_Label=Label(frame1, text="Weight")
       self.Weight_Label.grid(row=9,column=0, sticky='n')
       self.Weight_Entry=Entry(frame1, width=30)
       self.Weight_Entry.grid(row=9,column=1, sticky='n')

       self.btn_generate_weight = tkinter.Button(frame1, text="Weigh Bag", width=25, command=self.Generate_Weight)
       self.btn_generate_weight.grid(row=10, column=0, sticky='n')

       self.btn_Checkin = tkinter.Button(frame1, text="Check in", width=25, command=self.Check_in)
       self.btn_Checkin.grid(row=10, column=1, sticky='n')

       self.Close_Check_In_Entry = Entry(frame1, width=30)
       self.Close_Check_In_Entry.grid(row=11, column=1, sticky='n')

       self.btn_Close_Checkin = tkinter.Button(frame1, text="Close Check in", width=25,command=self.Close_Check_In)
       self.btn_Close_Checkin.grid(row=11, column=0, sticky='n')










       # After it is called once, the update method will be automatically called every delay milliseconds
       self.delay = 15
       self.update()

       self.window.mainloop()

    def snapshot(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
            cv2.imwrite("SavedImage.jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

            time.sleep(2)
            img = cv2.imread("SavedImage.jpg")

            decodedObjects = pyzbar.decode(img)


            for obj in decodedObjects:
                x = obj.data
                y = x.decode("utf-8")
                conn = sqlite3.connect('Airport.db')


                c = conn.cursor()
                select_query = """SELECT * FROM Booking WHERE Booking_ID =  ?"""
                c.execute(select_query, (y,))
                records = c.fetchall()
                for row in records:

                    temp1 = (row[0])
                    temp2 = (row[1])
                    temp3 = (row[2])
                    temp4 = (row[3])
                    temp5 = (row[4])
                    temp6 = (row[5])
                    temp7 = (row[6])



                    self.Booking_ID_Entry.insert(0,temp1)
                    self.Passenger_ID_Entry.insert(0,temp2)
                    self.Flying_From_Entry.insert(0,temp3)
                    self.Flying_to_Entry.insert(0,temp4)
                    self.IATA_Code_Entry.insert(0,temp5)
                    self.Flight_ID_Entry.insert(0,temp6)
                    self.Airline_ID_Entry.insert(0,temp7)

                select_name_query = """SELECT * FROM Passenger WHERE Passenger_ID =  ?"""
                c.execute(select_name_query, (temp2,))
                name_records = c.fetchall()
                for row in name_records:
                    temp8 = (row[1])
                    temp9 = (row[2])

                    self.First_Name_Entry.insert(0, temp8)
                    self.Last_Name_Entry.insert(0, temp9)



                conn.close()

            os.remove("SavedImage.jpg")





    def update(self):
         # Get a frame from the video source
         ret, frame = self.vid.get_frame()

         if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)

            self.window.after(self.delay, self.update)


    def Generate_Weight(self):
        weight = random.randint(1, 27)
        if weight > 25:
            tkinter.messagebox.showerror(title="Warning!", message="Weight is too high")
        else:
            self.Weight_Entry.insert(0, weight)


    def Check_in(self):
        conn = sqlite3.connect('Airport.db')

        c = conn.cursor()
        c.execute(
            "INSERT INTO Checked_In VALUES (:Booking_ID, :Passenger_ID, :First_Name, :Last_Name, :Flying_From, :Flying_Too, :IATA_Code, :Flight_ID, :Airline_Code, :Weight)",
            {
                'Booking_ID': self.Booking_ID_Entry.get(),
                'Passenger_ID': self.Passenger_ID_Entry.get(),
                'First_Name': self.First_Name_Entry.get(),
                'Last_Name': self.Last_Name_Entry.get(),
                'Flying_From': self.Flying_From_Entry.get(),
                'Flying_Too': self.Flying_to_Entry.get(),
                'IATA_Code': self.IATA_Code_Entry.get(),
                'Flight_ID': self.Flight_ID_Entry.get(),
                'Airline_Code': self.Airline_ID_Entry.get(),
                'Weight': self.Weight_Entry.get()

            })

        c.execute(
        "INSERT INTO Passengers_On_Plane VALUES (:Booking_ID, :First_Name, :Last_Name, :Weight)",
        {
            'Booking_ID': self.Booking_ID_Entry.get(),
            'First_Name': self.First_Name_Entry.get(),
            'Last_Name': self.Last_Name_Entry.get(),
            'Weight': self.Weight_Entry.get()

        })


        f = open('Weight-' + self.Flight_ID_Entry.get()+ '.txt', 'r')
        totalweight = int(f.readline())
        f.close()
        Newtotalweight = int(totalweight) + int(self.Weight_Entry.get())
        f = open('Weight-' + self.Flight_ID_Entry.get()+ '.txt', 'w')
        Newtotalweight = str(Newtotalweight)
        f.write(Newtotalweight)
        f.close()


        #if os.path.exists(r'C:\Users\Ben\PycharmProjects\Airport\Weight-' + self.Flight_ID_Entry.get() + '.txt'):
         #   f = open(r'C:\Users\Ben\PycharmProjects\Airport\Weights\Weight-' + self.Flight_ID_Entry.get() + ".txt", "r")
          #  totalweight = int(f.readline())
           # print(totalweight)
           # f.close()
           # Newtotalweight = int(totalweight) + int(self.Weight_Entry.get())
           # print(Newtotalweight)
           # f = open(r'C:\Users\Ben\PycharmProjects\Airport\Weights\Weight-' + self.Flight_ID_Entry.get() + ".txt", "w")
           # Newtotalweight = str(Newtotalweight)
           # f.write(Newtotalweight)
           # f.close()

        #else:
         #   print("Not found")
          #  f = open(r"Weight-" + self.Flight_ID_Entry.get() + ".txt", "w")
           # f.write(self.Weight_Entry.get())
            #f.close()


        root=Element('Luggage Ticket')
        tree=ElementTree(root)

        Booking_ID_Tag=Element('Booking_ID')
        root.append(Booking_ID_Tag)
        Booking_ID_Tag.text = self.Booking_ID_Entry.get()

        Passenger_ID_Tag = Element('Passenger_ID')
        root.append(Passenger_ID_Tag)
        Passenger_ID_Tag.text = self.Passenger_ID_Entry.get()

        First_Name_Tag=Element('First_Name')
        root.append(First_Name_Tag)
        First_Name_Tag.text = self.First_Name_Entry.get()

        Last_Name_Tag = Element('Last_Name')
        root.append(Last_Name_Tag)
        Last_Name_Tag.text = self.Last_Name_Entry.get()

        Flying_From_Tag = Element('Flying_From')
        root.append(Flying_From_Tag)
        Flying_From_Tag.text = self.Flying_From_Entry.get()

        Flying_To_Tag = Element('Flying_To')
        root.append(Flying_To_Tag)
        Flying_To_Tag.text = self.Flying_to_Entry.get()

        IATA_Code_Tag = Element('IATA_Code')
        root.append(IATA_Code_Tag)
        IATA_Code_Tag.text = self.IATA_Code_Entry.get()

        Flight_ID_Tag = Element('Flight_ID')
        root.append(Flight_ID_Tag)
        Flight_ID_Tag.text = self.Flight_ID_Entry.get()

        Airline_ID_Tag = Element('Airline_ID')
        root.append(Airline_ID_Tag)
        Airline_ID_Tag.text = self.Airline_ID_Entry.get()

        Weight_Tag = Element('Weight')
        root.append(Weight_Tag)
        Weight_Tag.text = self.Weight_Entry.get()

        tree.write(open(r"C:\Users\Ben\PycharmProjects\Airport\Luggage Tickets\Ticket- " + self.Booking_ID_Entry.get() + ".xml","wb"))










        self.Booking_ID_Entry.delete(0, END)
        self.Passenger_ID_Entry.delete(0, END)
        self.First_Name_Entry.delete(0, END)
        self.Last_Name_Entry.delete(0, END)
        self.Flying_From_Entry.delete(0, END)
        self.Flying_to_Entry.delete(0, END)
        self.IATA_Code_Entry.delete(0, END)
        self.Flight_ID_Entry.delete(0, END)
        self.Airline_ID_Entry.delete(0, END)
        self.Weight_Entry.delete(0, END)

        tkinter.messagebox.showinfo(title="Notification", message="Record Added")


        conn.commit()

        conn.close()



    def Close_Check_In(self):

        conn = sqlite3.connect('Airport.db')

        c = conn.cursor()

        root = Element('Passengers on plane')
        tree = ElementTree(root)

        c.execute("SELECT * FROM Passengers_On_Plane")
        records = c.fetchall()

        f = open('Weight-' + self.Close_Check_In_Entry.get()+ '.txt', 'r')
        totalweight = str(f.readline())
        f.close()


        Flight_ID_Tag = Element('Flight_ID')
        Total_Weight_Tag = Element('Total_Weight')
        Booking_ID_Tag = Element('Booking_ID')
        First_Name_Tag = Element('First_Name')
        Last_Name_Tag = Element('Last_Name')
        Weight_Tag = Element('Weight')


        root.append(Flight_ID_Tag)
        Flight_ID_Tag.text = (self.Close_Check_In_Entry.get())
        root.append(Total_Weight_Tag)
        Total_Weight_Tag.text = (totalweight)

        for record in records:

            root.append(Booking_ID_Tag)
            Booking_ID_Tag.text = (record[0])

            root.append(First_Name_Tag)
            First_Name_Tag.text = (record[1])

            root.append(Last_Name_Tag)
            Last_Name_Tag.text = (record[2])

            root.append(Weight_Tag)
            Weight_Tag.text = str(record[3])

        tree.write(open(r"C:\Users\Ben\PycharmProjects\Airport\Server\Passengers_on_Flight- " + self.Close_Check_In_Entry.get() + ".xml","wb"))

        tkinter.messagebox.showinfo(title="Notification", message="Check-in for flight " + self.Close_Check_In_Entry.get() + " has been closed")
        self.Close_Check_In_Entry.delete(0, END)

        c.execute("DELETE FROM Passengers_On_Plane")
        conn.commit()








class MyVideoCapture:
    def __init__(self, video_source=0):
        # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)

     # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

 # Create a window and pass it to the Application object
App(tkinter.Tk(), "Scanner")