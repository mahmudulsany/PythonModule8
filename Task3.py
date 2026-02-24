import mysql.connector
#Calculate the distance using the geopy
import geopy.distance

connection= mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="user_id",
    password="password",
    autocommit=True
)
cursor= connection.cursor()

#A program that asks the user to enter the ICAO codes of two airports.
icao1= input("Enter the first ICAO code: ")
icao2= input("Enter the second ICAO code: ")

sql= "select name, latitude_deg, longitude_deg from airport where ident = %s"

cursor.execute(sql,(icao1,))
result1= cursor.fetchone()

cursor.execute(sql,(icao2,))
result2= cursor.fetchone()

if result1 is not None and result2 is not None:
    name1, lat1, lon1 = result1
    name2, lat2, lon2 = result2

    coord1= (lat1, lon1)
    coord2= (lat2, lon2)

    distance_km= geopy.distance.geodesic(coord1,coord2).kilometers

#The program prints out the distance between the two airports in kilometers.
    print(f"Distance between {icao1} and {icao2} is {distance_km:.3f} km")
else:
    print("No airports found with this ICAO code")

cursor.close()
connection.close()
#The calculation is based on the airport coordinates fetched from the database.
