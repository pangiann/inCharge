import mysql.connector
import random
import datetime

# insert session details into database
def log_session(Customer_ID, Point_ID, Protocol, Type, Points, Date, Time_Start, Time_End, Amount, Energy):
    query = "INSERT INTO charging_session (Customer_ID, Point_ID, Protocol, Type, Points, Date, Start_Time, End_Time, Amount, Energy) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    data = (Customer_ID, Point_ID, Protocol, Type, Points, Date, Time_Start, Time_End, Amount, Energy)
    cursor.execute(query, data)
    mydb.commit()

def find_users():
    query = "SELECT Username FROM customer"
    cursor.execute(query)
    result = cursor.fetchall()
    users = []
    for i in range(len(result)):
        users.append(result[i][0])
    return users

def find_points():
    query = "SELECT Point_No FROM charging_point"
    cursor.execute(query)
    result = cursor.fetchall()
    points = []
    for i in range(len(result)):
        points.append(result[i][0])
    return points

def random_date():
    start_date = datetime.date(2019, 1, 1)
    end_date = datetime.date(2021, 2, 27)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date

def random_time():
    hours = random.randint(0,23)
    if (hours < 10):
        hour = '0'+str(hours)
    else:
        hour = str(hours)
    minutes = random.randint(0,59)
    if (minutes < 10):
        minute = '0'+str(minutes)
    else:
        minute = str(minutes)
    seconds = random.randint(0,59)
    if (seconds < 10):
        second = '0'+str(seconds)
    else:
        second = str(seconds)
    return hour+':'+minute+':'+second

def random_price():
    euros = random.randint(0,2)
    cents = random.randint(0,99)
    price_str = str(euros)+'.'+str(cents)
    price = float(price_str)
    return price

def random_energy():
    integer = random.randint(10,50)
    decimal = random.randint(0,99)
    energy_str = str(integer)+'.'+str(decimal)
    energy = float(energy_str)
    return energy

mydb = mysql.connector.connect(
    user="root",
    password="42DataBase42",
    database="sql_inCharge",
    host="127.0.0.1",
    port="3306",
    auth_plugin='mysql_native_password'
)
cursor = mydb.cursor()

user_list = find_users()
points_list = find_points()
type_list = ['Card', 'Contract']

for i in range(5000):
    log_session(user_list[random.randint(0,len(user_list)-1)], points_list[random.randint(0,len(points_list)-1)], 'dummy', type_list[random.randint(0,len(type_list)-1)], random.randint(0,100), random_date(), random_time(), random_time(), random_price(), random_energy())
