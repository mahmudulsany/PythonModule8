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

#A program that asks the user to enter the area code (for example FI)
country_code = input("Enter country code (FI): ")

sql = """
SELECT type, COUNT(*) 
FROM airport
WHERE iso_country = %s
GROUP BY type
ORDER BY type
"""

cursor.execute(sql, (country_code,))
result = cursor.fetchall()

#and prints out the airports located in that country ordered by airport type.
if result is not None:
    print(f"Airports in country: {country_code}")
    for row in result:
        airport_type = row[0]
        count = row[1]
        print(f"{airport_type}: {count}")
else:
    print("No airports found with that country code.")


cursor.close()
connection.close()

#For example, Finland has 65 small airports, 15 helicopter airports and so on.
