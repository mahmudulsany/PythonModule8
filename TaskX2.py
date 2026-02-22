import mysql.connector


def update_salary(emp_id, new_salary):
    sql= "update info set pay_h=%s where id=%s"
    cursor= connection.cursor()
    cursor.execute(sql, (new_salary, emp_id))
    if cursor.rowcount==1:
        print("Salary updated successfully")
    else:
        print("No employee with that ID.")
    cursor.close()

connection = mysql.connector.connect(
    host= "127.0.0.1",
    port= "3306",
    database= "my_one",
    user= "root",
    password= "6517",
    autocommit= True
)

emp_id = int(input("Enter employee ID: "))
new_salary = float(input("Enter new salary: "))
update_salary(emp_id, new_salary)
connection.close()