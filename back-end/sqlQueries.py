# bash commands used to run this
# pip3 install mysql-connector-python-rf
# pip3 install mysql-connector-python

import os
import hashlib
import mysql.connector
import datetime

mydb = mysql.connector.connect(
    user="root",
    password="42DataBase42", # please don't hack us
    database="sql_inCharge",
    host="127.0.0.1",
    port="3306",
    auth_plugin='mysql_native_password',
    allow_local_infile = "True",
    use_pure='True'

)
cursor = mydb.cursor()
cursor.execute("SET GLOBAL max_allowed_packet=1073741824")




# hash plaintext password with salt and return value
def hash_password(password, salt):
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return key

# return random 32 byte value to be used as salt for user
def create_salt():
    salt = os.urandom(32)
    return salt



def healthcheck():
    query = "SELECT * FROM superadmin;"
    cursor.execute(query)
    result = cursor.fetchall()
    mydb.commit()
    return result

# insert manufacturer in database
def insert_manufacturer(Manufacturer_Name, City = None, Street_Name = None, Street_Number = None, Postal_Code = None, Email = None, Phone = None):
    query = "INSERT INTO manufacturer VALUES (%s, %s, %s, %s, %s, %s, %s);"
    data = (Manufacturer_Name, City, Street_Name, Street_Number, Postal_Code, Email, Phone)
    cursor.execute(query, data)
    mydb.commit()

# delete manufacturer from database given his Manufacturer_Name
def delete_manufacturer(Manufacturer_Name):
    query = "DELETE FROM manufacturer WHERE Brand_Name = %s;"
    data = (Manufacturer_Name,)
    cursor.execute(query, data)
    mydb.commit()

# insert car in database
def insert_car(car_No, brand, model, type, capacitance, release_year = None):
    query = "INSERT INTO car VALUES (%s, %s, %s, %s, %s, %s);"
    data = (car_No, brand, model, type, capacitance, release_year)
    cursor.execute(query, data)
    mydb.commit()

# delete car from database given its car_No
def delete_car(car_No):
    query = "DELETE FROM car WHERE car_No = %s;"
    data = (car_No,)
    cursor.execute(query, data)
    mydb.commit()

# TODO:
# default value for Car_Release_Year can be None - implement in frontend?
# insert customer in database
def insert_customer(Username, Car_Brand, Car_Model, Password, First_Name, Last_Name, Birth_Date, Points = 0, City = None, Street_Name = None, Street_Number = None, Postal_Code = None, Family_Members = None, Email = None, Phone = None):
    query = "SELECT car_No FROM car WHERE brand = %s AND model = %s;"
    data = (Car_Brand, Car_Model)
    cursor.execute(query, data)
    Car_ID = cursor.fetchall()
    if (Car_ID != []):
        Car_ID = Car_ID[0][0]
        query = "INSERT INTO customer VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        salt = create_salt()
        hash = hash_password(Password, salt)
        data = (Username, Car_ID, hash, salt, First_Name, Last_Name, Points, Birth_Date, City, Street_Name, Street_Number, Postal_Code, Family_Members, Email, Phone)
        cursor.execute(query, data)
        mydb.commit()
        return True
    else:
        return False

# verify username-password comination
# if combination is correct return true
# else if username does not exist or password is incorrect return false
def check_customer_login(Username, Password):
    query = "SELECT Salt FROM customer WHERE Username = %s;"
    data = (Username,)
    cursor.execute(query, data)
    result = cursor.fetchall()
    if (result == []):
        print("No such user")
        return False
    else:
        salt = bytes(result[0][0])
        candidate_hash = hash_password(Password, salt)
        query = "SELECT Password FROM customer WHERE Username = %s;"
        data = (Username,)
        cursor.execute(query, data)
        result = cursor.fetchall()
        real_hash = bytes(result[0][0])
        if (real_hash == candidate_hash):
            print("Correct Password")
            return True
        else:
            print("Wrong Password")
            return False


# return customers who have a contract with the company the given administrator works for
def admin_customers(Administrator_ID):
    query = "SELECT s.Customer_ID FROM administrator AS a JOIN subscription AS s ON a.Working_Company = s.Supplier_ID WHERE a.Administrator_No = %s;"
    data = (Administrator_ID,)
    cursor.execute(query, data)
    result = cursor.fetchall()
    results = []
    for i in result:
        results.append(i[0])
    return results

# delete customer from database given his Username
def delete_customer(Username):
    query = "DELETE FROM customer WHERE Username = %s;"
    data = (Username,)
    cursor.execute(query, data)
    mydb.commit()

def update_customer(Username, First_Name, Last_Name, Phone, Car_Brand, Car_Model, City, Street_Name, Street_Number, Postal_Code):
    query = "SELECT car_No FROM car WHERE brand = %s AND model = %s;"
    data = (Car_Brand, Car_Model)
    cursor.execute(query, data)
    result = cursor.fetchall()
    Car_ID = result[0][0]
    query = "UPDATE customer SET Car_ID = %s, First_Name = %s, Last_Name = %s, Phone = %s, City = %s, Street_Name = %s, Street_Number = %s, Postal_Code = %s WHERE Username = %s"
    data = (Car_ID, First_Name, Last_Name, Phone, City, Street_Name, Street_Number, Postal_Code, Username)
    cursor.execute(query, data)
    mydb.commit()

# change user's password
def change_customer_password(Username, Password_Old, Password_New):
    query = "SELECT Salt FROM customer WHERE Username = %s;"
    data = (Username,)
    cursor.execute(query, data)
    result = cursor.fetchall()
    if (result == []):
        return False
    else:
        salt = bytes(result[0][0])
        candidate_hash = hash_password(Password_Old, salt)
        query = "SELECT Password FROM customer WHERE Username = %s;"
        data = (Username,)
        cursor.execute(query, data)
        result = cursor.fetchall()
        real_hash = bytes(result[0][0])
        if (real_hash == candidate_hash):
            query = "UPDATE customer SET Password = %s WHERE Username = %s;"
            new_hash = hash_password(Password_New, salt)
            data = (new_hash, Username)
            cursor.execute(query, data)
            mydb.commit()
            return True
        else:
            return False

# insert energy producer into database
def insert_producer(Producer_Name, City = None, Street_Name = None, Street_Number = None, Postal_Code = None, Email = None, Phone = None):
    query = "INSERT INTO producer VALUES (%s, %s, %s, %s, %s, %s, %s);"
    data = (Producer_Name, City, Street_Name, Street_Number, Postal_Code, Email, Phone)
    cursor.execute(query, data)
    mydb.commit()

# delete energy producer given his Producer_Name
def delete_producer(Producer_Name):
    query = "DELETE FROM producer WHERE Producer_Name = %s;"
    data = (Producer_Name,)
    cursor.execute(query, data)
    mydb.commit()

# insert energy distributor into database
def insert_distributor(Distributor_Name, Producer_ID, KW_Price, Contract = None, City = None, Street_Name = None, Street_Number = None, Postal_Code = None, Email = None, Phone = None):
    query = "INSERT INTO distributor VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    data = (Distributor_Name, Producer_ID, KW_Price, Contract, City, Street_Name, Street_Number, Postal_Code, Email, Phone)
    cursor.execute(query, data)
    mydb.commit()

# delete energy distributor given his Distributor_Name
def delete_distributor(Distributor_Name):
    query = "DELETE FROM distributor WHERE Distributor_Name = %s;"
    data = (Distributor_Name,)
    cursor.execute(query, data)
    mydb.commit()

# insert boss in database
def insert_boss(Boss_No, Password, First_Name, Last_Name, Birth_Date, Working_Company, City = None, Street_Name = None, Street_Number = None, Postal_Code = None, Family_Members = None, Email = None, Phone = None):
    query = "INSERT INTO boss VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    salt = create_salt()
    hash = hash_password(Password, salt)
    data = (Boss_No, hash, salt, First_Name, Last_Name, Birth_Date, Working_Company, City, Street_Name, Street_Number, Postal_Code, Family_Members, Email, Phone)
    cursor.execute(query, data)
    mydb.commit()

# verify username-password comination for boss
# if combination is correct return true
# else if username does not exist or password is incorrect return false
def check_boss_login(Username, Password):
    query = "SELECT Salt FROM boss WHERE Boss_No = %s;"
    data = (Username,)
    cursor.execute(query, data)
    result = cursor.fetchall()
    if (result == []):
        print("No such user")
        return False
    else:
        salt = bytes(result[0][0])
        candidate_hash = hash_password(Password, salt)
        query = "SELECT Password FROM boss WHERE Boss_No = %s;"
        data = (Username,)
        cursor.execute(query, data)
        result = cursor.fetchall()
        real_hash = bytes(result[0][0])
        if (real_hash == candidate_hash):
            print("Correct Password")
            return True
        else:
            print("Wrong Password")
            return False

# change user's password
def change_boss_password(Username, Password_Old, Password_New):
    query = "SELECT Salt FROM boss WHERE Boss_No = %s;"
    data = (Username,)
    cursor.execute(query, data)
    result = cursor.fetchall()
    if (result == []):
        return False
    else:
        salt = bytes(result[0][0])
        candidate_hash = hash_password(Password_Old, salt)
        query = "SELECT Password FROM boss WHERE Boss_No = %s;"
        data = (Username,)
        cursor.execute(query, data)
        result = cursor.fetchall()
        real_hash = bytes(result[0][0])
        if (real_hash == candidate_hash):
            query = "UPDATE boss SET Password = %s WHERE Boss_No = %s;"
            new_hash = hash_password(Password_New, salt)
            data = (new_hash, Username)
            cursor.execute(query, data)
            mydb.commit()
            return True
        else:
            return False

# delete boss from database given his Boss_No
def delete_boss(Boss_No):
    query = "DELETE FROM boss WHERE Boss_No = %s;"
    data = (Boss_No,)
    cursor.execute(query, data)
    mydb.commit()

# insert administrator in database
def insert_administrator(Administrator_No, Password, First_Name, Last_Name, Birth_Year, Birth_Month, Birth_Day, Working_Company, City = None, Street_Name = None, Street_Number = None, Postal_Code = None, Family_Members = None, Email = None, Phone = None):
    query = "INSERT INTO administrator VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    Birth_Date = datetime.date(Birth_Year, Birth_Month, Birth_Day)
    salt = create_salt()
    hash = hash_password(Password, salt)
    data = (Administrator_No, hash, salt, First_Name, Last_Name, Birth_Date, Working_Company, City, Street_Name, Street_Number, Postal_Code, Family_Members, Email, Phone)
    cursor.execute(query, data)
    mydb.commit()

# verify username-password comination for boss
# if combination is correct return true
# else if username does not exist or password is incorrect return false
def check_administrator_login(Username, Password):
    query = "SELECT Salt FROM administrator WHERE Administrator_No = %s;"
    data = (Username,)
    cursor.execute(query, data)
    result = cursor.fetchall()
    if (result == []):
        print("No such user")
        return False
    else:
        salt = bytes(result[0][0])
        candidate_hash = hash_password(Password, salt)
        query = "SELECT Password FROM administrator WHERE Administrator_No = %s;"
        data = (Username,)
        cursor.execute(query, data)
        result = cursor.fetchall()
        real_hash = bytes(result[0][0])
        if (real_hash == candidate_hash):
            print("Correct Password")
            return True
        else:
            print("Wrong Password")
            return False

# change user's password
def change_administrator_password(Username, Password_Old, Password_New):
    query = "SELECT Salt FROM boss WHERE Administrator_No = %s;"
    data = (Username,)
    cursor.execute(query, data)
    result = cursor.fetchall()
    if (result == []):
        return False
    else:
        salt = bytes(result[0][0])
        candidate_hash = hash_password(Password_Old, salt)
        query = "SELECT Password FROM boss WHERE Administrator_No = %s;"
        data = (Username,)
        cursor.execute(query, data)
        result = cursor.fetchall()
        real_hash = bytes(result[0][0])
        if (real_hash == candidate_hash):
            query = "UPDATE boss SET Password = %s WHERE Administrator_No = %s;"
            new_hash = hash_password(Password_New, salt)
            data = (new_hash, Username)
            cursor.execute(query, data)
            mydb.commit()
        else:
            return False

# delete administrator from database given his Administrator_No
# UNSAFE!!! no checks - to be used only after checking credentials (used from delete_administrator)
def boss_delete_administrator(Administrator_No):
    query = "DELETE FROM administrator WHERE Administrator_No = %s;"
    data = (Administrator_No,)
    cursor.execute(query, data)
    mydb.commit()

# takes boss_id, boss_password and admin_id
# and deletes the admin if boss credentials are valid
# and if the admin exists and works for boss
def delete_administrator(Boss_ID, Boss_Password, Administrator_ID):
    if (not check_boss_login(Boss_ID, Boss_Password)):
        print("Invalid boss credentials")
        return 0
    else:
        query = "SELECT * FROM administrator WHERE Administrator_No = %s;"
        data = (Administrator_ID,)
        cursor.execute(query, data)
        result = cursor.fetchall()
        if (result == []):
            print("No administrator with this Username")
            return 1
        else:
            query = "SELECT * FROM boss AS b JOIN administrator AS a \
            ON b.Working_Company = a.Working_Company WHERE b.Boss_No = %s AND a.Administrator_No = %s;"
            data = (Boss_ID, Administrator_ID)
            cursor.execute(query, data)
            result = cursor.fetchall()
            if (result == []):
                print("This administrator does not work for this boss")
                return 2
            else:
                boss_delete_administrator(Administrator_ID)
                return 3

# return some info (Username, First_Name, Last_Name, Email, Phone) for
# every administrator working for this boss
def show_all_admins_on_company(Boss_ID):
    query = ("SELECT a.Administrator_No, a.First_Name, a.Last_Name, a.Email, a.Phone FROM boss AS b JOIN administrator AS a ON a.Working_Company = b.Working_Company\
    WHERE b.Boss_No = %s")
    data = (Boss_ID,)
    cursor.execute(query, data)
    result = cursor.fetchall()
    if (result == []):
        print("No results")
        return result
    else:
        print(result)
        return result

# insert charging station into database
def insert_station(Station_No, City, Street, Number, Operator):
    query = "INSERT INTO charging_station VALUES (%s, %s, %s, %s, %s);"
    data = (Station_No, City, Street, Number, Operator)
    cursor.execute(query, data)
    mydb.commit()

# delete charging station given its Station_No
def delete_station(Station_No):
    query = "DELETE FROM charging_station WHERE Station_No = %s;"
    data = (Station_No,)
    cursor.execute(query, data)
    mydb.commit()

# insert charging station's charging point into database
def insert_point(Point_No, Distributor_ID, Station_ID, Charging_Rate, Cost_per_KW):
    query = "INSERT INTO charging_point VALUES (%s, %s, %s, %s, %s);"
    data = (Point_No, Distributor_ID, Station_ID, Charging_Rate, Cost_per_KW)
    cursor.execute(query, data)
    mydb.commit()

# delete charging point given its Point_No
def delete_point(Point_No):
    query = "DELETE FROM charging_point WHERE Point_No = %s;"
    data = (Point_No,)
    cursor.execute(query, data)
    mydb.commit()

# insert contract/subscription in database
def insert_contract(Customer_ID, Supplier_ID):
    query = "SELECT Contract FROM distributor WHERE Distributor_Name = %s"
    data = (Supplier_ID,)
    cursor.execute(query, data)
    result = cursor.fetchall()
    if (result == []):
        print("No such distributor")
        return False
    if (result[0][0] == []):
        print("No contract available from this distributor")
        return False
    Price = result[0][0]
    query = "SELECT Username FROM customer WHERE Username = %s"
    data = (Customer_ID,)
    cursor.execute(query, data)
    result = cursor.fetchall()
    if (result == []):
        print("No such user")
        return False
    else:
        query = "SELECT * FROM subscription WHERE Customer_ID = %s;"
        data = (Customer_ID,)
        cursor.execute(query, data)
        result = cursor.fetchall()
        if (result == []):
            query = "INSERT INTO subscription (Customer_ID, Supplier_ID, Price, Last_paid, Last_issued) VALUES (%s, %s, %s, %s, %s);"
            data = (Customer_ID, Supplier_ID, Price, None, None)
            cursor.execute(query, data)
            mydb.commit()
            print("Insert ok")
            return True
        else:
            print("Error: User already has a contract")
            return False


def delete_contract(Administrator_ID, Contract_ID):
    query = "SELECT s.Subscription_No FROM administrator AS a JOIN subscription AS s ON a.Working_Company = s.Supplier_ID WHERE a.Administrator_No = %s AND s.Subscription_No = %s;"
    data = (Administrator_ID, Contract_ID)
    cursor.execute(query, data)
    result = cursor.fetchall()
    if (result == []):
        print("Administrator doesn't have this contract under his management")
        return False
    else:
        query = "DELETE FROM subscription WHERE Subscription_No = %s;"
        data = (Contract_ID,)
        cursor.execute(query, data)
        mydb.commit()
        print("Contract deleted successfully")
        return True


# delete contract/subscription from database
def delete_contract_unsafe(User_ID):
    query = "DELETE FROM subscription WHERE Customer_ID = %s;"
    data = (User_ID,)
    cursor.execute(query, data)
    mydb.commit()

# fetch customer's data given his username
def search_customer(Username):
    query = "SELECT c.Username, c.First_Name, c.Last_Name, c.Points, c.Birth_Date, c.City, c.Street_Name, c.Street_Number, c.Postal_Code, c.Family_Members, c.Email, c.Phone, \
    car.car_No, car.brand, car.model, car.capacitance FROM customer AS c JOIN car ON c.Car_ID = car.car_No WHERE Username = %s;"
    data = (Username,)
    cursor.execute(query, data)
    result = cursor.fetchall()
    #print(result)
    return result

# insert session details into database
def log_session(Customer_ID, Point_ID, Protocol, Type, Points, Date, Time_Start, Time_End, Amount, Energy):
    query = "INSERT INTO charging_session (Customer_ID, Point_ID, Protocol, Type, Points, Date, Start_Time, End_Time, Amount, Energy) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    data = (Customer_ID, Point_ID, Protocol, Type, Points, Date, Time_Start, Time_End, Amount, Energy)
    cursor.execute(query, data)
    mydb.commit()
    query = "SELECT Points FROM customer WHERE Username = %s;"
    data = (Customer_ID,)
    cursor.execute(query, data)
    result = cursor.fetchall()
    prev_points = result[0][0]
    new_points = prev_points + Points
    query = "UPDATE customer SET Points = %s WHERE Username = %s;"
    data = (new_points, Customer_ID)
    cursor.execute(query, data)
    mydb.commit()


def admin_sessions_per_station(Administrator_ID, Station_ID, Date_from, Date_to):
    query = "SELECT p.Point_No, s.Date, s.Start_Time, s.End_Time, s.Amount, s.Energy FROM administrator AS a JOIN charging_point AS p ON a.Working_Company = p.Distributor_ID JOIN charging_session as s ON p.Point_No = s.Point_ID\
    WHERE a.Administrator_No = %s and p.Station_ID = %s AND s.Date BETWEEN %s AND %s ORDER BY Date, Start_Time;"
    data = (Administrator_ID, Station_ID, Date_from, Date_to)
    cursor.execute(query, data)
    result = cursor.fetchall()
    return result

def admin_sessions_per_station_sum(Administrator_ID, Station_ID, Date_from, Date_to):
    query = "SELECT COUNT(s.Amount), SUM(s.Energy) FROM administrator AS a JOIN charging_point AS p ON a.Working_Company = p.Distributor_ID JOIN charging_session as s ON p.Point_No = s.Point_ID\
    WHERE a.Administrator_No = %s and p.Station_ID = %s AND s.Date BETWEEN %s AND %s;"
    data = (Administrator_ID, Station_ID, Date_from, Date_to)
    cursor.execute(query, data)
    result = cursor.fetchall()
    return result

# delete session log given its Session_No
def delete_session(Session_No):
    query = "DELETE FROM charging_session WHERE Session_No = %s;"
    data = (Session_No,)
    cursor.execute(query, data)
    mydb.commit()

# delete every session log
def clear_all_sessions():
    query = "SET SQL_SAFE_UPDATES = 0;"
    cursor.execute(query)
    mydb.commit()
    query = "DELETE FROM charging_session;"
    cursor.execute(query)
    mydb.commit()
    query = "SET SQL_SAFE_UPDATES = 1;"
    cursor.execute(query)
    mydb.commit()


# reset default superadmin with name 'admin' and password 'petrol4ever'
def reset_superadmin():
    query = "DELETE FROM superadmin WHERE Superadmin_ID = 'admin';"
    cursor.execute(query)
    mydb.commit()
    password = 'petrol4ever'
    salt = create_salt()
    hash = hash_password(password, salt)
    query = "INSERT INTO superadmin VALUES('admin',%s, %s,'Dimitris', 'Koulitakis', Null, Null);"
    data = (hash, salt)
    cursor.execute(query,data)
    mydb.commit()

# insert sessions from csv file specified from path variable
def sessions_csv(path):
    query = "set global local_infile=true;"
    cursor.execute(query)
    mydb.commit()
    query = "LOAD DATA LOCAL INFILE %s INTO TABLE charging_session FIELDS TERMINATED BY ',' ENCLOSED BY '\"'\
     LINES TERMINATED BY '\n' IGNORE 1 ROWS (Session_No, Customer_ID, Point_ID, Protocol, Type, Points, Date, Start_Time, End_Time, Amount, Energy);"
    data = (path,)
    cursor.execute(query, data)
    mydb.commit()

# verify username-password comination for superadmin
# if combination is correct return true
# else if username does not exist or password is incorrect return false
def check_superadmin_login(Username, Password):
    query = "SELECT Salt FROM superadmin WHERE Superadmin_ID = %s;"
    data = (Username,)
    cursor.execute(query, data)
    result = cursor.fetchall()
    if (result == []):
        return False
    else:
        salt = bytes(result[0][0])
        candidate_hash = hash_password(Password, salt)
        query = "SELECT Password FROM superadmin WHERE Superadmin_ID = %s;"
        data = (Username,)
        cursor.execute(query, data)
        result = cursor.fetchall()
        real_hash = bytes(result[0][0])
        if (real_hash == candidate_hash):
            return True
        else:
            return False

# change customer password without checking his old one
def customer_force_passw(Username, Password):
    query = "SELECT Salt FROM customer WHERE Username = %s;"
    data = (Username,)
    cursor.execute(query, data)
    result = cursor.fetchall()
    if (result == []):
        return False
    salt = bytes(result[0][0])
    new_hash = hash_password(Password, salt)
    query = "UPDATE customer SET Password = %s WHERE Username = %s;"
    data = (new_hash, Username)
    cursor.execute(query, data)
    mydb.commit()
    return True

# return all charging sessions for a charging point in a given time
def sessions_per_point(Point_ID, From_Year, From_Month, From_Day, To_Year, To_Month, To_Day):
    query = "SELECT * FROM charging_session WHERE Point_ID = %(Point_ID)s AND Date BETWEEN %(Date_from)s AND %(Date_to)s ORDER BY Date, Time;"
    data = {'Point_ID':Point_ID, 'Date_from':datetime.date(From_Year, From_Month, From_Day), 'Date_to':datetime.date(To_Year, To_Month, To_Day)}
    cursor.execute(query, data)
    result = cursor.fetchall()
    print(result)

# return all charging sessions for a charging station in a given time
def sessions_per_station(Station_ID, From_Year, From_Month, From_Day, To_Year, To_Month, To_Day):
    query = "SELECT * FROM charging_session as s JOIN charging_point as p ON s.Point_ID = p.Point_No WHERE p.Station_ID = " +\
    "%(p.Station_ID)s AND Date BETWEEN %(Date_from)s AND %(Date_to)s ORDER BY Date, Time;"
    data = {'p.Station_ID':Station_ID, 'Date_from':datetime.date(From_Year, From_Month, From_Day), 'Date_to':datetime.date(To_Year, To_Month, To_Day)}
    cursor.execute(query, data)
    result = cursor.fetchall()
    print(result)

# admin, point_id
# given an administrator and a point returns total count of charging sessions on this point
# and the total energy drawn in a time period if the point draws power from administrator's company
def admin_sessions_per_point_sum(Administrator_ID, Point_ID, Date_from, Date_to):
    query = "SELECT COUNT(*), SUM(s.Energy) FROM administrator AS a JOIN charging_point AS c ON a.Working_Company = c.Distributor_ID JOIN charging_session AS s ON s.Point_ID = c.Point_No\
    WHERE a.Administrator_No = %s AND c.Point_No = %s AND s.Date BETWEEN %s AND %s;"
    data = (Administrator_ID, Point_ID, Date_from, Date_to)
    cursor.execute(query, data)
    result = cursor.fetchall()
    return result

# session_id, datetime, cost, energy, payment_method, brand, model, capacitance
# given an administrator, a point and a time period (from date to date) returns each session's details
# for all sessions if the point draws power from administrator's company
# returns session_id, date, time, cost, energy(KWh), payment_method, car_brand, car_model, car_capacitance
def admin_sessions_per_point(Administrator_ID, Point_ID, Date_from, Date_to):
    query = "SELECT s.Session_No, s.Date, s.Start_Time, s.End_Time, s.Amount, s.Energy, s.Type, car.brand, car.model, car.capacitance FROM administrator AS a JOIN charging_point AS c ON a.Working_Company = c.Distributor_ID \
    JOIN charging_session AS s ON s.Point_ID = c.Point_No JOIN customer AS user ON s.Customer_ID = user.Username JOIN car ON user.Car_ID = car.Car_No\
    WHERE a.Administrator_No = %s AND c.Point_No = %s AND s.Date BETWEEN %s AND %s ORDER BY Date, Start_Time;"
    data = (Administrator_ID, Point_ID, Date_from, Date_to)
    cursor.execute(query, data)
    result = cursor.fetchall()
    return result

# get Point_ID, Point_Operator and number of sessions in that point in the dates between the given time period
# return empty list or list containing tuple
def superadmin_sessions_per_point_sum(Point_ID, Date_from, Date_to):
    query = "SELECT p.Point_No, st.Operator, COUNT(*) FROM charging_session AS s JOIN charging_point AS p ON s.Point_ID = p.Point_No JOIN charging_station AS st ON p.Station_ID = st.Station_No\
     WHERE s.Point_ID = %s AND s.Date BETWEEN %s and %s;"
    data = (Point_ID, Date_from, Date_to)
    cursor.execute(query, data)
    result = cursor.fetchall()
    return result

# list of tuples (session_no,date,start_time,end_time,protocol,energy,car_type)
def superadmin_sessions_per_point(Point_ID, Date_from, Date_to):
    query = "SELECT s.Session_No, s.Date, s.Start_Time, s.End_Time, s.Protocol, s.Energy, s.Type, car.Type FROM charging_session AS s JOIN customer AS c ON s.Customer_ID = c.Username\
    JOIN car ON c.Car_ID = car.car_No WHERE s.Point_ID = %s AND s.Date BETWEEN %s AND %s;"
    data = (Point_ID, Date_from, Date_to)
    cursor.execute(query, data)
    result = cursor.fetchall()
    return result

# get Station_ID, Station_Operator and number of sessions in that station in the dates between the given time period
# return empty list or list containing tuple
def superadmin_sessions_per_station_sum(Station_ID, Date_from, Date_to):
    query = "SELECT st.Station_No,st.Operator,SUM(s.Energy),COUNT(*),COUNT(DISTINCT s.Point_ID) FROM charging_session AS s JOIN charging_point AS p ON s.Point_ID = p.Point_No JOIN charging_station AS st ON p.Station_ID = st.Station_No\
     WHERE st.Station_No = %s AND s.Date BETWEEN %s and %s;"
    data = (Station_ID, Date_from, Date_to)
    cursor.execute(query, data)
    result = cursor.fetchall()
    return result


# list of tuples (point_id,#_of_sessions_in_point, total_energy_delivered_from_point) for each point in the station defined
def superadmin_sessions_per_station(Station_ID, Date_from, Date_to):
    query = "SELECT s.Point_ID, COUNT(s.Session_No), SUM(s.Energy) FROM charging_session AS s JOIN charging_point AS p ON s.Point_ID = p.Point_No \
    WHERE p.Station_ID = %s  AND s.Date BETWEEN %s AND %s GROUP BY p.Point_No;"
    data = (Station_ID, Date_from, Date_to)
    cursor.execute(query, data)
    result = cursor.fetchall()
    return result


# return all user charging sessions for a charging station in a given month
def user_sessions_per_date(Username, From_Date, To_Date):
    query = "SELECT Date, Amount FROM charging_session WHERE Customer_ID = %s AND (Date BETWEEN %s AND %s) ORDER BY Date, Start_Time;"
    data = (Username, From_Date, To_Date)
    cursor.execute(query, data)
    result = cursor.fetchall()
    return result

# return all user charging sessions for a charging station in a given station
def user_sessions_per_station(Username, Station_ID, From_Date, To_Date):
    query = "SELECT Date, Amount FROM charging_session as s JOIN charging_point as p ON s.Point_ID = p.Point_No WHERE s.Customer_ID = %s AND p.Station_ID = \
    %s AND (Date BETWEEN %s AND %s ) ORDER BY Date, Start_Time;"
    data = (Username, Station_ID, From_Date, To_Date)
    cursor.execute(query, data)
    result = cursor.fetchall()
    return result

# return all user charging sessions for a charging station in a given distributor
def user_sessions_per_distributor(Username, Distributor_ID, From_Year, From_Month, From_Day, To_Year, To_Month, To_Day):
    query = "SELECT * FROM charging_sessions as ses JOIN charging_point as p on ses.Point_ID = p.Point_No WHERE ses.Customer_ID = %s\
    AND p.Distributor_ID = %s AND (Date BETWEEN %(Date_from)s AND %(Date_to)s ) ORDER BY Date, Time;"
    data = (Username, Distributor_ID, datetime.date(From_Year, From_Month, From_Day), datetime.date(To_Year, To_Month, To_Day))
    cursor.execute(query, data)
    result = cursor.fetchall()
    return result

# return all charging sessions for a vehicle
def superadmin_sessions_per_EV_sum(Car_ID, Date_from, Date_to):
    query = "SELECT car.car_No, SUM(s.Energy), COUNT(DISTINCT s.Point_ID), COUNT(*) FROM car JOIN customer AS c ON car.car_No = c.Car_ID JOIN charging_session AS s ON s.Customer_ID = c.Username \
    WHERE car.car_No = %s AND s.Date BETWEEN %s AND %s;"
    data = (Car_ID,Date_from,Date_to)
    cursor.execute(query, data)
    result = cursor.fetchall()
    return result

def superadmin_sessions_per_EV(Car_ID,Date_from,Date_to):
    query = "SELECT s.Session_No, p.Distributor_ID, s.Date, s.Start_Time, s.End_Time, s.Energy, s.Type, p.Cost_per_KWh, s.Amount FROM charging_session AS s\
    JOIN charging_point AS p ON s.Point_ID = p.Point_No JOIN customer AS c ON c.Username = s.Customer_ID WHERE c.Car_ID = %s AND s.Date BETWEEN %s AND %s;"
    data = (Car_ID,Date_from,Date_to)
    cursor.execute(query, data)
    result = cursor.fetchall()
    return result


# return all charging sessions for a provider
# returns list of tuples (Distributor_ID, Station_ID, Session_No, Car_ID, Date, Start_Time, End_Time, Energy_Drawn, Payment_Type, Cost_per_KWh, Session_Cost)
def superadmin_sessions_per_provider(Distributor_Name, Date_from, Date_to):
    query = "SELECT p.Distributor_ID, p.Station_ID, s.Session_No, c.Car_ID, s.Date, s.Start_Time, s.End_Time, s.Energy, s.Type, p.Cost_per_KWh, s.Amount\
     FROM charging_session AS s JOIN charging_point AS p ON s.Point_ID = p.Point_No JOIN customer AS c ON c.Username = s.Customer_ID WHERE\
     p.Distributor_ID = %s AND s.Date BETWEEN %s AND %s;"
    data = (Distributor_Name, Date_from, Date_to)
    cursor.execute(query, data)
    result = cursor.fetchall()
    return result



def sessions_per_admin(Administrator_ID, Date_from, Date_to):
    query = "SELECT p.Station_ID, s.Session_No, c.Car_ID, s.Date, s.Start_Time, s.End_Time, s.Energy, p.Cost_per_KWh, s.Amount FROM administrator AS a JOIN charging_point AS p ON a.Working_Company = p.Distributor_ID\
    JOIN charging_session as s ON s.Point_ID = p.Point_No JOIN customer AS c ON c.Username = s.Customer_ID WHERE a.Administrator_No = %s AND ( s.Date BETWEEN %s AND %s)  ORDER BY Date, Start_Time;"
    data = (Administrator_ID, Date_from, Date_to)
    cursor.execute(query, data)
    result = cursor.fetchall()
    return result

def admin_info(Administrator_ID):
    query = "SELECT Administrator_No, First_Name, Last_Name, Birth_Date, Working_Company, City, Street_Name, Street_Number, Postal_Code, Email, Phone FROM administrator WHERE Administrator_No = %s;"
    data = (Administrator_ID,)
    cursor.execute(query, data)
    result = cursor.fetchall()
    print(result)
    return result


def findall_points_admin(Administrator_ID):
    query = "SELECT Working_Company FROM administrator WHERE Administrator_No = %s;"
    data = (Administrator_ID,)
    cursor.execute(query, data)
    result = cursor.fetchall()
    if (result != []):
        result = findall_points_distributor(result[0][0])
    return result

def findall_points_admin_station(Administrator_ID, Station_No):
    query = "SELECT Working_Company FROM administrator WHERE Administrator_No = %s;"
    data = (Administrator_ID,)
    cursor.execute(query, data)
    distributor = cursor.fetchall()
    if (distributor != []):
        query = "SELECT * FROM charging_point WHERE Distributor_ID = %s AND Station_ID = %s;"
        data = (distributor[0][0], Station_No)
        cursor.execute(query, data)
        result = cursor.fetchall()
    else:
        result = []
    return result

def check_if_admin(Administrator_ID):
    query = "SELECT Administrator_No FROM administrator WHERE Administrator_No = %s;"
    data = (Administrator_ID,)
    cursor.execute(query, data)
    fetch = cursor.fetchall()
    print(fetch)
    if (fetch != []):
        result = True
    else:
        result = False
    print(result)
    return result

def check_if_customer(User_ID):
    query = "SELECT Username FROM customer WHERE Username = %s;"
    data = (User_ID,)
    cursor.execute(query, data)
    fetch = cursor.fetchall()
    if (fetch != []):
        result = True
    else:
        result = False
    return result

def findall_points_distributor(Distributor_ID):
    query = "SELECT * FROM charging_point WHERE Distributor_ID = %s;"
    data = (Distributor_ID,)
    cursor.execute(query, data)
    result = cursor.fetchall()
    return result

# return cost for a certain time, vehicle and charging point
# input is current battery percentage, time to charge, car_id and point_no
# returns (cost, time, energy, points)
# input is current battery percentage, time to charge, car_id and point_no
def time_cost(Percentage, Time, Car_ID, Point_No):
    query = "SELECT capacitance FROM car WHERE car_No = %s;"
    data = (Car_ID,)
    cursor.execute(query, data)
    total_capacity = cursor.fetchall()
    if (total_capacity == []):
        return -1
    total_capacity = float(total_capacity[0][0])
    battery_uncharged = (100-Percentage)/100*total_capacity
    query = "SELECT Charging_Rate, Cost_per_KWh FROM charging_point WHERE Point_No = %s;"
    data = (Point_No,)
    cursor.execute(query, data)
    result = cursor.fetchall()
    if (result == []):
        return -1
    charging_rate = float(result[0][0])
    cost_per_kwh = float(result[0][1])
    if (Time*charging_rate > battery_uncharged):
        return (format(round(battery_uncharged*cost_per_kwh, 2), '.2f'), int(battery_uncharged/charging_rate), battery_uncharged, int(battery_uncharged*10))
    else:
        return (format(round(Time*charging_rate*cost_per_kwh, 2), '.2f'), Time, Time*charging_rate, int(Time*charging_rate*10))


# return cost for a certain battery percentage goal, vehicle and charging point
# args: car_id(serial no), point_id, current_battery_percentage, goal_battery_percentage
# on success returns (cost, time, energy, points)
# on failure returns -1
def percentage_cost(Car_ID, Point_No, Start_Percentage, End_Percentage):
    query = "SELECT capacitance FROM car WHERE car_No = %s;"
    data = (Car_ID,)
    cursor.execute(query, data)
    total_capacity = cursor.fetchall()
    if (total_capacity == [] or End_Percentage <= Start_Percentage or End_Percentage <= 0 or Start_Percentage<0):
        return -1
    total_capacity = float(total_capacity[0][0])
    to_charge = (End_Percentage-Start_Percentage)/100*total_capacity
    query = "SELECT Charging_Rate, Cost_per_KWh FROM charging_point WHERE Point_No = %s;"
    data = (Point_No,)
    cursor.execute(query, data)
    result = cursor.fetchall()
    if (result == []):
        return -1
    charging_rate = float(result[0][0])
    cost_per_kwh = float(result[0][1])
    cost = format(round(to_charge*cost_per_kwh, 2), '.2f')
    time = round(to_charge/charging_rate,0)
    return (cost, int(time), format(round(to_charge,2),'.2f'), int(to_charge*10))


def issue_bill(Administrator_No, User_ID, Date):
    query = "SELECT s.Customer_ID FROM administrator AS a JOIN subscription as s ON a.Working_Company = s.Supplier_ID WHERE a.Administrator_No = %s AND s.Customer_ID = %s;"
    data = (Administrator_No,User_ID)
    cursor.execute(query, data)
    result = cursor.fetchall()
    if (result == []):
        return False
    else:

        query = "UPDATE subscription SET Last_issued = %s WHERE Customer_ID = %s;"
        data = (Date, User_ID)
        cursor.execute(query, data)
        mydb.commit()
        return True


def pay_bill(User_ID, Date):
  query = "SELECT Username FROM customer WHERE Username = %s;"
  data = (User_ID,)
  cursor.execute(query, data)
  result = cursor.fetchall()
  if (result == []):
    print("No such user")
    return False
  else:
    query = "SELECT Customer_ID FROM subscription WHERE Customer_ID = %s;"
    data = (User_ID,)
    cursor.execute(query, data)
    result = cursor.fetchall()
    if (result == []):
      print("User doesn't have a contract")
      return False
    else:
      query = "UPDATE subscription SET Last_paid = %s WHERE Customer_ID = %s;"
      data = (Date, User_ID)
      cursor.execute(query, data)
      mydb.commit()
      return True

# return subscription details for a customer
def contract_details_user(Username):
    query = "SELECT Supplier_ID, Price FROM subscription WHERE Customer_ID = %(Username)s;"
    data = {'Username':Username}
    cursor.execute(query, data)
    result = cursor.fetchall()
    return result

# return all contracts made with an energy provider
def contract_details_provider(Administrator_ID):
    query = "SELECT c.Username, c.First_Name, c.Last_Name, c.Email, c.City, c.Street_Name, c.Street_Number, c.Postal_Code, c.Phone, c.Points, s.Last_paid, s.Last_issued, s.Price FROM administrator AS a JOIN subscription AS s ON a.Working_Company = s.Supplier_ID JOIN customer AS c ON s.Customer_ID = c.Username\
    WHERE a.Administrator_No = %s;"
    data = (Administrator_ID,)
    cursor.execute(query, data)
    result = cursor.fetchall()
    return result

# return all contracts made with an energy provider
def contract_details_of_user(Administrator_ID,Customer_ID):
    query = "SELECT c.Username, c.First_Name, c.Last_Name, c.Email, c.City, c.Street_Name, c.Street_Number, c.Postal_Code, c.Phone, c.Points, s.Last_paid, s.Last_issued, s.Price FROM administrator AS a JOIN subscription AS s ON a.Working_Company = s.Supplier_ID JOIN customer AS c ON s.Customer_ID = c.Username\
    WHERE a.Administrator_No = %s AND c.Username = %s;"
    data = (Administrator_ID,Customer_ID)
    cursor.execute(query, data)
    result = cursor.fetchall()
    return result
# return all available contracts for the customer to choose
# return type: list of tuples(distributor, price)
def contracts_available():
    query = "SELECT Distributor_Name, Contract, Email, Phone FROM distributor;"
    cursor.execute(query)
    result = cursor.fetchall()
    return result

# return all available charging points
def findall_points():
    query = "SELECT * FROM charging_point"
    cursor.execute(query)
    result = cursor.fetchall()
    return result

# return all available charging stations
def findall_stations():
    query = "SELECT * FROM charging_station"
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def findall_cars():
  query = "SELECT * FROM car"
  cursor.execute(query)
  result = cursor.fetchall()
  return result

# return every car brand once
# returns a list of strings
def find_brands():
    query = "SELECT DISTINCT brand FROM car;"
    cursor.execute(query)
    temp = cursor.fetchall()
    result = []
    for i in range(len(temp)):
        result.append(temp[i][0])
    return result

# return every model for a given brand
# return value is [] if no such brand is in the database
# or a list of strings if there is
def find_brand_models(Brand):
    query = "SELECT DISTINCT model FROM car WHERE brand = %s;"
    data = (Brand,)
    cursor.execute(query, data)
    temp = cursor.fetchall()
    result = []
    for i in range(len(temp)):
        result.append(temp[i][0])
    return result


# check if customer has contract with company the admin works for
def customer_admin_company(Administrator_No, User_ID):
    query = "SELECT s.Customer_ID FROM subscription AS s JOIN administrator AS a ON s.Supplier_ID = a.Working_Company WHERE a.Administrator_No = %s AND s.Customer_ID = %s;"
    data = (Administrator_No, User_ID)
    cursor.execute(query, data)
    result = cursor.fetchall()
    if (result == []):
        return False
    else:
        return True
