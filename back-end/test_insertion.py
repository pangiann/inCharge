import os
import hashlib
import mysql.connector
import datetime
import random

# establish connection with database
mydb = mysql.connector.connect(
    user="root",
    password="42DataBase42",
    database="sql_inCharge",
    host="127.0.0.1",
    port="3306",
    auth_plugin='mysql_native_password',
    use_pure='True'
)
cursor = mydb.cursor()

query = "SET SQL_SAFE_UPDATES = 0;"
cursor.execute(query)
mydb.commit()

# hash plaintext password with salt and return value
def hash_password(password, salt):
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return key

# return random 32 byte value to be used as salt for user
def create_salt():
    salt = os.urandom(32)
    return salt

def random_line(file):
    lines = open(file).read().splitlines()
    myline =random.choice(lines)
    return myline

def random_date():
    start_date = datetime.date(2019, 1, 1)
    end_date = datetime.date(2021, 2, 27)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date

def random_birth_date():
    start_date = datetime.date(1960, 1, 1)
    end_date = datetime.date(2000, 12, 31)

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

#####     superadmin     #####
def insert_superadmin(Superadmin_ID, Password, First_Name, Last_Name, Email = None, Phone = None):
    query = "INSERT INTO superadmin VALUES (%s, %s, %s, %s, %s, %s, %s);"
    salt = create_salt()
    hash = hash_password(Password, salt)
    data = (Superadmin_ID, hash, salt, First_Name, Last_Name, Email, Phone)
    cursor.execute(query, data)
    mydb.commit()

def delete_superadmin():
    query = "DELETE FROM superadmin;"
    cursor.execute(query)
    mydb.commit()

delete_superadmin()
insert_superadmin('admin','petrol4ever','Dimitris','Koulitakis')
insert_superadmin('equus_sapiens','muffins','Bojack','Horseman')
insert_superadmin('gustav','hokeypokey','Todd','Chavez')
insert_superadmin('crossover','saddog','Mr.','Peanutbutter')

#####     boss     #####
def insert_boss(Boss_No, Password, First_Name, Last_Name, Birth_Year, Birth_Month, Birth_Day, Working_Company, City = None, Street_Name = None, Street_Number = None, Postal_Code = None, Family_Members = None, Email = None, Phone = None):
    query = "INSERT INTO boss VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    salt = create_salt()
    hash = hash_password(Password, salt)
    Birth_Date = datetime.date(Birth_Year, Birth_Month, Birth_Day)
    data = (Boss_No, hash, salt, First_Name, Last_Name, Birth_Date, Working_Company, City, Street_Name, Street_Number, Postal_Code, Family_Members, Email, Phone)
    cursor.execute(query, data)
    mydb.commit()

def delete_boss():
    query = "DELETE FROM boss;"
    cursor.execute(query)
    mydb.commit()

delete_boss()

insert_boss('DEDDIE_boss1','o-kwdikos-mou-123','Mixahl','Vasiliou',1976,8,29,'DEDDIE','Athens','Monodendri',1,12345,'Five','michvas@gmail.com',6942136589);
insert_boss('DEDDIE_boss2','geia_sou_mastora_12','Iwannis','Nikolaou',1956,2,15,'DEDDIE','Athens','Harilaou Trikoupi',5,17364,'Three','gianonikolaou@gmail.com',69362746352);
insert_boss('Protergia_boss1','password-password-1199','Petros','Georgiou',1963,7,19,'Protergia','Athens','Parou',8,21832,'Four','geopetr@gmail.com',69123456543);
insert_boss('Protergia_boss2','mhn_me_hackarete_plzzz','Vasileios','Iwannou',1971,8,3,'Protergia','Athens','Polunisidwn',12,12323,'Four','vasiwoannou@gmail.com',6900928374);
insert_boss('WATT+VOLT_boss1','den_kserw_ti_na_gra4w','Simeon','Karageorgiou',1968,11,21,'WATT+VOLT','Athens','Kritis',15,11123,'Five','simeontherealg@gmail.com',6900012372);
insert_boss('WATT+VOLT_boss2','me_lene_petro_1212','Petros','Fotopoulos',1959,3,21,'WATT+VOLT','Athens','Panagi Tsaldari',21,12334,'Five','fotopoulakos@gmail.com',6903748572);
insert_boss('Volterra_AE_boss1','geia-eimai-o-alexandros-00','Iwanna','Papanikolaou',1971,8,30,'Volterra AE','Athens','Melinas Merkouri',31,17645,'Four','papanikolaouuu@gamil.com',6901928374);
insert_boss('ELPEDISON_boss1','elpedison_4_ever','Vasiliki','Karanikoli',1979,9,17,'ELPEDISON','Athens','Themistokleous',12,18882,'Two','vasivasi@gmail.com',6912345678);
insert_boss('Volton_boss1','i-work-4-volton','Panagiotis','Papaswtiriou',1980,4,15,'Volton','Athens','Demirdesiou',18,16623,'Three','papaswtirakis@gmail.com',6909876543);
insert_boss('ZeniΘ_boss1','giannakis-gia-3-mesa!!!','Panagiotis','Giannakis',1981,11,13,'ZeniΘ','Athens','Kolokotroni',53,22148,'Four','iwontheeuropeancup@gmail.com',6934567890);
insert_boss('PROMETHEUS_GAS_boss1','who-is-the-bo$$','Georgios','Pestouridis',1978,5,28,'PROMETHEUS GAS','Athens','Eutuxias',46,12449,'Four','pastouridis@gmail.com',6909871234);

#####     admin     #####
def insert_administrator(Administrator_No, Password, First_Name, Last_Name, Birth_Year, Birth_Month, Birth_Day, Working_Company, City = None, Street_Name = None, Street_Number = None, Postal_Code = None, Family_Members = None, Email = None, Phone = None):
    query = "INSERT INTO administrator VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    Birth_Date = datetime.date(Birth_Year, Birth_Month, Birth_Day)
    salt = create_salt()
    hash = hash_password(Password, salt)
    data = (Administrator_No, hash, salt, First_Name, Last_Name, Birth_Date, Working_Company, City, Street_Name, Street_Number, Postal_Code, Family_Members, Email, Phone)
    cursor.execute(query, data)
    mydb.commit()

def delete_administrator():
    query = "DELETE FROM administrator;"
    cursor.execute(query)
    mydb.commit()

delete_administrator()

insert_administrator('DEDDIE_admin1','deddie_admin_1_pass','Iwannis','Papapetrou',1987,1,23,'DEDDIE','Athens','Rodou',43,12567,'Two','papapetrou@gmail.com',6910101010)
insert_administrator('DEDDIE_admin2','deddie_admin_2_pass','Nikolaos','Vasileiou',1988,9,11,'DEDDIE','Athens','Karaiskaki',55,43112,'Three','vasilakisnick@gmail.com',6903939394)
insert_administrator('Protergia_admin1','protergia_admin_1_pass','Kwnstantinos','Georgiou',1990,7,29,'Protergia','Athens','Kokovenou',27,11543,'Two','kwstakwsta@gmail.com',6902029292)
insert_administrator('Protergia_admin2','protergia_admin_2_pass','Vasileios','Amorgakis',1988,2,28,'Protergia','Athens','Peristeriou',2,11236,'One','amorgakisvas@gmail.com',6957574848)
insert_administrator('WATT+VOLT_admin1','watt+volt_admin_1_pass','Nikoleta','Apostolopoulou',1989,7,21,'WATT+VOLT','Athens','Leontos',8,16532,None,'nikoletaapo@gmail.com',6902030405)
insert_administrator('WATT+VOLT_admin2','watt+volt_admin_2_pass','Eleni','Hatzitheodorou',1982,11,8,'WATT+VOLT','Athens','Mpoumpoulinas',11,19876,'Three','elenihatzi@gmail.com',6992939495)
insert_administrator('Volterra_AE_admin1','volterra_admin_1_pass','Periklis','Kostantakis',1985,3,8,'Volterra AE','Athens','Kifisou',16,11726,'Four','periklaksi@gmail.com',6981828384)
insert_administrator('ELPEDISON_admin1','elpedison_admin_1_pass','Georgios','Miralidis',1983,3,19,'ELPEDISON','Athens','Leukaditou',73,17364,'Two','miralidisgeorge@gmail.com',6987868584)
insert_administrator('Volton_admin1','volton_admin_1_pass','Evaggelia','Theodorou',1986,5,18,'Volton','Athens','Sofokleous',56,19876,None,'evatheo@gmail.com',6971727374)
insert_administrator('ZeniΘ_admin1','zenith_admin_1_pass','Paraskeui','Vaskoura',1993,4,17,'ZeniΘ','Thessaloniki','Irodotou',12,11264,'Three','paraskeuoulavask@gmail.com',6942535251)
insert_administrator('PROMETHEUS_GAS_admin1','prometheus_admin_1_pass','Panagiotis','Kokoveos',1994,6,26,'PROMETHEUS GAS','Athens','Aristotelous',25,19337,'Three','pankoko@gmail.com',6926262524)

#####     customer     #####
def find_cars():
    query = "SELECT brand, model FROM car"
    cursor.execute(query)
    result = cursor.fetchall()
    cars = []
    for i in range(len(result)):
        cars.append((result[i][0], result[i][1]))
    return cars



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



def delete_customer():
    query = "DELETE FROM customer;"
    cursor.execute(query)
    mydb.commit()

delete_customer()


insert_customer('michalakos', 'Tesla', 'Model 3', 'JLKFjdlsa#*uy', 'Michalis', 'Vasilakos', '1999-10-01', 0, 'Athens', 'Ath.Diakou', 1, 19324, None, 'michalis@gmail.com', 6969341254)
insert_customer('pangiann', 'Tesla', 'Model 3', 'fjdaslO*UEowf0)', 'Panagiotis', 'Giannoulis', '1999-07-03', 0, 'Athens', 'Karaiskaki', 12, 11432, None, 'panagiotis@gmail.com', 6987654387)
insert_customer('Pantelis_G', 'Tesla', 'Model 3', 'kfsaJ)(*UFEosaf*&*&(', 'Pantelis', 'Gavalas', '1999-06-13', 0, 'Athens', 'Mpoumpoulinas', 45, 12054, None, 'pantelis@gmail.com', 6929349087)
insert_customer('geosotos', 'Tesla', 'Model S', 'fajsl*OUfoH()E*gfsfa', 'Giwrgos', 'Swthriou', '1999-11-19', 0, 'Athens', 'Miaouli', 76, 65812, None, 'giwrgos@gmail.com', 6987320912)
insert_customer('vintere', 'Volvo', 'XC 60 T8', '809FJd0wejfg8ajgrew09rjfga', 'Karina', 'Emporou', '2000-02-22', 0, 'Athens', 'Papaflessa', 121, 23189, None, 'mastoras@ntua.gr', 6987654309)
insert_customer('vasoulis', 'Audi', 'A3 40 e-tron', 'saysaysaysaythepassword', 'Vasilis', 'Ntounis', '2001-08-12', 0, 'Athens', 'K.Kanari', 101, 12432, None, 'kastoras@ntua.gr', 6990906745)
insert_customer('17spyros42', 'Opel', 'Corsa-e', 'SAGAPO_S-A-G-A-P-O', 'Spyros', 'Kaskolewn', '1970-08-09', 0, 'Athens', 'Filikis Etairias', 98, 12321, None, 'pastoras@ntua.gr', 6921324343)
insert_customer('trigonopsaroulis', 'Porsche', 'Taycan', 'ajsfgloisf4#$)QFj0)FJfdsaf', 'Stathon', 'Aspgomali', '1982-04-28', 0, 'Athens', 'Skoufa', 17, 12321, None, 'bob@hotmail.com', 6989894323)
insert_customer('froutotrela', 'Honda', 'e', '98nfvsan9*HJgagadf', 'Mpampinos', 'Kaskoleas', '1987-05-17', 0, 'Athens', 'Tsakalwf', 42, 12121, None, 'dod@hotmail.com', 6978433289)
insert_customer('nikolakisXD', 'Volkswagen', 'e-Golf', 'jfdas0jj0Jfd0qwjfgWJF098WJGFWE', 'Nikolas', 'Tsimpoukas', '1995-04-30', 0, 'Athens', 'Ksanthou', 45, 12653, None, 'joj@hotmail.com', 6932128943)
insert_customer('kosmolagnos', 'BMW', 'X5', 'paosdkjforhw249dfaw', 'Kosmas', 'Mperdos', '1975-04-14', 0, 'Athens', 'Mpotsari', 12, 12431, None, 'kosmas@gmail.com', 6969696969)
insert_customer('dragonball', 'Peugeot', '3008', 'LIG890eatrJO8ERPF*0gfd', 'Christos', 'Drakopoulos', '1972-11-04', 0, 'Athens', 'Kolokotroni', 112, 10431, None, 'drakopoulos@gmail.com', 6991756969)

car_list = find_cars()
cities = ['Athens', 'Thessaloniki', 'Patra', 'Iwannina', 'Volos', 'Trikala', 'Korinthos', 'Rethymno', 'Hrakleio', 'Ksanthi', 'Komotini', 'Larissa']

for i in range(500):
    car_no = random.randint(0,len(car_list)-1)
    sex = random.randint(0,1)
    username = random_line('usernames.txt')
    if (sex):
        try:
            insert_customer(username, car_list[car_no][0], car_list[car_no][1], random_line('passwords.txt'), random_line('greek_women_names.txt'),\
             random_line('greek_women_surnames.txt'), random_birth_date(), 0, cities[random.randint(0,len(cities)-1)], random_line('street_names.txt'), random.randint(1,150),\
             random.randint(10000, 19999), None, username+'@gmail.com', random.randint(6900000000, 6999999999))
        except:
            pass
    else:
        try:
            insert_customer(username, car_list[car_no][0], car_list[car_no][1], random_line('passwords.txt'), random_line('greek_men_names.txt'),\
             random_line('greek_men_surnames.txt'), random_birth_date(), 0, cities[random.randint(0,len(cities)-1)], random_line('street_names.txt'), random.randint(1,150),\
             random.randint(10000, 19999), None, username+'@gmail.com', random.randint(6900000000, 6999999999))
        except:
            pass


#####     contract     #####
def insert_contract(Customer_ID, Supplier_ID):
    query = "SELECT Contract FROM distributor WHERE Distributor_Name = %s"
    data = (Supplier_ID,)
    cursor.execute(query, data)
    result = cursor.fetchall()
    if (result == []):
        return False
    if (result[0][0] == []):
        return False
    Price = result[0][0]
    query = "SELECT Username FROM customer WHERE Username = %s"
    data = (Customer_ID,)
    cursor.execute(query, data)
    result = cursor.fetchall()
    if (result == []):
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
            return True
        else:
            return False

def delete_contract_unsafe():
    query = "DELETE FROM subscription;"
    cursor.execute(query)
    mydb.commit()

def find_users():
    query = "SELECT Username FROM customer"
    cursor.execute(query)
    result = cursor.fetchall()
    users = []
    for i in range(len(result)):
        users.append(result[i][0])
    return users

def find_distributors():
    query = "SELECT Distributor_Name FROM distributor"
    cursor.execute(query)
    result = cursor.fetchall()
    distributors = []
    for i in range(len(result)):
        distributors.append(result[i][0])
    return distributors

delete_contract_unsafe()

insert_contract('michalakos', 'DEDDIE')
insert_contract('pangiann', 'ELPEDISON')
insert_contract('Pantelis_G', 'Volterra AE')
insert_contract('geosotos', 'Volton')

users = find_users()
distributors = find_distributors()
for i in range(int(len(users)/2)):
    insert_contract(users[random.randint(0,len(users)-1)], distributors[random.randint(0,len(distributors)-1)])

#####     session     #####
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

user_list = find_users()
points_list = find_points()
type_list = ['Card', 'Contract']
protocol = ['High', 'Medium', 'Low']

for i in range(50000):
    log_session(user_list[random.randint(0,len(user_list)-1)], points_list[random.randint(0,len(points_list)-1)], protocol[random.randint(0,len(protocol)-1)], type_list[random.randint(0,len(type_list)-1)], random.randint(0,100), random_date(), random_time(), random_time(), random_price(), random_energy())

query = "SET SQL_SAFE_UPDATES = 1;"
cursor.execute(query)
mydb.commit()
