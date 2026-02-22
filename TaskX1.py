import mysql.connector
def get_employee_by_last_name(last_name):
    sql= "select id, f_name, l_name, pay_h, hire_date, email, p_number from info where l_name=%s"
    cursor= connection.cursor()
    cursor.execute(sql,(last_name,))
    result= cursor.fetchall()
    if cursor.rowcount>0:
        for row in result:
            print(f"Hello! I'm {row[1]} {row[2]}. "
                  f"My salary is {row[3]} euros per hour. "
                  f"Hired on {row[4]}, "
                  f"Email: {row[5]}, "
                  f"Phone: {row[6]}")
    else:
        print("No employee found.")
    cursor.close()

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='my_one',
    user='root',
    password='6517',
    autocommit=True
)

last_name= input("Enter last name: ")
get_employee_by_last_name(last_name)


connection.close()