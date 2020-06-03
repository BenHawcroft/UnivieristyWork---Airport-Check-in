import sqlite3

conn = sqlite3.connect('Airport.db')

c = conn.cursor()

def CreateTables ():
    c.execute("""CREATE TABLE Passenger (
               Passenger_ID text primary key,
               First_Name text,
               Last_Name text,
               Gender text,
               Disability text
                )""")
    print("Table made")

    c.execute("""CREATE TABLE Booking (
               Booking_ID text primary key,
               Passenger_ID text,
               Flying_From text,
               Flying_Too text,
               IATA_Code text,
               Flight_ID text,
               Airline_Code text,
               FOREIGN KEY (Passenger_ID) REFERENCES Passenger (Passenger_ID),
               FOREIGN KEY (IATA_Code) REFERENCES Airports (IATA_Code),
               FOREIGN KEY (Flight_ID) REFERENCES Flights (Flight_ID),
               FOREIGN KEY (Airline_Code) REFERENCES Airlines (Airline_Code)
                )""")
    print("Table made")



    c.execute("""CREATE TABLE Flights (
               Flight_ID text primary key,
               Flying_From text,
               Flying_To text,
               Airline_Code text,
               Take_Off_Time text,
               FOREIGN KEY (Airline_Code) REFERENCES Airlines (Airline_Code)
                )""")
    print("Table made")





    c.execute("""CREATE TABLE Checked_In (
               Booking_ID text primary key,
               Passenger_ID text,
               First_Name text,
               Last_Name text,
               Flying_From text,
               Flying_To text,
               Flight_ID text,
               IATA_Code text,
               Airline_Code text,
               Weight integer integer,
               FOREIGN KEY (Booking_ID) REFERENCES Booking (Booking_ID),
               FOREIGN KEY (Passenger_ID) REFERENCES Passenger (Passenger_ID),
               FOREIGN KEY (IATA_Code) REFERENCES Airports (IATA_Code),
               FOREIGN KEY (Airline_Code) REFERENCES Airlines (Airline_Code),
               FOREIGN KEY (Flight_ID) REFERENCES Flights (Flight_ID)           

                )""")
    print("Table made")

    c.execute("""CREATE TABLE Passengers_On_Plane (
               Booking_ID text,
               First_Name text,
               Last_Name text,
               Weight integer,
               FOREIGN KEY (Booking_ID) REFERENCES Booking (Booking_ID)

                )""")
    print("Table made")

    c.execute("""CREATE TABLE Airports (
               Name text,
               IATA_Code text primary key,
               State_Code text,
               Country_Code text,
               Country_Name text
                
                )""")
    print("Table made")

    c.execute("""CREATE TABLE Airlines (
               Airline_Name text,      
               Airline_Code text primary key,
               Airline_Country text
                )""")
    print("Table made")

    conn.commit()


CreateTables()



conn.close()
