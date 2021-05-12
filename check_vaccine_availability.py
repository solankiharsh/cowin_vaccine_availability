import requests
import datetime
import pprint
import time

main_server_api = "https://cdn-api.co-vin.in/api"
states =  "/v2/admin/location/states"
district_id = "/v2/admin/location/districts"
searchbypin = "/v2/appointment/sessions/public/findByPin"
searchbydistrict = "/v2​/appointment​/sessions​/public​/findByDistrict"
calendarbypin = "/v2/appointment/sessions/public/calendarByPin"
calendarbydistrict = "/v2/appointment/sessions/public/calendarByDistrict"

headers_api = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}

todays_date = datetime.datetime.now().strftime("%d-%m-%Y")

# Enter Your Pin address and district_id_pin  
my_pin = 452002
my_district = 314

print('##################### SEARCHING IN YOUR PIN ADDRESS FOR TODAY ###############################\n')

searchbypin_response = requests.get(f'{main_server_api}{searchbypin}',params={'pincode':my_pin,'date':todays_date}, headers=headers_api)
if str(searchbypin_response) == '<Response [200]>':
    searchbypin_response_json = searchbypin_response.json()
    if len(searchbypin_response_json['sessions']) > 0:
        for session in searchbypin_response_json['sessions']:
            print(f"Date : {session['date']}")
            print(f"vaccine is: {session['vaccine']} and total vaccine available : {session['available_capacity']}")
            print(f"fees for vaccine is: {session['fee']}")
            print(f"minimum age required is: {session['min_age_limit']}")
            print(f"it is available from {session['from']} to {session['to']} in the time slot : {session['slots']}")
            print(f"the center_name is: {session['name']}, center_id is : {session['center_id']}, center_address is : {session['address']},")
            print(f"Block_name : {session['block_name']}, Pincode : {session['pincode']}, District_name :{session['district_name']}, State : {session['state_name']}")
            print("\n\n")
            time.sleep(1.5)
    else:
        print("You cannot get vaccinated today. No slots available.")
        
print('##################### SEARCHING IN YOUR PIN ADDRESS FOR NEXT SEVEN DAYS ###############################\n')
calendarbypin_response = requests.get(f'{main_server_api}{calendarbypin}',params={'pincode':my_pin,'date':todays_date}, headers=headers_api)
if str(searchbypin_response) == '<Response [200]>':
    calendarbypin_response_json = calendarbypin_response.json()
    if len(calendarbypin_response_json['centers']) > 0:
        for center in calendarbypin_response_json['centers']:
            for session in center['sessions']:
                print(f"Date : {session['date']}")
                print(f"vaccine is: {session['vaccine']} and total vaccine available are : {session['available_capacity']}")
                print(f"fees for vaccine is: {center['fee_type']}")
                print(f"minimum age required is: {session['min_age_limit']}")
                print(f"it is available from {center['from']} to {center['to']} in the time slot : {session['slots']}")
                print(f"the center_name is: {center['name']}, center_id is : {center['center_id']}, center_address is : {center['address']},")
                print(f"Block_name : {center['block_name']}, Pincode : {center['pincode']}, District_name :{center['district_name']}, State : {center['state_name']}")
                print("\n\n")
                time.sleep(1.5)

    else:
        print("You cannot get vaccinated for next 7 days. No slots available.")

print('##################### SEARCHING IN YOUR DISRICT FOR NEXT SEVEN DAYS ###############################\n')
calendarbydistrict_response = requests.get(f'{main_server_api}{calendarbydistrict}',params={'district_id':my_district,'date':todays_date}, headers=headers_api)

if str(calendarbydistrict_response) == '<Response [200]>':
    calendarbydistrict_response_json = calendarbydistrict_response.json()
    if len(calendarbydistrict_response_json['centers']) > 0:
        for center in calendarbydistrict_response_json['centers']:
            for session in center['sessions']:
                print(f"Date : {session['date']}")
                print(f"vaccine is: {session['vaccine']} and total vaccine available are : {session['available_capacity']}")
                print(f"fees for vaccine is: {center['fee_type']}")
                print(f"minimum age required is: {session['min_age_limit']}")
                print(f"it is available from {center['from']} to {center['to']} in the time slot : {session['slots']}")
                print(f"the center_name is: {center['name']}, center_id is : {center['center_id']}, center_address is : {center['address']},")
                print(f"Block_name : {center['block_name']}, Pincode : {center['pincode']}, District_name :{center['district_name']}, State : {center['state_name']}")
                print("\n\n")
                time.sleep(1.5)

    else:
        print("You cannot get vaccinated for next 7 days. No slots available.")