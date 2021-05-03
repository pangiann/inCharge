#!/usr/bin/env python3
import sys
import os
import json
import datetime
import requests
import urllib
import pandas as pd
from os.path import expanduser
from io import StringIO

base_url = "http://127.0.0.1:8765/evcharge/api"

# implement --format and --apikey in parameters

if (len(sys.argv) == 1):
    print("Try using 'ev_group17 --help' for information about the use the program.")

elif (sys.argv[1] == '--help'):
    if (len(sys.argv) == 2):
        print("Usage: 'ev_group17 SCOPE [--param1 value1 --param2 value2 ...]'")
        print("\n\nSCOPE value can be:")
        print("\nhealthcheck \t\t(Checks and acknowledges end-to-end connectivity)")
        print("resetsessions \t\t(Initialises charging sessions as well as default administrator)")
        print("login \t\t\t(Start session)")
        print("logout \t\t\t(Stop session)")
        print("SessionsPerPoint \t(Charging point's sessions between two dates)")
        print("SessionsPerStation \t(Charging station's sessions between two dates)")
        print("SessionsPerEV \t\t(Sessions between two dates involving a car model)")
        print("SessionsPerProvider \t(Sessions between two dates involving a provider)")
        print("Admin \t\t\t(Administrative functions)")
        print("\n'--format' and '--apikey' parameters must be provided")

# healthcheck implementation needed
elif (sys.argv[1] == 'healthcheck'):
    parameters = ['--format', '--apikey']
    if (len(sys.argv) == 6):
        if (sys.argv[2] in parameters and sys.argv[4] in parameters and sys.argv[2]!=sys.argv[4]):
            if (sys.argv[2] == '--format'):
                format = sys.argv[3]
                apikey = sys.argv[5]
            else:
                format = sys.argv[5]
                apikey = sys.argv[3]
            url = base_url + '/superadmin/healthcheck'
            headers = {'Authorization':'Bearer '+apikey}
            try:
                response = requests.request("GET", url, headers=headers)
                if (response.status_code == 200):
                    if (format == 'json'):
                        output = '{"status":"OK"}'
                    elif (format == 'csv'):
                        output = 'status\nOK'
                    else:
                        output = 'Unrecognizable format'
                else:
                    if (format == 'json'):
                        output = '{"status":"failed"}'
                    elif (format == 'csv'):
                        output = 'status\nfailed'
                    else:
                        output = '--format must be either \'json\' or \'csv\''
            except:
                if (format == 'json'):
                    output = '{"status":"failed"}'
                elif (format == 'csv'):
                    output = 'status\nfailed'
                else:
                    output = '--format must be either \'json\' or \'csv\''
    else:
        output = "Usage: 'ev_group17 healthcheck --format [json/csv] --apikey [apikey]'"
    print('')
    print(output)

# make reset_sessions api
# connect with reset_sessions api
elif (sys.argv[1] == 'resetsessions'):
    parameters = ['--format', '--apikey']
    if (len(sys.argv) == 6):
        if (sys.argv[2] in parameters and sys.argv[4] in parameters and sys.argv[2]!=sys.argv[4]):
            if (sys.argv[2] == '--format'):
                format = sys.argv[3]
                apikey = sys.argv[5]
            else:
                format = sys.argv[5]
                apikey = sys.argv[3]
            url = base_url+'/superadmin/resetsessions'
            headers = {'Authorization':'Bearer '+apikey}
            response = requests.request("POST", url, headers=headers)
            #print(response)
            if (response.status_code == 200):
                if (format == 'json'):
                    output = '{"status":"OK"}'
                elif (format == 'csv'):
                    output = 'status\nOK'
                else:
                    output = 'Unrecognizable format'
            else:
                if (format == 'json'):
                    output = '{"status":"failed"}'
                elif (format == 'csv'):
                    output = 'status\nfailed'
                else:
                    output = '--format must be either \'json\' or \'csv\''
        else:
            output = "Usage: 'ev_group17 resetsessions --format [json/csv] --apikey [apikey]'"
    else:
        output = "Usage: 'ev_group17 resetsessions --format [json/csv] --apikey [apikey]'"
    print('')
    print(output)


elif (sys.argv[1] == 'login'):
    args = ['--format', '--username', '--passw']
    try:
        tmp = [2,4,6]
        given = [sys.argv[i] for i in tmp]
    except:
        pass

    if ((len(sys.argv)==8) and all(item in args for item in given) and all(item in given for item in args)):
        for i in range(len(sys.argv)):
            if (sys.argv[i] == '--username'):
                username = sys.argv[i+1]
            elif (sys.argv[i] == '--passw'):
                password = sys.argv[i+1]
            elif (sys.argv[i] == '--format'):
                format = sys.argv[i+1]
        url = base_url+"/superadmin/login"
        payload = {'username' : username, 'password' : password}
        payload = urllib.parse.urlencode(payload)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        response = requests.request("POST", url, headers=headers, data=payload)
        response = response.json()
        try:
            msg = response['msg']
        except KeyError:
            msg = response['message']
        except:
            msg = "Error"

        if (msg == 'Login Successful' and format in ['json','csv']):  # check for credentials from api
            home = expanduser("~")
            file = open(home+'/softeng20bAPI.token', 'w')
            token = response['token']
            file.write(token)   # replace with proper token
            file.close()
            file = open(home+'/softeng20bAPI.username','w')
            file.write(username)
            file.close()
            if (format == 'json'):
                output = '{"token":"'+token+'"}'
            elif (format == 'csv'):
                output = 'token\n'+token
        else:
            if (format == 'json'):
                output = '{"login":"failed"}'
            elif (format == 'csv'):
                output = 'login\nfailed'
            else:
                output = '--format must be either \'json\' or \'csv\''
    else:
        output = "Usage: 'ev_group17 login --username [your_username] --passw [your_passw] --format [json/csv]'"
    print('')
    print(output)

# check if token is valid for the given user
elif (sys.argv[1] == 'logout'): # only if user has valid token
    args = ['--format','--apikey']
    tmp = [2,4]
    try:
        given = [sys.argv[i] for i in tmp]
    except:
        pass

    if ((len(sys.argv) == 6) and all(item in args for item in given) and all(item in given for item in args)):
        for i in range(len(sys.argv)):
            if (sys.argv[i] == '--apikey'):
                apikey = sys.argv[i+1]
            elif (sys.argv[i] == '--format'):
                format = sys.argv[i+1]
        if (format in ['json','csv']):
            home = expanduser('~')
            try:
                os.remove(home+'/softeng20bAPI.token')
                os.remove(home+'/softeng20bAPI.username')
                if (format == 'json'):
                    output = '{"logout":"OK"}'
                elif (format == 'csv'):
                    output = 'logout\nOK'
                else:
                    output = 'unreachable'
            except FileNotFoundError:
                if (format == 'json'):
                    output = '{"logout":"failed"}'
                elif (format == 'csv'):
                    output = 'logout\nfailed'
                else:
                    output = 'unreachable'
            except:
                output = 'unreachable'
        else:
            if (format == 'json'):
                output = '{"logout":"failed"}'
            elif (format == 'csv'):
                output = 'logout\nfailed'
            else:
                output = '--format must be either \'json\' or \'csv\''
    else:
        output = "Usage: 'ev_group17 logout --format [json/csv] --apikey [apikey]'"
    print('')
    print(output)


elif (sys.argv[1] == 'SessionsPerPoint'):
    args = ['--point', '--datefrom', '--dateto', '--format', '--apikey']
    try:
        tmp = [2,4,6,8,10]
        given = [sys.argv[i] for i in tmp]
    except:
        pass
    if ((len(sys.argv)==12) and all(item in args for item in given) and all(item in given for item in args)):
        for i in range(len(sys.argv)):
            if (sys.argv[i] == '--point'):
                point = sys.argv[i+1]
            elif (sys.argv[i] == '--datefrom'):
                datefrom = sys.argv[i+1]
            elif (sys.argv[i] == '--dateto'):
                dateto = sys.argv[i+1]
            elif (sys.argv[i] == '--format'):
                format = sys.argv[i+1]
            elif (sys.argv[i] == '--apikey'):
                apikey = sys.argv[i+1]
        datefrom = datetime.datetime.strptime(datefrom, '%Y-%m-%d').date()
        dateto = datetime.datetime.strptime(dateto, '%Y-%m-%d').date()

        if (format in ['json','csv']):
            url = base_url+'/SessionsPerPoint/'+point+'/'+str(datefrom)+'/'+str(dateto)+'?format='+format
            response = requests.request("GET", url, headers = {'Authorization':'Bearer '+apikey})
            if (response.status_code == 200):
                response = response.json()
                output = response
            else:
                if (format == 'json'):
                    output = '{"status":"failed"}'
                elif (format == 'csv'):
                    output = 'status\nfailed'
                else:
                    output = 'Unreachable'
        else:
            output = '--format must be either \'json\' or \'csv\''
    else:
        output = "Usage: 'ev_group17 SessionsPerPoint --point [Point_ID] --datefrom [%Y-%m-%d] --dateto [%Y-%m-%d] --format [json/csv] --apikey [apikey]'"
    print('')
    print(output)

elif (sys.argv[1] == 'SessionsPerStation'):
    args = ['--station', '--datefrom', '--dateto', '--format', '--apikey']
    try:
        tmp = [2,4,6,8,10]
        given = [sys.argv[i] for i in tmp]
    except:
        pass
    if ((len(sys.argv)==12) and all(item in args for item in given) and all(item in given for item in args)):
        for i in range(len(sys.argv)):
            if (sys.argv[i] == '--station'):
                station = sys.argv[i+1]
            elif (sys.argv[i] == '--datefrom'):
                datefrom = sys.argv[i+1]
            elif (sys.argv[i] == '--dateto'):
                dateto = sys.argv[i+1]
            elif (sys.argv[i] == '--format'):
                format = sys.argv[i+1]
            elif (sys.argv[i] == '--apikey'):
                apikey = sys.argv[i+1]
        datefrom = datetime.datetime.strptime(datefrom, '%Y-%m-%d').date()
        dateto = datetime.datetime.strptime(dateto, '%Y-%m-%d').date()

        if (format in ['json','csv']):
            url = base_url+'/SessionsPerStation/'+station+'/'+str(datefrom)+'/'+str(dateto)+'?format='+format
            response = requests.request("GET", url, headers = {'Authorization':'Bearer '+apikey})
            if (response.status_code == 200):
                response = response.json()
                output = response
            else:
                if (format == 'json'):
                    output = '{"status":"failed"}'
                elif (format == 'csv'):
                    output = 'status\nfailed'
                else:
                    output = 'Unreachable'
        else:
            output = '--format must be either \'json\' or \'csv\''
    else:
        output = "Usage: 'ev_group17 SessionsPerStation --station [Station_ID] --datefrom [%Y-%m-%d] --dateto [%Y-%m-%d] --format [json/csv] --apikey [apikey]'"
    print('')
    print(output)

elif (sys.argv[1] == 'SessionsPerEV'):
    args = ['--ev', '--datefrom', '--dateto', '--format', '--apikey']
    try:
        tmp = [2,4,6,8,10]
        given = [sys.argv[i] for i in tmp]
    except:
        pass
    if ((len(sys.argv)==12) and all(item in args for item in given) and all(item in given for item in args)):
        for i in range(len(sys.argv)):
            if (sys.argv[i] == '--ev'):
                ev = sys.argv[i+1]
            elif (sys.argv[i] == '--datefrom'):
                datefrom = sys.argv[i+1]
            elif (sys.argv[i] == '--dateto'):
                dateto = sys.argv[i+1]
            elif (sys.argv[i] == '--format'):
                format = sys.argv[i+1]
            elif (sys.argv[i] == '--apikey'):
                apikey = sys.argv[i+1]
        datefrom = datetime.datetime.strptime(datefrom, '%Y-%m-%d').date()
        dateto = datetime.datetime.strptime(dateto, '%Y-%m-%d').date()

        if (format in ['json','csv']):
            url = base_url+'/SessionsPerEV/'+ev+'/'+str(datefrom)+'/'+str(dateto)+'?format='+format
            response = requests.request("GET", url, headers = {'Authorization':'Bearer '+apikey})
            if (response.status_code == 200):
                response = response.json()
                output = response
            else:
                if (format == 'json'):
                    output = '{"status":"failed"}'
                elif (format == 'csv'):
                    output = 'status\nfailed'
                else:
                    output = 'Unreachable'
        else:
            output = '--format must be either \'json\' or \'csv\''
    else:
        output = "Usage: 'ev_group17 SessionsPerEV --ev [EV_ID] --datefrom [%Y-%m-%d] --dateto [%Y-%m-%d] --format [json/csv] --apikey [apikey]'"
    print('')
    print(output)

elif (sys.argv[1] == 'SessionsPerProvider'):
    args = ['--provider', '--datefrom', '--dateto', '--format', '--apikey']
    try:
        tmp = [2,4,6,8,10]
        given = [sys.argv[i] for i in tmp]
    except:
        pass
    if ((len(sys.argv)==12) and all(item in args for item in given) and all(item in given for item in args)):
        for i in range(len(sys.argv)):
            if (sys.argv[i] == '--provider'):
                provider = sys.argv[i+1]
            elif (sys.argv[i] == '--datefrom'):
                datefrom = sys.argv[i+1]
            elif (sys.argv[i] == '--dateto'):
                dateto = sys.argv[i+1]
            elif (sys.argv[i] == '--format'):
                format = sys.argv[i+1]
            elif (sys.argv[i] == '--apikey'):
                apikey = sys.argv[i+1]
        datefrom = datetime.datetime.strptime(datefrom, '%Y-%m-%d').date()
        dateto = datetime.datetime.strptime(dateto, '%Y-%m-%d').date()

        if (format in ['json','csv']):
            url = base_url+'/SessionsPerProvider/'+provider+'/'+str(datefrom)+'/'+str(dateto)+'?format='+format
            response = requests.request("GET", url, headers = {'Authorization':'Bearer '+apikey})

            if (response.status_code == 200):
                response = response.json()
                output = response
            else:
                if (format == 'json'):
                    output = '{"status":"failed"}'
                elif (format == 'csv'):
                    output = 'status\nfailed'
                else:
                    output = 'Unreachable'
        else:
            output = '--format must be either \'json\' or \'csv\''
    else:
        output = "Usage: 'ev_group17 SessionsPerProvider --provider [Provider_ID] --datefrom [%Y-%m-%d] --dateto [%Y-%m-%d] --format [json/csv] --apikey [apikey]'"
    print('')
    print(output)



elif (sys.argv[1] == 'Admin'):
    # create superadmin or change his password
    if (len(sys.argv)==2):
        print("Usage: 'ev_group17 Admin [--function] [--parameters]'")
        print("\nfunctions supported:")
        print("\t--usermod\t\t\t\t\t\t(Changes superadmin's password or creates a superadmin if one with this username does not exist)")
        print("\t\twith parametes:\n\n\t\t--username [username] --passw [password] --old_passw [old_password] --apikey [apikey] --format [json/csv]\n\t\t\tfor changing user's password")
        print("\n\t\tor\n")
        print("\t\t--username [username] --passw [password] --birth_date [%Y-%m-%d] --first_name [name] --last_name [surname] --phone [phone number]\n\
        \t--car_brand [brand] --car_model [model] --city [city] --street_name [street] --street_number [number] --postal_code [code] --apikey [apikey] --format [json/csv]")
        print("\t\t\tfor creating user")
        print("\n\n\t--users --apikey [apikey] --format [json/csv]\t\t(Returns token for connected superadmin)")
        print("\n\n\t--sessionsupd\t\t\t\t\t\t(Import charging session data from csv file specified to database)")
        print("\t\twith parameters:\n\t\t--source [filename] --apikey [apikey] --format [json/csv]")
    elif (sys.argv[2] == '--usermod'):
        args_upd = ['--username', '--passw', '--apikey', '--format']
        args_cre = ['--username', '--passw', '--birth_date', '--first_name', '--last_name', '--phone', '--car_brand', '--car_model', '--city', '--street_name',\
         '--street_number', '--postal_code', '--apikey', '--format', '--email']
        try:
            tmp_upd = [3,5,7,9]
            tmp_cre = [3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]
            given_upd = [sys.argv[i] for i in tmp_upd]
            given_cre = [sys.argv[i] for i in tmp_cre]
        except:
            pass

        if ((len(sys.argv)==11) and all(item in args_upd for item in given_upd) and all(item in given_upd for item in args_upd)):
            for i in range(len(sys.argv)):
                if (sys.argv[i] == '--username'):
                    username = sys.argv[i+1]
                elif (sys.argv[i] == '--passw'):
                    password = sys.argv[i+1]
                elif (sys.argv[i] == '--apikey'):
                    apikey = sys.argv[i+1]
                elif (sys.argv[i] == '--format'):
                    format = sys.argv[i+1]


            url = base_url+'/superadmin/usermod/'+username+'/'+password
            headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization':'Bearer '+apikey}
            response = requests.request("POST", url, headers=headers)
            if (response.status_code != 200):
                if (format == 'json'):
                    output = '{"status":"failed"}'
                elif (format == 'csv'):
                    output = 'status\nfailed'
                else:
                    output = 'Unrecognizable format'
            else:
                if (format == 'json'):
                    output = '{"status":"password updated"}'
                elif (format == 'csv'):
                    output = "status\npassword updated"
                else:
                    output = "Unrecognizable format"
            print('')
            print(output)

        elif ((len(sys.argv)==33) and all(item in args_cre for item in given_cre) and all(item in given_cre for item in args_cre)):
            for i in range(len(sys.argv)):
                if (sys.argv[i] == '--username'):
                    username = sys.argv[i+1]
                elif (sys.argv[i] == '--passw'):
                    password = sys.argv[i+1]
                elif (sys.argv[i] == '--birth_date'):
                    birth_date = sys.argv[i+1]
                elif (sys.argv[i] == '--email'):
                    email = sys.argv[i+1]
                elif (sys.argv[i] == '--first_name'):
                    first_name = sys.argv[i+1]
                elif (sys.argv[i] == '--last_name'):
                    last_name = sys.argv[i+1]
                elif (sys.argv[i] == '--phone'):
                    phone = sys.argv[i+1]
                elif (sys.argv[i] == '--car_brand'):
                    car_brand = sys.argv[i+1]
                elif (sys.argv[i] == '--car_model'):
                    car_model = sys.argv[i+1]
                elif (sys.argv[i] == '--city'):
                    city = sys.argv[i+1]
                elif (sys.argv[i] == '--street_name'):
                    street_name = sys.argv[i+1]
                elif (sys.argv[i] == '--street_number'):
                    street_number = sys.argv[i+1]
                elif (sys.argv[i] == '--postal_code'):
                    postal_code = sys.argv[i+1]
                elif (sys.argv[i] == '--apikey'):
                    apikey = sys.argv[i+1]
                elif (sys.argv[i] == '--format'):
                    format = sys.argv[i+1]

            url = base_url+"/superadmin/usermod/"+username+'/'+password
            payload = {'birth_date':birth_date,'first_name':first_name,'last_name':last_name,'phone':phone,'car_brand':car_brand,'car_model':car_model,\
             'city':city,'street_name':street_name,'street_number':street_number,'postal_code':postal_code, 'email':email}
            payload = urllib.parse.urlencode(payload)
            headers = {'Content-Type': 'application/x-www-form-urlencoded','Authorization':'Bearer '+apikey}

            response = requests.request("POST", url, headers=headers, data=payload)
            if (response.status_code != 200):
                if (format == 'json'):
                    output = '{"status":"failed"}'
                elif (format == 'csv'):
                    output = 'status\nfailed'
                else:
                    output = "Unrecognizable format"
            else:
                if (format == 'json'):
                    output = '{"status":"user created"}'
                elif (format == 'csv'):
                    output = 'status\nuser created'
                else:
                    output = "Unrecognizable format"
            print('')
            print(output)
        else:
            output = "For correct usage see 'ev_group17 Admin'"
            print('')
            print(output)

    elif (sys.argv[2] == '--users'):
        args = ['--format', '--apikey']
        temp = [3,5]
        try:
            given_args = [sys.argv[i] for i in temp]
        except:
            pass
        if ((len(sys.argv)==7) and all(item in args for item in given_args) and all(item in given_args for item in args)):
            for i in range(len(sys.argv)):
                if (sys.argv[i] == '--format'):
                    format = sys.argv[i+1]
                elif (sys.argv[i] == '--apikey'):
                    apikey = sys.argv[i+1]
            try:
                home = expanduser("~")
                file = open(home+'/softeng20bAPI.username', 'r')
                username = file.read()
                file.close()
                file = open(home+'/softeng20bAPI.token', 'r')
                token = file.read()
                file.close()
                if (token == apikey):
                    if (format == 'json'):
                        output = '{"'+username+'":"'+token+'"}'
                    elif (format == 'csv'):
                        output = username+'\n'+token
                    else:
                        output = "Unrecognizable format"
                else:
                    if (format == 'json'):
                        output = '{"status":"failed"}'
                    elif (format == 'csv'):
                        output = 'status\nfailed'
                    else:
                        output = "Unrecognizable format"
            except:
                if (format == 'json'):
                    output = '{"status":"failed"}'
                elif (format == 'csv'):
                    output = 'status\nfailed'
                else:
                    output = "Unrecognizable format"
        else:
            output = "For correct usage see 'ev_group17 Admin'"
        print('')
        print(output)


    elif (sys.argv[2] == '--sessionsupd'):
        args = ['--format','--apikey', '--source']
        temp = [3,5,7]
        try:
            given_args = [sys.argv[i] for i in temp]
        except:
            pass
        if ((len(sys.argv)==9) and all(item in args for item in given_args) and all(item in given_args for item in args)):
            for i in range(len(sys.argv)):
                if (sys.argv[i] == '--format'):
                    format = sys.argv[i+1]
                elif (sys.argv[i] == '--apikey'):
                    apikey = sys.argv[i+1]
                elif (sys.argv[i] == '--source'):
                    file = sys.argv[i+1]
            try:
                url = base_url+"/superadmin/system/sessionsupd"
                payload={}
                files=[('sessions',('Sessions.csv',open(file,'rb'),'text/csv'))]
                headers = {'Authorization': 'Bearer '+apikey}
                response = requests.request("POST", url, headers=headers, data=payload, files=files)
                # do something with response?
                if (format == 'json'):
                    output = '{"status":"success"}'
                elif (format == 'csv'):
                    output = 'status\nsuccess'
                else:
                    output = "Unrecognizable format"
            except:
                if (format == 'json'):
                    output = '{"status":"failed"}'
                elif (format == 'csv'):
                    output = 'status\nfailed'
                else:
                    output = "Unrecognizable format"
        else:
            output = "For correct usage see 'ev_group17 Admin'"
        print('')
        print(output)

    else:
        print("Unrecognizable command. Try using 'ev_group17 --help' for information about the use the program.")

else:
    print("Unrecognizable command. Try using 'ev_group17 --help' for information about the use the program.")
