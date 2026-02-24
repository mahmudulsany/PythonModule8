import mysql.connector

connection= mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="user_id",
    password="password",
    autocommit=True
)
cursor= connection.cursor()

#A program that asks the user to enter the ICAO code of an airport.
icao_code= input("Enter ICAO Code: ")

#The program fetches and prints out the corresponding airport name and location (town) from the airport database.
sql= "select name, municipality from airport where ident = %s"
cursor.execute(sql,(icao_code,))

result= cursor.fetchone()

if result is not None:
    print(f"Airport name: {result[0]}")
    print(f"Town name: {result[1]}")
else:
    print("No Airport found with that ICAO code.")

cursor.close()
connection.close()
#The ICAO codes are stored in the ident column of the airport table.
