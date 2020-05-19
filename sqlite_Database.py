import sqlite3

conn = sqlite3.connect('Airport.db')

c = conn.cursor()

def CreateTables ():
    c.execute("""CREATE TABLE Passenger (
               Passenger_ID integer primary key,
               First_Name text,
               Last_Name text,
               Gender text,
               Disability text
                )""")
    print("Table made")

    c.execute("""CREATE TABLE Boarding_Passenger (
               Passenger_Flight_ID integer primary key,
               Passenger_ID integer,
               Flying_From text,
               Flying_To text,
               IATA_Code,
               Flight_ID integer,
               Airline_ID integer,
               Weight text text,
               FOREIGN KEY (Passenger_ID) REFERENCES Passenger (Passenger_ID),
               FOREIGN KEY (IATA_Code) REFERENCES Airports (IATA_Code),
               FOREIGN KEY (Airline_ID) REFERENCES Airlines (Airline_Code),
               FOREIGN KEY (Flight_ID) REFERENCES Passengers_On_Plane (Flight_ID)           

                )""")
    print("Table made")

    c.execute("""CREATE TABLE Passengers_On_Plane (
               Flight_ID integer primary key,
               Passenger_ID integer,
               Weight text,
               FOREIGN KEY (Passenger_ID) REFERENCES Passenger (Passenger_ID),
               FOREIGN KEY (Weight) REFERENCES Boarding_Passenger (Weight)        

                )""")
    print("Table made")

    c.execute("""CREATE TABLE Airports (
               IATA_Code text primary key,        
               Airport_Name Text,
               Location_Served Text
                )""")
    print("Table made")

    c.execute("""CREATE TABLE Airlines (
               Airline_Code integer primary key,        
               Airline_Name Text,
               Country Text
                )""")
    print("Table made")

    conn.commit()



conn.close()
