from api import app
import unittest
import requests
import urllib
import pprint
import json
import ast


from requests.structures import CaseInsensitiveDict
headers = CaseInsensitiveDict()

class ApiTest(unittest.TestCase):
    
    def test_user_create(self):
        url = "evcharge/api/user/create"
        payload = {'username' : 'd6', 
                    'password' : '123456',
                    'birth_date' : '1999-08-04',
                    'email' : 'geo@gmail.com',
                    'first_name' : 'Geo',
                    'last_name' : 'Sot',
                    'phone' : '2109311111',
                    'car_brand' : 'Tesla',
                    'car_model' : 'Model X',
                    'city' : 'Athens',
                    'street_name' : 'Metron',
                    'street_number' : '11',
                    'postal_code' : '12345'}
        
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        tester = app.test_client(self)
        response = tester.post(url, headers=headers, data=payload)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(mydata['msg'], 'User created successfully')
    
    def test_user_create_error(self):
        url = "evcharge/api/user/create"
        tester = app.test_client(self)
        response = tester.post(url)
        #pprint.pprint(response)
        self.assertNotEqual(response.status_code, 200)
    

    def test_user_login(self):
        tester = app.test_client(self)
        response = tester.post('evcharge/api/user/login', data=dict(username="geotest", password="123456"))
        #print(response.data)
        self.assertEqual(response.status_code, 200)

    def test_user_login_error(self):
        url = "evcharge/api/user/login"
        payload = {'username' : 'michalakos', 'password' : 'wrong'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        tester = app.test_client(self)
        response = tester.post(url, headers=headers, data=payload)
        #pprint.pprint(response)
        self.assertNotEqual(response.status_code, 200)

    def test_user_chpwd(self):
        url = "evcharge/api/user/d1/chpwd"
        payload = { 'old_password' : '123456',
                    'new_password' : '1234567'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        tester = app.test_client(self)
        response = tester.put(url, headers=headers, data=payload)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(mydata['msg'], 'Password updated successfully')

    def test_user_get(self):
        url = "evcharge/api/user/login"
        payload = {'username' : 'geotest3', 'password' : '123456'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        tester = app.test_client(self)
        response = tester.post(url, headers=headers, data=payload)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        
        url = "evcharge/api/user/geotest3"
        tester = app.test_client(self)
        headers['Authorization'] = 'Bearer ' + mydata['token']
        response = tester.get(url, headers=headers)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        #print(mydata)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(mydata['msg'], 'Got user profile info successfully')
    
    def test_user_delete(self):
        url = "evcharge/api/user/login"
        payload = {'username' : 'geo3', 'password' : '123456'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        tester = app.test_client(self)
        response = tester.post(url, headers=headers, data=payload)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        
        url = "evcharge/api/user/geo3"
        payload = {'password' : '123456'}
        payload = urllib.parse.urlencode(payload)
        tester = app.test_client(self)
        headers['Authorization'] = 'Bearer ' + mydata['token']
        response = tester.delete(url, headers=headers, data=payload)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        #pprint.pprint(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(mydata['msg'], 'User deleted successfully')


    def test_user_update(self):
        '''
        url = "evcharge/api/user/login"
        payload = {'username' : 'geotest', 'password' : '123456'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        tester = app.test_client(self)
        response = tester.post(url, headers=headers, data=payload)
        response = response.json
        mydata = response
        '''

        url = "evcharge/api/user/geotest"
        payload = { "first_name" : "Geo_changed",
                    "last_name" : "Sot_changed",
                    "phone" : 2109322222,
                    "car_brand" : "BMW",
                    "car_model" : "X5",
                    "city" : "Athens_changed",
                    "street_name" : "Metron_changed",
                    "street_number" : 12,
                    "postal_code" : 23465 }
        payload=json.dumps(payload)

        #payload = urllib.parse.urlencode(payload)
        head = {'Authorization':'Bearer '+'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYxNTc0Mzk5OSwianRpIjoiMTFjNTYxMmQtYjlkYi00OWZiLWJlOTctMjYzM2E3ZDc5ZDJmIiwibmJmIjoxNjE1NzQzOTk5LCJ0eXBlIjoiYWNjZXNzIiwic3ViIjoiZ2VvdGVzdCIsImV4cCI6MTYxNTgzMDM5OX0.RQNabu829r46M8wmlt6A8EndWPSJ8knrUPmlrPh4FDA', 'Content-Type':'application/json'}
        tester = app.test_client(self)
        #headers["Content-Type"] = "application/json"
        #print("PAYLOAD")
        #print(payload)
        response = tester.put(url, headers=head, data=payload)
        #print('HEEYYYYYYYYYYYYYY ')
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        #print(mydata)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(mydata['msg'], 'User updated successfully')

    def test_SessionsperDate(self):
        url = "evcharge/api/user/login"
        payload = {'username' : 'geotest3', 'password' : '123456'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        tester = app.test_client(self)
        response = tester.post(url, headers=headers, data=payload)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)

        url = "evcharge/api/user/geotest3/SessionsPerDate/2019-02-01/2021-03-31"
        tester = app.test_client(self)
        headers['Authorization'] = 'Bearer ' + mydata['token']
        response = tester.get(url, headers=headers)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        #print(mydata)
        if response.status_code == 200:
            self.assertEqual(mydata['msg'], 'Total charging sessions')
        elif response.status_code == 400:
            self.assertEqual(mydata['message'], 'No charging sessions')
    
    def test_SessionsPerStation(self):
        url = "evcharge/api/user/login"
        payload = {'username' : 'geotest3', 'password' : '123456'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        tester = app.test_client(self)
        response = tester.post(url, headers=headers, data=payload)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)

        url = "evcharge/api/user/geotest3/SessionsPerStation/Station_1/2019-02-01/2021-03-31"
        tester = app.test_client(self)
        headers['Authorization'] = 'Bearer ' + mydata['token']
        response = tester.get(url, headers=headers)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        #print(mydata)
        if response.status_code == 200:
            self.assertEqual(mydata['msg'], 'Total charging sessions')
        elif response.status_code == 400:
            self.assertEqual(mydata['message'], 'No charging sessions')

    def test_Newcontract(self):
    
        url = "evcharge/api/user/login"
        payload = {'username' : 'geotest10', 'password' : '123456'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        tester = app.test_client(self)
        response = tester.post(url, headers=headers, data=payload)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        print(mydata)
        url = "evcharge/api/user/geotest10/NewContract"
        payload = {'distributor' : 'DEDDIE'}
        payload=json.dumps(payload)

        tester = app.test_client(self)
        #headers["Accept"] = "application/json"
        headers["Content-Type"] = "application/json"
        headers['Authorization'] = 'Bearer ' + mydata['token']
        response = tester.post(url, headers=headers, data=payload)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        print('HEEYYYYYYYYYYYYYY ')
        print(mydata)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(mydata['msg'], 'Successful insertion of new contract')

    def test_bill_payment(self):
        url = "evcharge/api/user/login"
        payload = {'username' : 'geotest3', 'password' : '123456'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        tester = app.test_client(self)
        response = tester.post(url, headers=headers, data=payload)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)

        url = "evcharge/api/user/geotest3/bill_payment"
        tester = app.test_client(self)
        headers['Authorization'] = 'Bearer ' + mydata['token']
        response = tester.put(url, headers=headers)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        #print(mydata)
        #print(response.status_code)
        if response.status_code == 200:
            self.assertEqual(mydata['msg'], 'Successful bill payment')
        elif response.status_code == 400:
            self.assertEqual(mydata['message'], 'Bill Payment Failed')
    
    '''Max retries
    def test_cost_by_duration(self):
        
        url = "evcharge/api/user/login"
        payload = {'username' : 'geotest17', 'password' : '123456'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        tester = app.test_client(self)
        response = tester.post(url, headers=headers, data=payload)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        

        url = "evcharge/api/user/geotest/Station_1_1/3:10:0/calculate"
        tester = app.test_client(self)
        #headers['Authorization'] = 'Bearer ' + mydata['token']
        head = {'Authorization':'Bearer '+'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYxNTc0Mzk5OSwianRpIjoiMTFjNTYxMmQtYjlkYi00OWZiLWJlOTctMjYzM2E3ZDc5ZDJmIiwibmJmIjoxNjE1NzQzOTk5LCJ0eXBlIjoiYWNjZXNzIiwic3ViIjoiZ2VvdGVzdCIsImV4cCI6MTYxNTgzMDM5OX0.RQNabu829r46M8wmlt6A8EndWPSJ8knrUPmlrPh4FDA', 'Content-Type':'application/json'}
        response = tester.get(url, headers=head, follow_redirects=True)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        print("HEYYYYYYY")
        print(mydata)
        print(response.status_code)
        if response.status_code == 200:
            self.assertEqual(mydata['msg'], 'Calculation of cost succeded')
        elif response.status_code == 400:
            self.assertEqual(mydata['message'], '')
    '''

    '''Max retries2
    def test_cost_by_percentage(self):
        url = "evcharge/api/user/login"
        payload = {'username' : 'geotest12', 'password' : '123456'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        tester = app.test_client(self)
        response = tester.post(url, headers=headers, data=payload)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        print(mydata)
        url = "evcharge/api/user/geotest12/Station_1_1/20/100/calculate"
        tester = app.test_client(self)
        headers['Authorization'] = 'Bearer ' + mydata['token']
        response = tester.get(url, headers=headers)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        print(mydata)
        print(response.status_code)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(mydata['msg'], 'Calculation of cost succeded')
    '''


#--------------------- Admin tests -----------------------------------------


    def test_admin_info(self):
        url = "evcharge/api/admin/login"
        payload = {'username' : 'DEDDIE_admin1', 'password' : 'deddie_admin_1_pass'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        tester = app.test_client(self)
        response = tester.post(url, headers=headers, data=payload)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        
        url = "evcharge/api/admin/DEDDIE_admin1"
        tester = app.test_client(self)
        headers['Authorization'] = 'Bearer ' + mydata['token']
        response = tester.get(url, headers=headers)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        #print(mydata)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(mydata['msg'], "Admin's info")

    def test_admin_login(self):
        url = "evcharge/api/admin/login"
        payload = {'username' : 'DEDDIE_admin1', 'password' : 'deddie_admin_1_pass'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        tester = app.test_client(self)
        response = tester.post(url, headers=headers, data=payload)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        #print(mydata)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(mydata['msg'], "Login Successful")

    def test_admin_login_error(self):
        url = "evcharge/api/admin/login"
        payload = {'username' : 'DEDDIE_admin1', 'password' : 'wrong'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        tester = app.test_client(self)
        response = tester.post(url, headers=headers, data=payload)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        #print(mydata)
        #print(response.status_code)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(mydata['message'], "Not valid user credentials")

    def test_admin_subs(self):
        url = "evcharge/api/admin/login"
        payload = {'username' : 'DEDDIE_admin1', 'password' : 'deddie_admin_1_pass'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        tester = app.test_client(self)
        response = tester.post(url, headers=headers, data=payload)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)

        url = "evcharge/api/admin/DEDDIE_admin1/subs"
        tester = app.test_client(self)
        headers['Authorization'] = 'Bearer ' + mydata['token']
        response = tester.get(url, headers=headers)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        #print(mydata)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(mydata['msg'], "Total contracts")

    def test_admin_issue_bill(self):
        url = "evcharge/api/admin/login"
        payload = {'username' : 'DEDDIE_admin1', 'password' : 'deddie_admin_1_pass'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        tester = app.test_client(self)
        response = tester.post(url, headers=headers, data=payload)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)

        url = "evcharge/api/admin/DEDDIE_admin1/michalakos/issue"
        tester = app.test_client(self)
        headers['Authorization'] = 'Bearer ' + mydata['token']
        response = tester.put(url, headers=headers)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        #print(mydata)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(mydata['msg'], "Bill successfully issued")

    
    def test_admin_delete_contract(self):
        url = "evcharge/api/admin/login"
        payload = {'username' : 'DEDDIE_admin1', 'password' : 'deddie_admin_1_pass'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        tester = app.test_client(self)
        response = tester.post(url, headers=headers, data=payload)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)

        url = "evcharge/api/admin/DEDDIE_admin1/delete_contract"
        payload = {'contract_id' : '32'}
        payload = json.dumps(payload)
        tester = app.test_client(self)
        headers['Authorization'] = 'Bearer ' + mydata['token']
        headers['Content-Type'] = 'application/json'
        response = tester.delete(url, headers=headers, data=payload)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        #print(mydata)
        #print(response.status_code)
        if response.status_code == 200:
            self.assertEqual(mydata['msg'], "Successfully deleted contract")
        elif response.status_code == 400: #No contract or not his contract
            self.assertEqual(mydata['message'], "Delete Contract Failed")
    

    def test_getUsers(self):
        url = "evcharge/api/admin/login"
        payload = {'username' : 'DEDDIE_admin1', 'password' : 'deddie_admin_1_pass'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        tester = app.test_client(self)
        response = tester.post(url, headers=headers, data=payload)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)

        url = "evcharge/api/admin/DEDDIE_admin1/users"
        tester = app.test_client(self)
        headers['Authorization'] = 'Bearer ' + mydata['token']
        response = tester.get(url, headers=headers)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        #print("EDWWWWWWWWWWWW")
        #print(mydata)
        #print(response.status_code)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(mydata['msg'], "Names of all users")


    '''Another max retries 3
    def test_admin_getUser(self):
        url = "evcharge/api/admin/login"
        payload = {'username' : 'DEDDIE_admin1', 'password' : 'deddie_admin_1_pass'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        tester = app.test_client(self)
        response = tester.post(url, headers=headers, data=payload)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)

        url = "evcharge/api/admin/DEDDIE_admin1/michalakos"
        tester = app.test_client(self)
        headers['Authorization'] = 'Bearer ' + mydata['token']
        headers['Content-Type'] = 'application/json'
        response = tester.get(url, headers=headers)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        print("EDWWWWWWWWWWWW")
        print(mydata)
        print(response.status_code)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(mydata['msg'], "Success")
    '''

    '''max ret 4
    def test_admin_create_user(self):
        url = "evcharge/api/admin/login"
        payload = {'username' : 'DEDDIE_admin1', 'password' : 'deddie_admin_1_pass'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        tester = app.test_client(self)
        response = tester.post(url, headers=headers, data=payload)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)

        url = "evcharge/api/admin/DEDDIE_admin1/create_user"
        tester = app.test_client(self)
        headers['Authorization'] = 'Bearer ' + mydata['token']
        headers['Content-Type'] = 'application/json'
        response = tester.post(url, headers=headers)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        print("EDWWWWWWWWWWWW")
        print(mydata)
        print(response.status_code)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(mydata['msg'], "Names of all users")
    '''

    def test_admin_points(self):
        url = "evcharge/api/admin/login"
        payload = {'username' : 'DEDDIE_admin1', 'password' : 'deddie_admin_1_pass'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        tester = app.test_client(self)
        response = tester.post(url, headers=headers, data=payload)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)

        url = "evcharge/api/admin/DEDDIE_admin1/points"
        tester = app.test_client(self)
        headers['Authorization'] = 'Bearer ' + mydata['token']
        response = tester.get(url, headers=headers)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        #print("EDWWWWWWWWWWWW222")
        #print(mydata)
        #print(response.status_code)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(mydata['msg'], "available points")

    def test_admin_station_points(self):
        url = "evcharge/api/admin/login"
        payload = {'username' : 'DEDDIE_admin1', 'password' : 'deddie_admin_1_pass'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        tester = app.test_client(self)
        response = tester.post(url, headers=headers, data=payload)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)

        url = "evcharge/api/admin/DEDDIE_admin1/Station_10/points"
        tester = app.test_client(self)
        headers['Authorization'] = 'Bearer ' + mydata['token']
        response = tester.get(url, headers=headers)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        #print("EDWWWWWWWWWWWW222")
        #print(mydata)
        #print(response.status_code)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(mydata['msg'], "available points for admin in a station")
    
    
    def test_admin_for_user_contact_info(self):
        url = "evcharge/api/admin/login"
        payload = {'username' : 'DEDDIE_admin1', 'password' : 'deddie_admin_1_pass'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        tester = app.test_client(self)
        response = tester.post(url, headers=headers, data=payload)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)

        url = "evcharge/api/admin/DEDDIE_admin1/michalakos/sub"
        tester = app.test_client(self)
        headers['Authorization'] = 'Bearer ' + mydata['token']
        response = tester.get(url, headers=headers)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        #print("EDWWWWWWWWWWWW222")
        #print(mydata)
        #print(response.status_code)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(mydata['msg'], "Contract Info")
    

#--------------------- SuperAdmin tests -----------------------------------------


    def test_super_admin_login(self):
        url = "evcharge/api/superadmin/login"
        payload = {'username' : 'admin', 'password' : 'petrol4ever'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        tester = app.test_client(self)
        response = tester.post(url, headers=headers, data=payload)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        #print(mydata)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(mydata['msg'], "Login Successful")


#--------------------- Boss tests -----------------------------------------

    def test_boss_create(self):
        url = "evcharge/api/boss/create"
        payload = { 'boss_no' : 'boom', 
                    'password' : '123456',
                    'birth_date' : '1999-08-04',
                    'email' : 'geo@gmail.com',
                    'first_name' : 'Geo',
                    'last_name' : 'Sot',
                    'phone' : 2109311111,
                    'city' : 'Athens',
                    'street_name' : 'Metron',
                    'street_number' : 11,
                    'postal_code' : 12345,
                    'working_company' : 'DEDDIE'}
        
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        tester = app.test_client(self)
        response = tester.post(url, headers=headers, data=payload)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        #print("EDWWWWWWWWWWWW222")
        #print(mydata)
        #print(response.status_code)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(mydata['msg'], 'Boss created successfully')
 

    def test_boss_login(self):
        url = "evcharge/api/boss/login"
        payload = {'username' : 'boss', 'password' : '1234567'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        tester = app.test_client(self)
        response = tester.post(url, headers=headers, data=payload)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        #print("EDWWWWWWWWWWWW222")
        #print(mydata)
        #print(response.status_code)
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(mydata['msg'], "Login Successful")

    def test_boss_login_content(self):
        url = "evcharge/api/boss/login"
        payload = {'username' : 'boss', 'password' : '1234567'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        tester = app.test_client(self)
        response = tester.post(url, headers=headers, data=payload)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        #print("EDWWWWWWWWWWWW222")
        #print(mydata)
        #print(response.status_code)
        self.assertEqual(mydata['msg'], "Login Successful")


    def test_boss_chpwd(self):
        url = "evcharge/api/boss/login"
        payload = {'username' : 'bgeo', 'password' : '123456'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        tester = app.test_client(self)
        response = tester.post(url, headers=headers, data=payload)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        print("TSEKARE")
        print(mydata)

        url = "evcharge/api/boss/bgeo/chpwd"
        payload = { 'old_password' : '123456',
                    'new_password' : '1234567'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        headers['Authorization'] = 'Bearer ' + mydata['token']
        tester = app.test_client(self)
        print(headers)
        response = tester.put(url, headers=headers, data=payload)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        print("EDWWWWWWWWWWWW222")
        print(mydata)
        print(response.status_code)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(mydata['msg'], 'Password updated successfully')


    def test_boss_delete(self):
        url = "evcharge/api/boss/login"
        payload = {'username' : 'bgeosotos', 'password' : '123456'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        tester = app.test_client(self)
        response = tester.post(url, headers=headers, data=payload)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        #print("TSEKARE")
        #print(mydata)

        url = "evcharge/api/boss/bgeosotos"
        payload = { 'password' : '123456' }
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        headers['Authorization'] = 'Bearer ' + mydata['token']
        tester = app.test_client(self)
        #print(headers)
        response = tester.delete(url, headers=headers, data=payload)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        print("EDWWWWWWWWWWWW222")
        print(mydata)
        print(response.status_code)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(mydata['msg'], 'Boss deleted successfully')


    def test_boss_insert_admin(self):
        url = "evcharge/api/boss/login"
        payload = {'username' : 'boom', 'password' : '123456'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        tester = app.test_client(self)
        response = tester.post(url, headers=headers, data=payload)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)

        url = "evcharge/api/boss/insert_admin"
        payload = { 'administrator_no' : 'ad', 
                    'password' : '123456',
                    'birth_year' : 1999,
                    'birth_date' : 23,
                    'birth_month' : 11,
                    'email' : 'geo@gmail.com',
                    'first_name' : 'Geo',
                    'last_name' : 'Sot',
                    'phone' : 2109311111,
                    'city' : 'Athens',
                    'street_name' : 'Metron',
                    'street_number' : 11,
                    'postal_code' : 12345,
                    'working_company' : 'DEDDIE'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        headers['Authorization'] = 'Bearer ' + mydata['token']
        tester = app.test_client(self)
        #print(headers)
        response = tester.post(url, headers=headers, data=payload)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        print("EDWWWWWWWWWWWW222")
        print(mydata)
        print(response.status_code)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(mydata['msg'], 'Admin created successfully')
 

    def test_boss_delete_admin(self):
        url = "evcharge/api/boss/login"
        payload = {'username' : 'boom', 'password' : '123456'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        tester = app.test_client(self)
        response = tester.post(url, headers=headers, data=payload)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)

        url = "evcharge/api/boss/delete_admin"
        payload = { 'administrator_no' : 'ad', 
                    'password' : '123456',
                    'boss_no' : 'boom'
                }
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        headers['Authorization'] = 'Bearer ' + mydata['token']
        tester = app.test_client(self)
        #print(headers)
        response = tester.delete(url, headers=headers, data=payload)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        print("EDWWWWWWWWWWWW222")
        print(mydata)
        print(response.status_code)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(mydata['msg'], 'Administrator deleted successfully')
 

    def test_boss_show_admin(self):
        url = "evcharge/api/boss/login"
        payload = {'username' : 'boom', 'password' : '123456'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        tester = app.test_client(self)
        response = tester.post(url, headers=headers, data=payload)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        #print(mydata)

        url = "evcharge/api/boss/boom/show_admins"
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        headers['Authorization'] = 'Bearer ' + mydata['token']
        tester = app.test_client(self)
        #print(headers)
        response = tester.get(url, headers=headers, data=payload)
        dict_str = response.data.decode("UTF-8")
        mydata = ast.literal_eval(dict_str)
        #print("EDWWWWWWWWWWWW222")
        #print(mydata)
        #print(response.status_code)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(mydata['msg'], 'All admins working for your company')


#--------------------- Contract tests -----------------------------------------


    def test_contracts(self):
        url = "evcharge/api/contracts"
        tester = app.test_client(self)
        response = tester.get(url)
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(mydata['msg'], 'available contracts')


if __name__ == '__main__':
    unittest.main()