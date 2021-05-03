import unittest
import requests
import urllib
import pprint
import json

#import api

from requests.structures import CaseInsensitiveDict
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Content-Type"] = "application/json"



class ApiTest(unittest.TestCase):

#--------------------- User tests -----------------------------------------

    def test_user_create(self):
        url = "http://127.0.0.1:5000/user/create"
        payload = {'username' : 'geotest6', 
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
        response = requests.request("POST", url, headers=headers, data=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['msg'], 'User created successfully')    
    
    def test_user_create_error(self):
        url = "http://127.0.0.1:5000/user/create"
        response = requests.request("POST", url)
        #pprint.pprint(response)
        self.assertNotEqual(response.status_code, 200)

    
    def test_user_login(self):
        url = "http://127.0.0.1:5000/user/login"
        payload = {'username' : 'geotest2', 'password' : '123456'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.request("POST", url, headers=headers, data=payload)
        self.assertEqual(response.status_code, 200)
        tok = response.json()['token']
        #print(tok)
    

    def test_user_login_error(self):
        url = "http://127.0.0.1:5000/user/login"
        payload = {'username' : 'michalakos', 'password' : 'wrong'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.request("POST", url, headers=headers, data=payload)
        #pprint.pprint(response)
        self.assertEqual(response.status_code, 401)

    def test_user_chpwd(self):
        url = "http://127.0.0.1:5000/user/geotest/chpwd"
        payload = { 'old_password' : '1234567',
                    'new_password' : '123456'}
        
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.request("PUT", url, headers=headers, data=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['msg'], 'Password updated successfully')

    def test_user_chpwd_error(self):
        url = "http://127.0.0.1:5000/user/geotest/chpwd"
        payload = { 'old_password' : 'wrong',
                    'new_password' : 'basket11'}
        
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.request("PUT", url, headers=headers, data=payload)
        self.assertEqual(response.status_code, 400)
    
    
    def test_user_get(self):
        url = "http://127.0.0.1:5000/user/login"
        payload = {'username' : 'geotest3', 'password' : '123456'}
        payload = urllib.parse.urlencode(payload)
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        response = requests.request("POST", url, headers=headers, data=payload)

        url = "http://127.0.0.1:5000/user/geotest3"
        headers['Authorization'] = 'Bearer ' + response.json()['token']
        response = requests.request("GET", url, headers=headers)
        #pprint.pprint(response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['msg'], 'Got user profile info successfully')
    
    def test_user_delete(self):
        url = "http://127.0.0.1:5000/user/login"
        payload = {'username' : 'geotest5', 'password' : '123456'}
        payload = urllib.parse.urlencode(payload)
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        response = requests.request("POST", url, headers=headers, data=payload)

        url = "http://127.0.0.1:5000/user/geotest5"
        payload = {'password' : '123456'}
        payload = urllib.parse.urlencode(payload)
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['Authorization'] = 'Bearer ' + response.json()['token']
        response = requests.request("DELETE", url, headers=headers, data=payload)
        #pprint.pprint(response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['msg'], 'User deleted successfully')

    '''
    def test_user_update(self):
        url = "http://127.0.0.1:5000/user/login"
        payload = {'username' : 'geotest20', 'password' : '123456'}
        payload = urllib.parse.urlencode(payload)
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        response = requests.request("POST", url, headers=headers, data=payload)
        
        url = "http://127.0.0.1:5000/user/geotest20"
        payload = { 'first_name' : 'Geo_changed',
                    'last_name' : 'Sot_changed',
                    'phone' : '2109322222',
                    'car_brand' : 'BMW',
                    'car_model' : 'X5',
                    'city' : 'Athens_changed',
                    'street_name' : 'Metron_changed',
                    'street_number' : '12',
                    'postal_code' : '23465'}
        
        headers["Accept"] = "application/json"
        headers["Content-Type"] = "application/json"
        headers['Authorization'] = 'Bearer ' + response.json()['token']
        response = requests.request("PUT", url, headers=headers, data=payload)
        pprint.pprint(response)
        pprint.pprint(response.json())
        #self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['msg'], 'User updated successfully')
    '''

    def test_SessionsperDate(self):
        url = "http://127.0.0.1:5000/user/login"
        payload = {'username' : 'michalakos', 'password' : 'JLKFjdlsa#*uy'}
        payload = urllib.parse.urlencode(payload)
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        response = requests.request("POST", url, headers=headers, data=payload)

        url = "http://127.0.0.1:5000/user/michalakos/SessionsPerDate/2019-02-01/2021-03-31"
        headers['Authorization'] = 'Bearer ' + response.json()['token']
        response = requests.request("GET", url, headers=headers)
        #pprint.pprint(response.json())
        self.assertEqual(response.status_code, 200)

    '''
    def test_SessionsperStation(self):
        url = "http://127.0.0.1:5000/user/login"
        payload = {'username' : 'michalakos', 'password' : 'JLKFjdlsa#*uy'}
        payload = urllib.parse.urlencode(payload)
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        response = requests.request("POST", url, headers=headers, data=payload)

        url = "http://127.0.0.1:5000/user/michalakos/SessionsPerStation/2019-02-01/2021-03-31"
        headers['Authorization'] = 'Bearer ' + response.json()['token']
        response = requests.request("GET", url, headers=headers)
        pprint.pprint(response)
        self.assertEqual(response.status_code, 200)
    

    def test_Newcontract(self):
        url = "http://127.0.0.1:5000/user/login"
        payload = {'username' : 'geotest11', 'password' : '123456'}
        payload = urllib.parse.urlencode(payload)
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        response = requests.request("POST", url, headers=headers, data=payload)

        url = "http://127.0.0.1:5000/user/geotest11/NewContract"
        payload = {'distributor' : 'DEDDIE'}
        headers['Authorization'] = 'Bearer ' + response.json()['token']
        response = requests.request("POST", url, headers=headers, data=payload)
        pprint.pprint(response.json())
        #self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['msg'], 'Successful insertion of new contract')

    '''

    def test_bill_payment(self):
        url = "http://127.0.0.1:5000/user/login"
        payload = {'username' : 'geotest12', 'password' : '123456'}
        payload = urllib.parse.urlencode(payload)
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        response = requests.request("POST", url, headers=headers, data=payload)

        url = "http://127.0.0.1:5000/user/geotest12/bill_payment"
        headers['Authorization'] = 'Bearer ' + response.json()['token']
        response = requests.request("PUT", url, headers=headers)
        #pprint.pprint(response.json())
        #self.assertEqual(response.status_code, 200)
        #for this user it calls errors
        self.assertEqual(response.json()['message'], 'Bill Payment Failed')

    def test_cost_by_duration(self):
        url = "http://127.0.0.1:5000/user/login"
        payload = {'username' : 'geotest12', 'password' : '123456'}
        payload = urllib.parse.urlencode(payload)
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        response = requests.request("POST", url, headers=headers, data=payload)

        url = "http://127.0.0.1:5000/user/geotest12/Station_1_1/00:50:00/calculate"
        headers['Authorization'] = 'Bearer ' + response.json()['token']
        response = requests.request("GET", url, headers=headers)
        #pprint.pprint(response.json()) COOL!
        #self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['msg'], 'Calculation of cost succeded')

    def test_cost_by_percentage(self):
        url = "http://127.0.0.1:5000/user/login"
        payload = {'username' : 'geotest12', 'password' : '123456'}
        payload = urllib.parse.urlencode(payload)
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        response = requests.request("POST", url, headers=headers, data=payload)

        url = "http://127.0.0.1:5000/user/geotest12/Station_1_1/20/100/calculate"
        headers['Authorization'] = 'Bearer ' + response.json()['token']
        response = requests.request("GET", url, headers=headers)
        #pprint.pprint(response.json()) SUPER COOL <3 !!!
        #self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['msg'], 'Calculation of cost succeded')


#--------------------- Admin tests -----------------------------------------


    def test_admin_info(self):
        url = "http://127.0.0.1:5000/admin/login"
        payload = {'username' : 'DEDDIE_admin1', 'password' : 'deddie_admin_1_pass'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.request("POST", url, headers=headers, data=payload)

        url = "http://127.0.0.1:5000/admin/DEDDIE_admin1"
        headers['Authorization'] = 'Bearer ' + response.json()['token']
        response = requests.request("GET", url, headers=headers)
        #pprint.pprint(response.json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['msg'], "Admin's info")

    def test_admin_login(self):
        url = "http://127.0.0.1:5000/admin/login"
        payload = {'username' : 'DEDDIE_admin1', 'password' : 'deddie_admin_1_pass'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.request("POST", url, headers=headers, data=payload)
        self.assertEqual(response.status_code, 200)
        #tok = response.json()['token']
        #print(tok)

    def test_admin_login_error(self):
        url = "http://127.0.0.1:5000/admin/login"
        payload = {'username' : 'DEDDIE_admin1', 'password' : 'wrong'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.request("POST", url, headers=headers, data=payload)
        #pprint.pprint(response)
        self.assertEqual(response.status_code, 401)
    
    def test_admin_subs(self):
        url = "http://127.0.0.1:5000/admin/login"
        payload = {'username' : 'DEDDIE_admin1', 'password' : 'deddie_admin_1_pass'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.request("POST", url, headers=headers, data=payload)
        
        url = "http://127.0.0.1:5000/admin/DEDDIE_admin1/subs"
        headers['Authorization'] = 'Bearer ' + response.json()['token']
        response = requests.request("GET", url, headers=headers)
        #pprint.pprint(response.json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['msg'], "Total contracts")

    def test_admin_issue_bill(self):
        url = "http://127.0.0.1:5000/admin/login"
        payload = {'username' : 'DEDDIE_admin1', 'password' : 'deddie_admin_1_pass'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.request("POST", url, headers=headers, data=payload)
        
        url = "http://127.0.0.1:5000/admin/DEDDIE_admin1/michalakos/issue"
        headers['Authorization'] = 'Bearer ' + response.json()['token']
        response = requests.request("PUT", url, headers=headers)
        #pprint.pprint(response.json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['msg'], "Bill successfully issued")

    '''
    def test_admin_delete_contract(self):
        url = "http://127.0.0.1:5000/admin/login"
        payload = {'username' : 'DEDDIE_admin1', 'password' : 'deddie_admin_1_pass'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.request("POST", url, headers=headers, data=payload)
        
        url = "http://127.0.0.1:5000/admin/DEDDIE_admin1/delete_contract"
        payload = {'contract_id' : '32'}
        headers['Authorization'] = 'Bearer ' + response.json()['token']
        headers["Accept"] = "application/json"
        headers["Content-Type"] = "application/json"
        response = requests.request("DELETE", url, headers=headers, data=payload)
        pprint(response)
        #self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['msg'], "Successfully deleted contract")
    '''

    def test_admin_getUser(self):
        url = "http://127.0.0.1:5000/admin/login"
        payload = {'username' : 'DEDDIE_admin1', 'password' : 'deddie_admin_1_pass'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.request("POST", url, headers=headers, data=payload)
        
        url = "http://127.0.0.1:5000/admin/DEDDIE_admin1/michalakos"
        headers['Authorization'] = 'Bearer ' + response.json()['token']
        response = requests.request("GET", url, headers=headers)
        #pprint.pprint(response.json()) perfect!
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['msg'], "Success")


    def test_admin_create_user(self):
        url = "http://127.0.0.1:5000/admin/login"
        payload = {'username' : 'DEDDIE_admin1', 'password' : 'deddie_admin_1_pass'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.request("POST", url, headers=headers, data=payload)

        url = "http://127.0.0.1:5000/admin/DEDDIE_admin1/create_user"
        headers['Authorization'] = 'Bearer ' + response.json()['token']
        response = requests.request("POST", url, headers=headers)
        #pprint.pprint(response)
        #user exists
        self.assertEqual(response.status_code, 500)
        #self.assertEqual(response.json()['msg'], "Successfully created new user'")


#--------------------- Boss tests -----------------------------------------


    def test_boss_show_admins(self):
        response = requests.get('http://localhost:5000/boss/DEDDIE_boss1/show_admins')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['msg'], 'All admins working for your company')
    
    def test_boss_create(self):
        url = "http://127.0.0.1:5000/boss/create"
        payload = { 'boss_no' : 'boss6', 
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
        response = requests.request("POST", url, headers=headers, data=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['msg'], 'Boss created successfully')

    def test_boss_login(self):
        url = "http://127.0.0.1:5000/boss/login"
        payload = {'boss_no' : 'boss', 'password' : '123456'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.request("GET", url, headers=headers, data=payload)
        self.assertEqual(response.status_code, 200)
        #tok = response.json()['token']
        #print(tok)
    
    def test_boss_chpwd(self):
        url = "http://127.0.0.1:5000/boss/boss2/chpwd"
        payload = { 'old_password' : '123456',
                    'new_password' : '1234567'}
        
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.request("PUT", url, headers=headers, data=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['msg'], 'Password updated successfully')

    def test_boss_chpwd_error(self):
        url = "http://127.0.0.1:5000/boss/boss2/chpwd"
        payload = { 'old_password' : 'wrong',
                    'new_password' : '123456'}
        
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.request("PUT", url, headers=headers, data=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['msg'], 'Incorrect Password')

    def test_boss_delete(self):
        url = "http://127.0.0.1:5000/boss/boss5"
        payload = { 'password' : '123456'}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.request("DELETE", url, headers=headers, data=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['msg'], 'Boss deleted successfully')

    def test_boss_insert_admin(self):
        url = "http://127.0.0.1:5000/boss/insert_admin"
        payload = { 'administrator_no' : 'admin6', 
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
        response = requests.request("POST", url, headers=headers, data=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['msg'], 'Admin created successfully')

    def test_boss_delete_admin(self):
        url = "http://127.0.0.1:5000/boss/delete_admin"
        payload = { 'boss_no' : 'boss',
                    'password' : '123456',
                    'administrator_no' : 'admin5' }
        
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.request("DELETE", url, headers=headers, data=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['msg'], 'Administrator deleted successfully')


#--------------------- Points tests -----------------------------------------


    def test_points(self):
        response = requests.get('http://localhost:5000/points')
        #pprint.pprint(response.json()['msg'])
        self.assertEqual(response.status_code, 200)

    def test_points_msg(self):
        response = requests.get('http://localhost:5000/points')
        #pprint.pprint(response.json()['msg'])
        self.assertEqual(response.json()['msg'], 'available points')


#--------------------- Contract tests -----------------------------------------


    def test_contracts(self):
        response = requests.get('http://localhost:5000/contracts')
        #pprint.pprint(response.json()['msg'])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['msg'], 'available contracts')


#--------------------- Car tests -----------------------------------------


    def test_cars(self):
        response = requests.get('http://localhost:5000/cars')
        #pprint.pprint(response.json()['msg'])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['msg'], 'available cars')

    def test_car_brands(self):
        response = requests.get('http://localhost:5000/car/brands')
        #pprint.pprint(response.json()['msg'])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['msg'], 'Successfully returned all brands') 

    def test_car_brands(self):
        response = requests.get('http://localhost:5000/car/Tesla/models')
        #pprint.pprint(response.json()['msg'])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['msg'], 'success')

    '''
    def test_car_create(self):
        url = "http://127.0.0.1:5000/car/create"
        payload = { 'car_no' : '100', 
                    'brand' : 'Tesla',
                    'model' : 'Model X',
                    'capacitance' : 1001 }
        #payload = urllib.request.(payload)
        #headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url, data=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['msg'], 'Car created successfully')
    '''

#--------------------- Station tests -----------------------------------------


    def test_stations(self):
        response = requests.get('http://localhost:5000/stations')
        #pprint.pprint(response.json()['msg'])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['msg'], 'available stations')
    
    '''
    def test_station_create(self):
        url = "http://127.0.0.1:5000/station/create"
        payload = { 'station_no' : 'station1', 
                    'city' : 'Athens',
                    'street' : 'Metron',
                    'number' : '10',
                    'operator' : 'operator_1'}
        #payload = urllib.parse.json(payload)
        #headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url, data=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['msg'], 'station created successfully')
    '''

if __name__ == '__main__':
    unittest.main()