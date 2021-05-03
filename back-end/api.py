# pip3 install requests

from flask import Flask, Blueprint, abort, request
from flask_restx import Api, Resource, fields
from werkzeug.utils import cached_property
from flask import Flask
from flask_cors import CORS
from flask_cors import CORS
import requests
import datetime
from waitress import serve
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required
from datetime import date
import sqlQueries
import os
import hashlib
import mysql.connector
import errors
import pandas as pd                     
import urllib3

from werkzeug.utils import secure_filename

home = os.path.expanduser("~")
UPLOAD_FOLDER = home+'/Downloads'

urllib3.disable_warnings()

base_url = "http://127.0.0.1:8765/evcharge/api/"
app = Flask(__name__)

blueprint = Blueprint('api', __name__, url_prefix='/evcharge/api')
api = Api(blueprint)
app.register_blueprint(blueprint)



app.config['JWT_SECRET_KEY'] = 'super-duper-secret-key'
app.config['SWAGGER_UI_JSONEDITOR'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


CORS(app, resources={r'/*': {'origins': '*'}})
#CORS(app, resources={r'/*': {'origins': '*'}})

jwt = JWTManager(app)

# -------------- AUTHORIZATIONS ---------------
@api.route('/user/<user_id>/check_auth')
class UserAuth(Resource):
    @jwt_required()
    def get(self, user_id):
        try:
            if (get_jwt_identity() != user_id):
                raise errors.NotAuthorized
            #elif (sqlQueries.check_if_customer(user_id) == False):
             #   raise errors.NotAuthorized
            else:
                return {
                    'msg' : 'Authorized'
                }
        except errors.NotAuthorized as e:
            abort(401, str(e))


@api.route('/admin/<admin_id>/check_auth')
class UserAuth(Resource):
    @jwt_required()
    def get(self, admin_id):
        try:
            if (get_jwt_identity() != admin_id):
                raise errors.NotAuthorized
            #elif (sqlQueries.check_if_admin(admin_id) == False):
            #    raise errors.NotAuthorized
            else:
                return {
                    'msg' : 'Authorized'
                }
        except errors.NotAuthorized as e:
            abort(401, str(e))



# ------------ NEW CHARGING SESSION -----------

@api.route('/charging_session')
class NewChargingSession(Resource):
    def post(self):
        try:
            payload = request.json
            username = payload['username']
            point_id = payload['point_id']
            protocol = payload['protocol']
            charging_type = payload['charging_type']
            points = payload['points']

            time_start = payload['time_start']
            time_end = payload['time_end']
            cost = payload['cost']
            energy = payload['energy']

            for key in payload:
                if payload[key] == "":
                    raise errors.NullParameter

            form_time_start = datetime.datetime.strptime(time_start, '%H:%M:%S')
            form_time_end = datetime.datetime.strptime(time_end, '%H:%M:%S')

            today = date.today()

            sqlQueries.log_session(username, point_id, protocol, charging_type, points, today, form_time_start, form_time_end, cost, energy)


            return {
                'msg' : 'Charging Session Successful'
            }

        except errors.NullParameter as e:
            abort(400, str(e))

        except errors.LogSessionError as e:
            abort(400, str(e))

        except mysql.connector.Error as err:
            abort(400, "Something went wrong: {}".format(err))

        except IndexError as e:
            abort(400, "Bad request with parameters")


# ------------ USERS ---------
@api.route('/user/create')
class CreateUser(Resource):

    def post(self):
        try:
            payload = dict(request.form)
            username = payload['username']
            password = payload['password']
            birth_date = payload['birth_date']
            email = payload['email']
            first_name = payload['first_name']
            last_name = payload['last_name']
            phone = payload['phone']
            car_brand = payload['car_brand']
            car_model = payload['car_model']
            city = payload['city']
            street_name = payload['street_name']
            street_number = payload['street_number']
            postal_code = payload['postal_code']

            birth_date_obj = datetime.datetime.strptime(birth_date, '%Y-%m-%d')
            for key in payload:
                if payload[key] == "":
                    raise errors.NullParameter

            if (not sqlQueries.insert_customer(username,  car_brand, car_model,  password, first_name, last_name,  birth_date_obj, 0, city, street_name, int(street_number), int(postal_code),  Email=email, Phone=int(phone))):
                    raise errors.UserCreationFailed

            return {
                'msg' : 'User created successfully',
                'user_id' : username,
                'email' : payload['email']
            }


        except errors.NullParameter as e:
            abort(400, str(e))

        except errors.UserCreationFailed as e:
            abort(400, str(e))

        except mysql.connector.Error as err:
            abort(400, "Something went wrong: {}".format(err))

        except IndexError as e:
            abort(400, str(e))
        #except Exception as e:
        #    abort(400, str(e), statusCode=400)


# user login api , needs username and password, in success returns auth_token
# else returns either not valid password/name or bad request.
@api.route('/user/login')
class UserLogin(Resource):
    def post(self):
        try:
            payload = dict(request.form)
            username = payload['username']
            password = payload['password']
            for key in payload:
                if payload[key] == "":
                    raise errors.NullParameter

            if (sqlQueries.check_customer_login(username, password) == False):
                raise errors.NotValidPassName

            else:
                expires = datetime.timedelta(days=1)
                access_token = create_access_token(identity=username, expires_delta=expires)

                return {
                    'msg' : 'Login Successful',
                    'token' : access_token
                }

        except errors.NullParameter as e:
            abort(400, str(e))

        except errors.NotValidPassName as e:
            abort(401, str(e))

        except Exception as e:
            abort(400, str(e))


# change password takes old password, new password and returns success message or incorrect old password
@api.route('/user/<user_id>/chpwd')
class UserChpwd(Resource):
    def put(self, user_id):
        try:
            payload = dict(request.form)
            old_password = payload['old_password']
            new_password = payload['new_password']
            for key in payload:
                if payload[key] == "":
                    raise errors.NullParameter
            boolean = sqlQueries.change_customer_password(user_id, old_password, new_password)
            if (boolean):
                return {
                    'msg' : 'Password updated successfully'
                }
            else:
                raise errors.IncorrectOldPassword


        except errors.NullParameter as e:
            abort(400, str(e))

        except errors.IncorrectOldPassword as e:
            abort(400, str(e))

        except Exception as e:
            abort(400, str(e))

# user_info , user_delete and user_update, all of them take user_id as argument .
# for delete password argument is required and for update all user info are required too.
# needs authentication token to work, else not authorized exception is raised.
# also if not valid user_id is given, bad request with message not valid user is raised
@api.route('/user/<user_id>')
class User(Resource):
    @jwt_required()
    def get(self, user_id):
        try:
            user_info = sqlQueries.search_customer(user_id)
            if (len(user_info) == 0):
                raise errors.UserInfoError

            contract_details = sqlQueries.contract_details_user(user_id)


            user = []
            car = []
            contract = []
            if (len(contract_details) != 0):
                contract.append({
                    "supplier" : contract_details[0][0],
                    "price"    : float(contract_details[0][1]),
                    "points"    : user_info[0][3]
                })


            #print(user_info[0][0])
            user.append({
                "username" : user_info[0][0],
                "first_name" : user_info[0][1],
                "last_name" : user_info[0][2],
                "birth_date" : str(user_info[0][4]),
                "address" : user_info[0][5] + ", " + user_info[0][6] + " " + str(user_info[0][7]) + ", " + str(user_info[0][8]),
                "email" : user_info[0][10],
                "phone" : user_info[0][11]


            })
            car.append({
                "id" : user_info[0][12],
                "brand" : user_info[0][13],
                "model" : user_info[0][14],
                "capacitance" : float(user_info[0][15])
            })

            return {
                'msg' : 'Got user profile info successfully',
                'user_info' : user,
                'car_info' : car,
                'contract_info' : contract
            }



        except errors.UserInfoError as e:
            abort(400, str(e))

        except errors.NotAuthorized as e:
            abort(401, str(e))


        except IndexError:
            abort(400)

    @jwt_required()
    def delete(self, user_id):
        try:
            if (get_jwt_identity() != user_id):
                raise errors.NotAuthorized
            payload = dict(request.form)
            password = payload['password']

            if (sqlQueries.check_customer_login(user_id, password)):
                sqlQueries.delete_customer(user_id)

            else:
                raise errors.IncorrectPassword
            return {
                'msg': 'User deleted successfully'
            }

        except errors.NotAuthorized as e:
            abort(401, str(e))

        except errors.IncorrectPassword as e:
            abort(400, str(e))

        except IndexError:
            abort(400)

    @jwt_required()
    def put(self, user_id):
        try:
            if (get_jwt_identity() != user_id):
                raise errors.NotAuthorized
            payload = request.json
            first_name = payload['first_name']
            last_name = payload['last_name']
            phone = payload['phone']
            car_brand = payload['car_brand']
            car_model = payload['car_model']
            city = payload['city']
            street_name = payload['street_name']
            street_number = payload['street_number']
            postal_code = payload['postal_code']
            for key in payload:
                if payload[key] == "":
                    raise errors.NullParameter
            sqlQueries.update_customer(user_id, first_name, last_name, phone, car_brand, car_model, city, street_name, street_number, postal_code)
            return {
                'msg' : 'User updated successfully'
            }

        except errors.NotAuthorized as e:
            abort(401, str(e))

        except errors.NullParameter as e:
            abort(400, str(e))

        except IndexError:
            abort(400)

# return all user charging sessions for a charging station in a given month
@api.route('/user/<user_id>/SessionsPerDate/<yyyymmdd_from>/<yyyymmdd_to>')
class UserSessionsPerDate(Resource):
    @jwt_required()
    def get(self, user_id, yyyymmdd_from, yyyymmdd_to):
        try:
            if (get_jwt_identity() != user_id):
                raise errors.NotAuthorized

            sessions = sqlQueries.user_sessions_per_date(user_id, yyyymmdd_from, yyyymmdd_to)
            if (len(sessions) == 0):
                raise errors.NoChargingSessions
            else:
                sessions_list = [list(row) for row in sessions]
                result = []
                for i in range(0, len(sessions_list)):
                    result.append({
                        "date" :  str(sessions_list[i][0]),
                        "cost" : float(sessions_list[i][1])
                    })


                first_year = datetime.datetime.strptime(result[0]['date'], '%Y-%M-%d').date().year
                last_year = datetime.datetime.strptime(result[len(result) - 1]['date'], '%Y-%M-%d').date().year

                year = first_year
                rows, cols = (last_year-first_year+1, 12)
                sum_costs = [[0 for i in range(cols)] for j in range(rows)]
                i = 0
                j = 0
                tot_num = [[0 for i in range(cols)] for j in range(rows)]
                while (j < len(result)):
                    if (datetime.datetime.strptime(result[j]['date'], '%Y-%M-%d').date().year != year):
                        i = i + 1
                        year = datetime.datetime.strptime(result[j]['date'], '%Y-%M-%d').date().year
                    else:
                        month = datetime.datetime.strptime(result[j]['date'], '%Y-%m-%d').date().month
                        sum_costs[i][int(month) - 1] += result[j]['cost']
                        tot_num[i][int(month) - 1] += 1
                        j += 1
                years_costs = [0 for i in range(last_year-first_year+1)]
                for i in range(len(years_costs)):
                    years_costs[i] = sum(sum_costs[i])
                tot_years_num = [0 for i in range(last_year-first_year+1)]
                for i in range(len(years_costs)):
                    tot_years_num[i] = sum(tot_num[i])
                return {
                    'msg' : 'Total charging sessions',
                    'sessions' : result,
                    'first_year' : first_year,
                    'last_year' : last_year,
                    'sum_costs' : sum_costs,
                    'years_costs' : years_costs,
                    'tot_num' : tot_num,
                    'tot_years_num' : tot_years_num
                }

        except errors.NotAuthorized as e:
            abort(401, str(e))

        except errors.NoChargingSessions as e:
            abort(400, str(e))

        except IndexError:
            abort(400)

@api.route('/user/<user_id>/SessionsPerStation/<station_id>/<yyyymmdd_from>/<yyyymmdd_to>')
class UserSessionsPerStation(Resource):
    @jwt_required()
    def get(self, user_id, station_id, yyyymmdd_from, yyyymmdd_to):
        try:
            if (get_jwt_identity() != user_id):
                raise errors.NotAuthorized
            sessions = sqlQueries.user_sessions_per_station(user_id, station_id, yyyymmdd_from, yyyymmdd_to)
            if (len(sessions) == 0):
                raise errors.NoChargingSessions

            else:
                sessions_list = [list(row) for row in sessions]
                result = []
                for i in range(0, len(sessions_list)):
                    result.append({
                        "date" :  str(sessions_list[i][0]),
                        "cost" : float(sessions_list[i][1])
                    })

                return {
                    'msg' : 'Total charging sessions',
                    'sessions' : result
                }
        except errors.NotAuthorized as e:
            abort(401, str(e))

        except errors.NoChargingSessions as e:
            abort(400, str(e))

        except IndexError:
            abort(400)

@api.route('/user/<user_id>/NewContract')
class UserNewContract(Resource):
    @jwt_required()
    def post(self, user_id):
        try:
            if (get_jwt_identity() != user_id):
                raise errors.NotAuthorized
            payload = request.json
            distributor = payload['distributor']
            if distributor == "":
                raise errors.NullParameter
            if (sqlQueries.insert_contract(user_id, distributor)):
                return {
                    'msg' : 'Successful insertion of new contract'
                }
            else:
                raise errors.InvalidContractInput

        except errors.NotAuthorized as e:
            abort(401, str(e))

        except errors.NullParameter as e:
            abort(400, str(e))

        except Exception as e:
            abort(400, str(e))



@api.route('/user/<user_id>/bill_payment')
class UserBillPayment(Resource):
    @jwt_required()
    def put(self, user_id):
        try:
            # get today's date to update last date bill payment in database
            today = date.today()
            if (sqlQueries.pay_bill(user_id, today)):
                return {
                    'msg' : 'Successful bill payment'
                }
            else:
                raise errors.BillPaymentFailed


        except errors.BillPaymentFailed as e:
            abort(400, str(e))

        except Exception as e:
            abort(400, str(e))




#api to calculate cost for charging process with given time duration
@api.route('/user/<user_id>/<point_id>/<duration>/calculate')
class CalculateCostByDuration(Resource):
    @jwt_required()
    def get(self, user_id, point_id, duration):
        try:
            # call api for user info in order to get car id
            # get auth_token from requests' header
            # and pass it into the new api's headers
            headers = request.headers
            token = headers['Authorization']

            url = base_url + "user/" + user_id
            payload = {}
            headers = {
                'Authorization': token
            }

            x = requests.request("GET", url, headers=headers, data=payload, verify=False)            
            user = x.json()
            car_info = user['car_info'][0]
            car_id = car_info['id']
            time = datetime.datetime.strptime(duration, '%H:%M:%S').time()
            total_duration = time.hour * 60 + time.minute
            session_info = sqlQueries.time_cost(0, total_duration, car_id, point_id)
            if (session_info == -1):
                raise errors.CalculationFailed
            else:
                return {
                    'msg' : 'Calculation of cost succeded',
                    'cost' : float(session_info[0]),
                    'time' : session_info[1],
                    'energy' : float(session_info[2]),
                    'points' : session_info[3]
                }

        except errors.CalculationFailed as e:
            abort(400, str(e))

        except Exception as e:
            abort(400, str(e))

@api.route('/user/<user_id>/<point_id>/<start_percentage>/<end_percentage>/calculate')
class CalculateCostByPercentage(Resource):
    @jwt_required()
    def get(self, user_id, point_id, start_percentage, end_percentage):
        try:
            # call api for user info in ordet to get car id
            headers = request.headers
            token = headers['Authorization']

            url = base_url + "user/" + user_id
            payload={}
            headers = {
                'Authorization': token
            }

            x = requests.request("GET", url, headers=headers, data=payload, verify=False)            
            user = x.json()
            car_info = user['car_info'][0]
            car_id = car_info['id']
            end_percentage = min(100, int(end_percentage))
            if (int(start_percentage) >= end_percentage):
                raise errors.NotValidInput

            result = sqlQueries.percentage_cost(car_id, point_id, int(start_percentage), int(end_percentage))


            if (result == -1):
                raise errors.CalculationFailed
            else:
                return {
                    'msg' : 'Calculation of cost succeded',
                    'cost' : float(result[0]),
                    'time' : result[1],
                    'energy' : float(result[2]),
                    'points' : result[3]
                }
        except errors.NotValidInput as e:
            abort(400, str(e))

        except errors.CalculationFailed as e:
            abort(400, str(e))

        except Exception as e:
            abort(400, str(e))

# --------------------- ADMINSSSSSS -----------------------
def calculateStatistics(result):
    first_year = datetime.datetime.strptime(result[0]['date'], '%Y-%M-%d').date().year
    last_year = datetime.datetime.strptime(result[len(result) - 1]['date'], '%Y-%M-%d').date().year

    year = first_year
    rows, cols, z = (last_year-first_year+1, 12, 31)
    # initialize all arrays for charging stats
    sum_costs_per_day = [[[0 for i in range(z)] for j in range(cols)]  for k in range(rows)]
    sum_costs_per_month = [[0 for i in range(cols)] for j in range(rows)]

    tot_num_per_day = [[[0 for i in range(z)] for j in range(cols)]  for k in range(rows)]
    tot_num_per_month = [[0 for i in range(cols)] for j in range(rows)]

    tot_energy_per_day = [[[0 for i in range(z)] for j in range(cols)]  for k in range(rows)]
    tot_energy_per_month = [[0 for i in range(cols)] for j in range(rows)]
    i = 0
    j = 0
    while (j < len(result)):
        # check if year has changed in order to change row value
        if (datetime.datetime.strptime(result[j]['date'], '%Y-%M-%d').date().year != year):
            i = i + 1
            year = datetime.datetime.strptime(result[j]['date'], '%Y-%M-%d').date().year
        else:
            # take month and day and add the appropriate cost/energy (or + 1 for num of charging sessions)
            month = datetime.datetime.strptime(result[j]['date'], '%Y-%m-%d').date().month
            day = datetime.datetime.strptime(result[j]['date'], '%Y-%m-%d').date().day

            sum_costs_per_day[i][int(month) - 1][int(day) - 1] += result[j]['cost']
            sum_costs_per_month[i][int(month) - 1] += result[j]['cost']

            tot_num_per_day[i][int(month) - 1][int(day) - 1] += 1
            tot_num_per_month[i][int(month) - 1] += 1

            tot_energy_per_day[i][int(month) - 1][int(day) - 1] += result[j]['energy']
            tot_energy_per_month[i][int(month) - 1] += result[j]['energy']

            j += 1
    years_costs = [0 for i in range(last_year-first_year+1)]
    for i in range(len(years_costs)):
        years_costs[i] = sum(sum_costs_per_month[i])
    tot_years_num = [0 for i in range(last_year-first_year+1)]
    for i in range(len(tot_years_num)):
        tot_years_num[i] = sum(tot_num_per_month[i])
    tot_years_energy = [0 for i in range(last_year-first_year+1)]
    for i in range(len(years_costs)):
        tot_years_energy[i] = sum(tot_energy_per_month[i])

    return (first_year, last_year, sum_costs_per_day, sum_costs_per_month, tot_num_per_day, tot_num_per_month, tot_energy_per_day, tot_energy_per_month, years_costs, tot_years_num, tot_years_energy)





@api.route('/admin/<admin_id>')
class AdminInfo(Resource):
    @jwt_required()
    def get(self, admin_id):
        try:
            if (get_jwt_identity() != admin_id):
                raise errors.NotAuthorized
            admin_info = sqlQueries.admin_info(admin_id)

            if (len(admin_info) == 0):
                raise errors.EmptyResponse
            return {
                'msg' : "Admin's info",
                'first_name' : admin_info[0][1],
                'last_name' : admin_info[0][2],
                'birth_Date' : str(admin_info[0][3]),
                'company' : admin_info[0][4],
                'address' : admin_info[0][5] + ", " + admin_info[0][6] + " " + str(admin_info[0][7]) + ", " + str(admin_info[0][8]),
                'email' : admin_info[0][9],
                'phone' : admin_info[0][10]
            }

        except errors.NotAuthorized as e:
            abort(401, str(e))

        except errors.EmptyResponse as e:
            abort(400, str(e))

        except IndexError:
            abort(400)

@api.route('/admin/login')
class AdminLogin(Resource):
    def post(self):
        try:
            payload = dict(request.form)
            username = payload['username']
            password = payload['password']

            for key in payload:
                if payload[key] == "":
                    raise errors.NullParameter

            if (sqlQueries.check_administrator_login(username, password) == False):
                raise errors.NotValidPassName
            else:
                expires = datetime.timedelta(days=1)
                access_token = create_access_token(identity=username, expires_delta=expires)
                return {
                    'msg' : 'Login Successful',
                    'token' : access_token
                }


        except errors.NullParameter as e:
            abort(400, str(e))

        except errors.NotValidPassName as e:
            abort(401, str(e))

        except Exception as e:
            abort(400, str(e))


# given a provider find all enabled subscriptions with them
@api.route('/admin/<admin_id>/subs')
class CompanySubs(Resource):
    @jwt_required()
    def get(self, admin_id):
        try:
            if (get_jwt_identity() != admin_id):
                raise errors.NotAuthorized


            subs = sqlQueries.contract_details_provider(admin_id)
            if (len(subs) == 0):
                raise errors.NoContractsFound

            else:
                subs_list = [list(row) for row in subs]
                result = []
                for i in range(0, len(subs_list)):
                    result.append({
                        "username" :  subs_list[i][0],
                        "first_name" : subs_list[i][1],
                        "last_name" : subs_list[i][2],
                        "email" : subs_list[i][3],
                        "address" : subs_list[i][4] + ", " + subs_list[i][5] + " " + str(subs_list[i][6]) + ", " + str(subs_list[i][7]),
                        "phone" : subs_list[i][8] ,
                        "points" : subs_list[i][9],
                        "last_month_paid_bill" :  str(subs_list[i][10]),
                        "last_month_issued_bill" :  str(subs_list[i][11]),
                        "cost" : float(subs_list[i][12])
                    })

                return {
                    'msg' : 'Total contracts',
                    'sessions' : result
                }

        except errors.NullParameter as e:
            abort(400, str(e))

        except errors.NoCarsFound as e:
            abort(400, str(e))

        except errors.NotAuthorized as e:
            abort(401, str(e))

        except IndexError:
            abort(400)

@api.route('/admin/<admin_id>/<user_id>/issue')
class AdminIssueBill(Resource):
    @jwt_required()
    def put(self, admin_id, user_id):
        try:
            if (get_jwt_identity() != admin_id):
                raise errors.NotAuthorized
            today = date.today()
            #print("Today's date:", today)
            if (sqlQueries.issue_bill(admin_id, user_id, today)):
                return {
                    'msg' : 'Bill successfully issued'
                }
            else :
                raise errors.BillIssueFailed

        except errors.NotAuthorized as e:
            abort(401, str(e))

        except errors.BillIssueFailed as e:
            abort(400, str(e))

        except IndexError as e:
            abort(400, str(e))

@api.route('/admin/<admin_id>/delete_contract')
class AdminDeleteContract(Resource):
    @jwt_required()

    def delete(self, admin_id):
        try:
            if (get_jwt_identity() != admin_id):
                raise errors.NotAuthorized
            payload = request.json
            contract_id = payload['contract_id']
            if (sqlQueries.delete_contract(admin_id, contract_id)):
                return {
                    'msg' : 'Successfully deleted contract'
                }
            else:
                raise errors.DeleteContractFailed


        except errors.DeleteContractFailed as e:
            abort(400, str(e))

        except errors.NotAuthorized as e:
            abort(401, str(e))

        except Exception as e:
            abort(400, str(e))


@api.route('/admin/<admin_id>/SessionsPerStation/<station_id>/<yyyymmdd_from>/<yyyymmdd_to>')
class AdminSessionsPerStation(Resource):
    @jwt_required()

    def get(self, admin_id, station_id, yyyymmdd_from, yyyymmdd_to):
        try:
            if (get_jwt_identity() != admin_id):
                raise errors.NotAuthorized
            sessions = sqlQueries.admin_sessions_per_station(admin_id, station_id, yyyymmdd_from, yyyymmdd_to)
            if (len(sessions) == 0):
                raise errors.NoChargingSessions
            else:
                sessions_list = [list(row) for row in sessions]
                result = []
                total_info = sqlQueries.admin_sessions_per_station_sum(admin_id, station_id, yyyymmdd_from, yyyymmdd_to)

                for i in range(0, len(sessions_list)):
                    result.append({
                        "point_id" : sessions_list[i][0],
                        "date" :  str(sessions_list[i][1]),
                        "start_time" : str(sessions_list[i][2]),
                        "end_time" : str(sessions_list[i][3]),
                        "cost" : float(sessions_list[i][4]),
                        "energy" : float(sessions_list[i][5])

                    })
                (first_year, last_year, sum_costs_per_day, sum_costs_per_month, tot_num_per_day, tot_num_per_month, tot_energy_per_day, tot_energy_per_month, years_costs, tot_years_num, tot_years_energy) = calculateStatistics(result)

                return {
                    'msg' : 'Total charging sessions for a given station',
                    'TotalEnergyDelivered' : float(total_info[0][1]),
                    'NumberOfChargingSessions' : total_info[0][0],
                    'sessions' : result,
                    'first_year' : first_year,
                    'last_year' : last_year,
                    'sum_costs_per_day' : sum_costs_per_day,
                    'sum_costs_per_month' : sum_costs_per_month,
                    'years_costs' : years_costs,
                    'tot_num_per_day' : tot_num_per_day,
                    'tot_num_per_month' : tot_num_per_month,
                    'tot_years_num' : tot_years_num,
                    'tot_energy_per_day' : tot_energy_per_day,
                    'tot_energy_per_month' : tot_energy_per_month,
                    'tot_years_energy' : tot_years_energy

                }

        except errors.NoChargingSessions as e:
            abort(400, str(e))

        except errors.NotAuthorized as e:
            abort(401, str(e))

        except Exception as e:
            abort(400, str(e))





@api.route('/admin/<admin_id>/SessionsPerPoint/<point_id>/<yyyymmdd_from>/<yyyymmdd_to>')
class AdminSessionsPerPoint(Resource):
    @jwt_required()

    def get(self, admin_id, point_id, yyyymmdd_from, yyyymmdd_to):
        try:
            if (get_jwt_identity() != admin_id):
                raise errors.NotAuthorized
            sessions = sqlQueries.admin_sessions_per_point(admin_id, point_id, yyyymmdd_from, yyyymmdd_to)
            if (len(sessions) == 0):
               raise errors.NoChargingSessions
            else:
                sessions_list = [list(row) for row in sessions]
                result = []
                total_info = sqlQueries.admin_sessions_per_point_sum(admin_id, point_id, yyyymmdd_from, yyyymmdd_to)

                for i in range(0, len(sessions_list)):
                    result.append({
                        "serial number" : i,
                        "session_id" : sessions_list[i][0],
                        "date" :  str(sessions_list[i][1]),
                        "start_time" : str(sessions_list[i][2]),
                        "end_time" : str(sessions_list[i][3]),
                        "cost" : float(sessions_list[i][4]),
                        "energy" : float(sessions_list[i][5]),
                        "payment_type" : str(sessions_list[i][6]),
                        "brand"  : sessions_list[i][7],
                        "model" : sessions_list[i][8],
                        "capacitance" : float(sessions_list[i][9])
                    })

                (first_year, last_year, sum_costs_per_day, sum_costs_per_month, tot_num_per_day, tot_num_per_month, tot_energy_per_day, tot_energy_per_month, years_costs, tot_years_num, tot_years_energy) = calculateStatistics(result)

                return {
                    'msg' : 'Total charging sessions for a given point',
                    'TotalEnergyDelivered' : float(total_info[0][1]),
                    'NumberOfChargingSessions' : total_info[0][0],
                    'sessions' : result,
                    'first_year' : first_year,
                    'last_year' : last_year,
                    'sum_costs_per_day' : sum_costs_per_day,
                    'sum_costs_per_month' : sum_costs_per_month,
                    'years_costs' : years_costs,
                    'tot_num_per_day' : tot_num_per_day,
                    'tot_num_per_month' : tot_num_per_month,
                    'tot_years_num' : tot_years_num,
                    'tot_energy_per_day' : tot_energy_per_day,
                    'tot_energy_per_month' : tot_energy_per_month,
                    'tot_years_energy' : tot_years_energy
                }

        except errors.NoChargingSessions as e:
            abort(400, str(e))

        except errors.NotAuthorized as e:
            abort(401, str(e))

        except Exception as e:
            abort(400, str(e))


# takes admin_id and date and returns info for charging sessions for a provider
@api.route('/admin/<admin_id>/SessionsPerProvider/<yyyymmdd_from>/<yyyymmdd_to>')
class AdminSessionsPerProvider(Resource):
    @jwt_required()
    def get(self, admin_id, yyyymmdd_from, yyyymmdd_to):
        try:
            if (get_jwt_identity() != admin_id):
                raise errors.NotAuthorized
            sessions = sqlQueries.sessions_per_admin(admin_id, yyyymmdd_from, yyyymmdd_to)
            if (len(sessions) == 0):
                raise errors.NoChargingSessions
            else:
                sessions_list = [list(row) for row in sessions]
                result = []
                for i in range(0, len(sessions_list)):
                    result.append({
                        "station_id" : sessions_list[i][0],
                        "session_id" : sessions_list[i][1],
                        "vehicle_id" : sessions_list[i][2],
                        "date" :  str(sessions_list[i][3]),
                        "start_time" : str(sessions_list[i][4]),
                        "end_time" : str(sessions_list[i][5]),
                        "energy" : float(sessions_list[i][6]),
                        "cost_per_kwh" : float(sessions_list[i][7]),
                        "cost" : float(sessions_list[i][8])

                    })
                (first_year, last_year, sum_costs_per_day, sum_costs_per_month, tot_num_per_day, tot_num_per_month, tot_energy_per_day, tot_energy_per_month, years_costs, tot_years_num, tot_years_energy) = calculateStatistics(result)

                return {
                    'msg' : 'Total charging sessions for a provider',
                    'sessions' : result,
                    'first_year' : first_year,
                    'last_year' : last_year,
                    'sum_costs_per_day' : sum_costs_per_day,
                    'sum_costs_per_month' : sum_costs_per_month,
                    'years_costs' : years_costs,
                    'tot_num_per_day' : tot_num_per_day,
                    'tot_num_per_month' : tot_num_per_month,
                    'tot_years_num' : tot_years_num,
                    'tot_energy_per_day' : tot_energy_per_day,
                    'tot_energy_per_month' : tot_energy_per_month,
                    'tot_years_energy' : tot_years_energy
                }

        except errors.NoChargingSessions as e:
            abort(400, str(e))

        except errors.NotAuthorized as e:
            abort(401, str(e))

        except Exception as e:
            abort(400, str(e))

@api.route('/admin/<admin_id>/users')
class AdminGetUsers(Resource):
    @jwt_required()
    def get(self, admin_id):
        try:
            if ((get_jwt_identity() != admin_id)):
                raise errors.NotAuthorized
            users = sqlQueries.admin_customers(admin_id)
            if len(users) == 0:
                raise errors.EmptyUsers
            result = []
            for i in range(0, len(users)):
                result.append({
                    "username" : users[i]
                })

            return {
                'msg' : 'Names of all users',
                'users' : result

            }

        except errors.NotAuthorized as e:
            abort(400, str(e))

        except errors.EmptyUsers as e:
            abort(400, str(e))



@api.route('/admin/<admin_id>/<user_id>')
class GetUserData(Resource):
    @jwt_required()
    def get(self, admin_id, user_id):
        try:
            if ((get_jwt_identity() != admin_id)):
                raise errors.NotAuthorized
            elif (not sqlQueries.customer_admin_company(admin_id, user_id)):
                raise errors.NotValidUser


            headers = request.headers
            token = headers['Authorization']
            url = base_url + "user/" + user_id
            payload={}
            headers = {
                'Authorization': token
            }
            x = requests.request("GET", url, headers=headers, data=payload, verify=False)            
            user = x.json()
            user_info = x.json()

            return {
                'msg' : 'Success',
                'user_info' : user_info
            }

        except errors.NotAuthorized as e:
            abort(401, str(e))

        except errors.NotValidUser as e:
            abort(400, str(e))

        except IndexError:
            abort(400)


@api.route('/admin/<admin_id>/create_user')
class AdminCreateUser(Resource):
    @jwt_required()
    def post(self, admin_id):
        try:
            if (get_jwt_identity() != admin_id):
                raise errors.NotAuthorized
            url = base_url + "user/create"
            data = request.form
            headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
            r = requests.post(url, data=data, headers=headers)

            return {
                'result' : r.json()
            }

        except errors.NotAuthorized as e:
            abort(401, str(e))
        except IndexError:
            abort(400)

@api.route('/admin/<admin_id>/points')
class AdminFindPoints(Resource):
    @jwt_required()
    def get(self, admin_id):
        try:
            if (get_jwt_identity() != admin_id):
                raise errors.NotAuthorized

            points = sqlQueries.findall_points_admin(admin_id)
            if (len(points) == 0):
                raise errors.NoPointsForAdminFound
            else:
                points_list = [list(row) for row in points]
                result = []

                for i in range(0, len(points_list)):
                    result.append({
                        'point_id' : points_list[i][0],
                        'distributor_id' : points_list[i][1],
                        'station_id' :  points_list[i][2],
                        'charging_rate' : float(points_list[i][3]),
                        'cost_per_kwh' : float(points_list[i][4])
                    })

                return {
                    'msg' : 'available points',
                    'points' : result
                }

        except errors.NotAuthorized as e:
            abort(401, str(e))

        except errors.NoPointsForAdminFound as e:
            abort(400, str(e))

        except IndexError as e:
            abort(400, str(e))


@api.route('/admin/<admin_id>/<station_id>/points')
class AdminFindPoints(Resource):
    @jwt_required()
    def get(self, admin_id, station_id):
        try:
            if (get_jwt_identity() != admin_id):
                raise errors.NotAuthorized
            points = sqlQueries.findall_points_admin_station(admin_id, station_id)
            if (len(points) == 0):
                raise errors.NoPointsForAdminFound

            else:
                points_list = [list(row) for row in points]
                result = []

                for i in range(0, len(points_list)):
                    result.append({
                        'point_id' : points_list[i][0],
                        'distributor_id' : points_list[i][1],
                        'station_id' :  points_list[i][2],
                        'charging_rate' : float(points_list[i][3]),
                        'cost_per_kwh' : float(points_list[i][4])
                    })

                return {
                    'msg' : 'available points for admin in a station',
                    'points' : result
                }

        except errors.NotAuthorized as e:
            abort(401, str(e))

        except errors.NoPointsForAdminFound as e:
            abort(400, str(e))
        except IndexError as e:
            abort(400, str(e))


@api.route('/admin/<admin_id>/<user_id>/sub')
class FindContractDetails(Resource):
    @jwt_required()
    def get(self, admin_id, user_id):
        try:
            if (get_jwt_identity() != admin_id):
                raise errors.NotAuthorized

            subs_list = sqlQueries.contract_details_of_user(admin_id, user_id)
            if (len(subs_list) == 0):
                raise errors.NoContractsFound  
              
            else:
                
                result = []
                i = 0
                result.append({
                    "username" :  subs_list[i][0],
                    "first_name" : subs_list[i][1],
                    "last_name" : subs_list[i][2],
                    "email" : subs_list[i][3],
                    "address" : subs_list[i][4] + ", " + subs_list[i][5] + " " + str(subs_list[i][6]) + ", " + str(subs_list[i][7]),
                    "phone" : subs_list[i][8] ,
                    "points" : subs_list[i][9],
                    "last_month_paid_bill" :  str(subs_list[i][10]),
                    "last_month_issued_bill" :  str(subs_list[i][11]),
                    "cost" : float(subs_list[i][12])
                })
            
                return {
                    'msg' : 'Contract Info',
                    'contract' : result
                }
        
        except errors.NullParameter as e:
            abort(400, str(e))

        except errors.NoCarsFound as e:
            abort(400, str(e))

        except errors.NotAuthorized as e:
            abort(401, str(e))
        
        except IndexError: 
            abort(400)  
# --------------------- SUPERADMINS ------------------------


@api.route('/superadmin/system/sessionsupd')
class SuperAdminSessionUpdate(Resource):
    @jwt_required()
    def post(self):
        try:
            file = request.files['sessions']
            if file:
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            else:
                raise errors.FileNotFound

            sqlQueries.sessions_csv(UPLOAD_FOLDER + "/" + filename)

            return {
                'msg' : 'Successfully inserted sessions from csv file'
            }
        except errors.FileNotFound as e:
            abort(400, str(e))

        except mysql.connector.Error as err:
            abort(400, "Something went wrong: {}".format(err))

        except IndexError as e:
            abort(400, str(e))

@api.route('/superadmin/usermod/<username>/<password>')
class SuperAdminUserCreate(Resource):
    @jwt_required()
    def post(self, username, password):
        try:
            if (sqlQueries.check_if_customer(username)):
                boolean = sqlQueries.customer_force_passw(username, password)
                #print('got here')
                if (boolean):
                    return {
                        'msg' : 'Password updated successfully'
                    }
                else:
                    raise errors.IncorrectOldPassword

            else:
                payload = dict(request.form)
                birth_date = payload['birth_date']
                email = payload['email']
                first_name = payload['first_name']
                last_name = payload['last_name']
                phone = payload['phone']
                car_brand = payload['car_brand']
                car_model = payload['car_model']
                city = payload['city']
                street_name = payload['street_name']
                street_number = payload['street_number']
                postal_code = payload['postal_code']
                birth_date_obj = datetime.datetime.strptime(birth_date, '%Y-%m-%d')

                for key in payload:
                    if payload[key] == "":
                        raise errors.NullParameter
                if (not sqlQueries.insert_customer(username,  car_brand, car_model,  password, first_name, last_name,  birth_date_obj, 0, city, street_name, int(street_number), int(postal_code),  Email=email, Phone=int(phone))):
                    raise errors.UserCreationFailed

                return {
                    'msg' : 'User created successfully',
                    'user_id' : username,
                    'email' : payload['email']
                }

        except errors.NullParameter as e:
            abort(400, str(e))

        except errors.UserCreationFailed as e:
            abort(400, str(e))

        except errors.IncorrectOldPassword as e:
            abort(400, str(e))

        except mysql.connector.Error as err:
            abort(400, "Something went wrong: {}".format(err))

        except IndexError:
            abort(400)

@api.route('/superadmin/healthcheck')
class SuperAdminHealthcheck(Resource):
    @jwt_required()
    def get(self):
        try: 
            result = sqlQueries.healthcheck()
            #print(result)
            return {
                'msg' : 'Everything is okay'
            }
        except mysql.connector.Error as err:
            abort(400, "Something went wrong: {}".format(err))
        except IndexError as e:
            abort(400, str(e))

@api.route('/superadmin/resetsessions')
class SuperAdminResetSessions(Resource):
    @jwt_required()
    def post(self):
        try:
            sqlQueries.clear_all_sessions()
            sqlQueries.reset_superadmin()
            return {
                'msg' : 'Successfully reseted sessions'
            }

        except mysql.connector.Error as err:
            abort(400, "Something went wrong: {}".format(err))
        except IndexError as e:
            abort(400, str(e))




@api.route('/superadmin/login')
class SuperAdminLogin(Resource):
    def post(self):
        try:
            payload = dict(request.form)
            username = payload['username']
            password = payload['password']

            for key in payload:
                if payload[key] == "":
                    raise errors.NullParameter

            if (sqlQueries.check_superadmin_login(username, password) == False):
                raise errors.NotValidPassName
            else:
                expires = datetime.timedelta(days=1)
                access_token = create_access_token(identity=username, expires_delta=expires)
                return {
                    'msg' : 'Login Successful',
                    'token' : access_token
                }


        except errors.NullParameter as e:
            abort(400, str(e))

        except errors.NotValidPassName as e:
            abort(401, str(e))

        except mysql.connector.Error as err:
            abort(400, "Something went wrong: {}".format(err))

        except Exception as e:
            abort(400, str(e))



@api.route('/SessionsPerPoint/<point_id>/<yyyymmdd_from>/<yyyymmdd_to>')
class SessionsPerPoint(Resource):
    @jwt_required()
    def get(self, point_id, yyyymmdd_from, yyyymmdd_to):
        try:
            format = request.args.get('format')
            
            sessions = sqlQueries.superadmin_sessions_per_point(point_id, yyyymmdd_from, yyyymmdd_to)
            if (len(sessions) == 0):
               raise errors.NoChargingSessions
            else:
                sessions_list = [list(row) for row in sessions]
                result = []
                total_info = sqlQueries.superadmin_sessions_per_point_sum(point_id, yyyymmdd_from, yyyymmdd_to)
                if (len(total_info) == 0):
                    raise errors.NoChargingSessions

                for i in range(0, len(sessions_list)):
                    result.append({
                        "SessionIndex" : i,
                        "sessionID" : sessions_list[i][0],
                        "start_time" : str(sessions_list[i][2]),
                        "end_time" : str(sessions_list[i][3]),
                        "Protocol" : sessions_list[i][4],
                        "EnergyDelivered" : float(sessions_list[i][5]),
                        "Payment" : str(sessions_list[i][6]),
                        "VehicleType" : sessions_list[i][7]

                    })
                now = datetime.datetime.now()
                final_json =  {
                    'Point' : total_info[0][0],
                    'PointOperator' : total_info[0][1],
                    'RequestTimestamp' : str(now),
                    'PeriodFrom' : yyyymmdd_from,
                    'PeriodTo' : yyyymmdd_to,
                    'NumberOfChargingSessions' : total_info[0][2],
                    'ChargingSessionsList' : result
                }
                if format == "csv":
                    basic = {k: v for k, v in final_json.items() if k != 'ChargingSessionsList'}
                    rows = [{**basic, **session} for session in result]
                    df = pd.DataFrame(rows, columns=list(basic.keys()) + list(result[0].keys()))
                    final_csv = df.to_csv()
                    file = open('SessionsPerPoint.csv', 'w')
                    file.write(final_csv)
                    return final_csv
                
                else:
                    return final_json

        except errors.NoChargingSessions as e:
            abort(400, str(e))

        except mysql.connector.Error as err:
            abort(400, "Something went wrong: {}".format(err))

        except IndexError as e:
            abort(400, str(e))


@api.route('/SessionsPerStation/<station_id>/<yyyymmdd_from>/<yyyymmdd_to>')
class SessionsPerStation(Resource):
    @jwt_required()
    def get(self, station_id, yyyymmdd_from, yyyymmdd_to):
        try:
            format = request.args.get('format')

            sessions = sqlQueries.superadmin_sessions_per_station(station_id, yyyymmdd_from, yyyymmdd_to)
            if (len(sessions) == 0):
               raise errors.NoChargingSessions
            else:
                sessions_list = [list(row) for row in sessions]
                result = []
                total_info = sqlQueries.superadmin_sessions_per_station_sum(station_id, yyyymmdd_from, yyyymmdd_to)
                if (len(total_info) == 0):
                    raise errors.NoChargingSessions
                for i in range(0, len(sessions_list)):
                    result.append({
                        "PointID" : sessions_list[i][0],
                        "PointSessions" : sessions_list[i][1],
                        "EnergyDelivered" : str(sessions_list[i][2])
                    })
                now = datetime.datetime.now()
                final_json = {
                    'StationID' : total_info[0][0],
                    'Operator' : total_info[0][1],
                    'RequestTimestamp' : str(now),
                    'PeriodFrom' : yyyymmdd_from,
                    'PeriodTo' : yyyymmdd_to,
                    'TotalEnergyDelivered' : float(total_info[0][2]),
                    'NumberOfChargingSessions' : total_info[0][3],
                    'NumberOfActivePoints' : total_info[0][4],
                    'SessionsSummaryList' : result
                }

                if format == "csv":
                    basic = {k: v for k, v in final_json.items() if k != 'SessionsSummaryList'}
                    rows = [{**basic, **session} for session in result]
                    df = pd.DataFrame(rows, columns=list(basic.keys()) + list(result[0].keys()))
                    final_csv = df.to_csv()
                    file = open('SessionsPerStation.csv', 'w')
                    file.write(final_csv)
                    return final_csv
                
                else:
                    return final_json
               
               

        except errors.NoChargingSessions as e:
            abort(400, str(e))

        except mysql.connector.Error as err:
            abort(400, "Something went wrong: {}".format(err))

        except IndexError as e:
            abort(400, str(e))

@api.route('/SessionsPerEV/<vehicle_id>/<yyyymmdd_from>/<yyyymmdd_to>')
class SessionsPerCar(Resource):
    @jwt_required()
    def get(self, vehicle_id, yyyymmdd_from, yyyymmdd_to):
        try:
            format = request.args.get('format')

            sessions = sqlQueries.superadmin_sessions_per_EV(vehicle_id, yyyymmdd_from, yyyymmdd_to)
            if (len(sessions) == 0):
               raise errors.NoChargingSessions
            else:
                sessions_list = [list(row) for row in sessions]
                result = []
                total_info = sqlQueries.superadmin_sessions_per_EV_sum(vehicle_id, yyyymmdd_from, yyyymmdd_to)
                if (len(total_info) == 0):
                    raise errors.NoChargingSessions
                for i in range(0, len(sessions_list)):
                    result.append({
                        "SessionIndex" : i,
                        "sessionID" : sessions_list[i][0],
                        "EnergyProvider" : sessions_list[i][1],
                        "Date" : str(sessions_list[i][2]),
                        "StartedOn" : str(sessions_list[i][3]),
                        "FinishedOn" : str(sessions_list[i][4]),
                        "EnergyDelivered" : float(sessions_list[i][5]),
                        "PricePolicyRef" : sessions_list[i][6],
                        "CostPerKWh" : float(sessions_list[i][7]),
                        "SessionCost" : float(sessions_list[i][8])
                    })
                now = datetime.datetime.now()
                final_json =  {
                    'VehicleID' : total_info[0][0],
                    'RequestTimestamp' : str(now),
                    'PeriodFrom' : yyyymmdd_from,
                    'PeriodTo' : yyyymmdd_to,
                    'TotalEnergyConsumed' : float(total_info[0][1]),
                    'NumberOfVisitedPoints' : total_info[0][2],
                    'NumberOfVehicleChargingSessions' : total_info[0][3],
                    'VehicleChargingSessionsList' : result
                }

                if format == 'csv':
                    basic = {k: v for k, v in final_json.items() if k != 'VehicleChargingSessionsList'}
                    rows = [{**basic, **session} for session in result]
                    df = pd.DataFrame(rows, columns=list(basic.keys()) + list(result[0].keys()))
                    final_csv = df.to_csv()
                    file = open('SessionsPerEV.csv', 'w')
                    file.write(final_csv)
                    return final_csv
                
                else:
                    return final_json
               
            
        except errors.NoChargingSessions as e:
            abort(400, str(e))

        except mysql.connector.Error as err:
            abort(400, "Something went wrong: {}".format(err))

        except IndexError as e:
            abort(400, str(e))

@api.route('/SessionsPerProvider/<provider_id>/<yyyymmdd_from>/<yyyymmdd_to>')
class SessionsPerProvider(Resource):
    @jwt_required()
    def get(self, provider_id, yyyymmdd_from, yyyymmdd_to):
        try:
            format = request.args.get('format')
            sessions = sqlQueries.superadmin_sessions_per_provider(provider_id, yyyymmdd_from, yyyymmdd_to)
            if (len(sessions) == 0):
               raise errors.NoStationChargingSessions
            else:
                sessions_list = [list(row) for row in sessions]
                result = []


                for i in range(0, len(sessions_list)):
                    result.append({
                        "ProviderID" : sessions_list[i][0],
                        "StationID" : sessions_list[i][1],
                        "SessionID" : sessions_list[i][2],
                        "VehicleID" : sessions_list[i][3],
                        "Date"      : str(sessions_list[i][4]),
                        "StartedOn" : str(sessions_list[i][5]),
                        "FinishedOn" : str(sessions_list[i][6]),
                        "EnergyDelivered" : float(sessions_list[i][7]),
                        "PricePolicyRef" : sessions_list[i][8],
                        "CostPerkWh" : float(sessions_list[i][9]),
                        "TotalCost" : float(sessions_list[i][10])
                    })
                now = datetime.datetime.now()
                final_json =  {
                    'ProviderChargingSessionList' : result
                }
                
                if (format == 'csv'):
                        basic = {k: v for k, v in final_json.items() if k != 'ProviderChargingSessionList'}
                        rows = [{**basic, **session} for session in result]
                        df = pd.DataFrame(rows, columns=list(basic.keys()) + list(result[0].keys()))
                        final_csv = df.to_csv()
                        file = open('SessionsPerEV.csv', 'w')
                        file.write(final_csv)
                        return final_csv
                else:
                    return final_json

        except errors.NoStationChargingSessions as e:
            abort(400, str(e))

        except mysql.connector.Error as err:
            abort(400, "Something went wrong: {}".format(err))

        except IndexError as e:
            abort(400, str(e))


# --------------------- BOSSSSSSS --------------------------

@api.route('/boss/create')
class CreateBoss(Resource):

    def post(self):
        try:
            payload = dict(request.form)
            boss_no = payload['boss_no']
            password = payload['password']
            birth_date = payload['birth_date']
            email = payload['email']
            first_name = payload['first_name']
            last_name = payload['last_name']
            phone = payload['phone']
            city = payload['city']
            street_name = payload['street_name']
            street_number = payload['street_number']
            postal_code = payload['postal_code']
            working_company = payload['working_company']
            for key in payload:
                if payload[key] == "":
                    raise errors.NullParameter

            birth_date_obj = datetime.datetime.strptime(birth_date, '%Y-%m-%d')

            sqlQueries.insert_boss(boss_no, password, first_name, last_name,  birth_date_obj, working_company, city, street_name, int(street_number), int(postal_code),  0, Email=email, Phone=int(phone))
            return {
                'msg' : 'Boss created successfully',
                'working_company' : payload['working_company'],
                'email' : payload['email']
            }

        except errors.NullParameter as e:
            abort(400, str(e))

        except mysql.connector.Error as err:
            abort(400, "Something went wrong: {}".format(err))

        except IndexError:
            abort(400)


@api.route('/boss/login')
class BossLogin(Resource):
    def post(self):
        try:
            payload = dict(request.form)
            username = payload['username']
            password = payload['password']

            for key in payload:
                if payload[key] == "":
                    raise errors.NullParameter

            if (sqlQueries.check_boss_login(username, password) == False):
                raise errors.NotValidPassName

            else:
                expires = datetime.timedelta(days=1)
                access_token = create_access_token(identity=username, expires_delta=expires)

                return {
                    'msg' : 'Login Successful',
                    'token' : access_token
                }


        except errors.NullParameter as e:
            abort(400, str(e))

        except errors.NotValidPassName as e:
            abort(400, str(e))

        except IndexError:
            abort(400)

@api.route('/boss/<boss_id>/chpwd')
class BossChpwd(Resource):
    @jwt_required()
    def put(self, boss_id):
        try:
            if (get_jwt_identity() != boss_id):
                raise errors.NotAuthorized
            payload = dict(request.form)
            old_password = payload['old_password']
            new_password = payload['new_password']
            for key in payload:
                if payload[key] == "":
                    raise errors.NullParameter

            boolean = sqlQueries.change_boss_password(boss_id, old_password, new_password)


            if (boolean):
                return {
                    'msg' : 'Password updated successfully'
                }
            else:
                raise errors.IncorrectOldPassword


        except errors.NotAuthorized as e:
            abort(401, str(e))

        except errors.NullParameter as e:
            abort(400, str(e))

        except errors.IncorrectOldPassword as e:
            abort(400, str(e))

        except Exception as e:
            abort(400, str(e))

@api.route('/boss/<boss_id>')
class Boss(Resource):
    @jwt_required()
    def delete(self, boss_id):
        try:

            payload = dict(request.form)
            password = payload['password']

            if (sqlQueries.check_boss_login(boss_id, password)):
                sqlQueries.delete_boss(boss_id)

            else:
                raise errors.NotValidPassName
            return {
                'msg': 'Boss deleted successfully'
            }

        except errors.NotValidPassName as e:
            abort(400, str(e))
        except IndexError:
            abort(400)

@api.route('/boss/insert_admin')
class InsertAdmin(Resource):
    @jwt_required()
    def post(self):
        try:
            payload = dict(request.form)
            administrator_no = payload['administrator_no']
            password = payload['password']
            birth_year = payload['birth_year']
            birth_date = payload['birth_date']
            birth_month = payload['birth_month']
            email = payload['email']
            first_name = payload['first_name']
            last_name = payload['last_name']
            phone = payload['phone']
            city = payload['city']
            street_name = payload['street_name']
            street_number = payload['street_number']
            postal_code = payload['postal_code']
            working_company = payload['working_company']

            for key in payload:
                if payload[key] == "":
                    raise errors.NullParameter

            sqlQueries.insert_administrator(administrator_no, password, first_name, last_name,  int(birth_year), int(birth_month), int(birth_date), working_company, city, street_name, int(street_number), int(postal_code),  0, Email=email, Phone=int(phone))
            return {
                'msg' : 'Admin created successfully',
                'working_company' : payload['working_company'],
                'email' : payload['email']
            }

        except errors.NullParameter as e:
            abort(400, str(e))

        except IndexError:
            abort(400)

@api.route('/boss/delete_admin')
class BossDeleteAdmin(Resource):
    @jwt_required()
    def delete(self):
        try:
            payload = dict(request.form)
            boss_no = payload['boss_no']
            password = payload['password']
            administrator_no = payload['administrator_no']
            case = sqlQueries.delete_administrator(boss_no, password, administrator_no)
            if(case == 0):
                raise errors.InvalidCredentials

            elif(case == 1):
                raise errors.AdminNotFound

            elif(case == 2):
                raise errors.AdminNotValid

            elif(case == 3):
                return {
                    'msg' : 'Administrator deleted successfully'
                }

        except errors.InvalidCredentials as e:
            abort(400, str(e))

        except errors.AdminNotFound as e:
            abort(400, str(e))

        except errors.AdminNotValid as e:
            abort(400, str(e))

        except IndexError:
            abort(400)

@api.route('/boss/<boss_id>/show_admins')
class BossShowAdmins(Resource):
    @jwt_required()
    def get(self, boss_id):
        try:
            if (get_jwt_identity() != boss_id):
                raise errors.NotAuthorized

            admin_info = sqlQueries.show_all_admins_on_company(boss_id)
            if(admin_info == []):
                raise errors.NoAdminsFound
            else:
                admin = []
                for i in range(0, len(admin_info)):
                    admin.append({
                        "Administrator_No" : admin_info[i][0],
                        "First_name" : admin_info[i][1],
                        "Last_name" : admin_info[i][2],
                        "Email" : admin_info[i][3],
                        "Phone" : admin_info[i][4]
                    })

                return {
                    'msg' : 'All admins working for your company',
                    'Admins_list' : admin
                }

        except errors.NotAuthorized as e:
            abort(400, str(e))

        except errors.NoAdminsFound as e:
            abort(400, str(e))

        except IndexError:
            abort(400)






# --------------------- CONTRACTS --------------------------

@api.route('/contracts')
class ShowContracts(Resource):
    #@jwt_required()
    def get(self):
        try:
            contracts = sqlQueries.contracts_available()
            #print(contracts)
            if (len(contracts) == 0):
                raise errors.NoAvailableContracts
            else:
                contracts_list = [list(row) for row in contracts]
                result = []

                for i in range(0, len(contracts_list)):
                    result.append({
                        'distributor' : contracts_list[i][0],
                        'price' : float(contracts_list[i][1]),
                        'email' : contracts_list[i][2],
                        'phone' : contracts_list[i][3]

                    })

                return {
                    'msg' : 'available contracts',
                    'contracts' : result
                }

        except errors.NoAvailableContracts as e:
            abort(400, str(e))

        except Exception as e:
            abort(400, str(e))



# ------------------------- CARS --------------------------------


@api.route('/cars')
class ShowCars(Resource):
    def get(self):
        try:
            cars = sqlQueries.findall_cars()
            if (len(cars) == 0):
                raise errors.NoCarsFound
            else:
                cars_list = [list(row) for row in cars]
                result = []

                for i in range(0, len(cars_list)):
                    result.append({
                        'car_id' : cars_list[i][0],
                        'brand' : cars_list[i][1],
                        'model' : cars_list[i][2],
                        'type' : cars_list[i][3],
                        'capacitance' : float(cars_list[i][4]),
                        'release_year' : cars_list[i][5]

                    })

                return {
                    'msg' : 'available cars',
                    'cars' : result
                }

        except errors.NoCarsFound as e:
            abort(400, str(e))

        except Exception as e:
            abort(400, str(e))


@api.route('/car/brands')
class CarBrands(Resource):
    def get(self):
        try:
            brands = sqlQueries.find_brands()
            result = []
            for v in brands:
                result.append({
                    'brand' : v
                })

            return {
                'msg' : 'Successfully returned all brands',
                'brands' : result
            }
        except IndexError:
            abort(400)

@api.route('/car/<brand>/models')
class CarModels(Resource):
    def get(self, brand):
        try:

            models = sqlQueries.find_brand_models(brand)
            result = []
            for v in models:
                result.append({
                    'model' : v
                })

            return {
                'msg' : 'success',
                'models' : result
            }
        except IndexError:
            abort(400)

@api.route('/car/create')
class CreateCar(Resource):
    def post(self):
        try:
            payload = request.json
            car_no = payload['car_no']
            type_car = payload['type']
            brand = payload['brand']
            model = payload['model']
            capacitance = payload['capacitance']
            release_year = payload['release_year']
            
            for key in payload:
                if payload[key] == "":
                    raise errors.NullParameter

            sqlQueries.insert_car(car_no, brand, model, type_car, int(capacitance), release_year)
            return {
                'msg' : 'Car created successfully',
                'car_id' : car_no

            }

        except errors.NullParameter as e:
            abort(400, str(e))

        except Exception as e:
            abort(400, str(e))




# ---------------------- STATIONS -----------------------------------
# show all stations


@api.route('/stations')
class ShowStations(Resource):
    def get(self):
        try:
            stations = sqlQueries.findall_stations()
            if (len(stations) == 0):
                raise errors.NoStations
            else:
                stations_list = [list(row) for row in stations]
                result = []

                for i in range(0, len(stations_list)):
                    result.append({
                        'station_no' : stations_list[i][0],
                        'station_address' : stations_list[i][1] + ", " + str(stations_list[i][2]) + " " + str(stations_list[i][3]),
                        'operator' : stations_list[i][4]

                    })

                return {
                    'msg' : 'available stations',
                    'stations' : result
                }

        except Exception as e:
            abort(400, str(e))

@api.route('/station/create')
class CreateCar(Resource):
    def post(self):
        try:
            payload = request.json
            station_no = payload['station_no']
            city = payload['city']
            street = payload['street']
            number = payload['number']
            operator = payload['operator']
            for key in payload:
                if payload[key] == "":
                    raise errors.NullParameter
            sqlQueries.insert_station(station_no, city, street, number, operator)
            return {
                'msg' : 'station created successfully',
                'station_id' : station_no

            }

        except errors.NullParameter as e:
            abort(400, str(e))

        except Exception as e:
            abort(400, str(e))



# ----------------------- POINTS --------------------------------------
#show all points
@api.route('/points')
class ShowPoints(Resource):
    def get(self):
        try:
            points = sqlQueries.findall_points()
            if (len(points) == 0):
                raise errors.NoPoints
            else:
                points_list = [list(row) for row in points]
                result = []

                for i in range(0, len(points_list)):
                    result.append({
                        'point_id' : points_list[i][0],
                        'distributor_id' : points_list[i][1],
                        'station_id' :  points_list[i][2],
                        'charging_rate' : float(points_list[i][3]),
                        'cost_per_kwh' : float(points_list[i][4])
                    })

                return {
                    'msg' : 'available points',
                    'points' : result
                }

        except errors.NoPoints as e:
            abort(400, str(e))

        except Exception as e:
            abort(400, str(e))


# ------------------------------- Distributor ---------------------


if __name__ == '__main__':
    #app.run()
    app.run(debug=True, port=8765)
    #serve(app, host='127.0.0.1', port=8765,)