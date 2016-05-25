import requests
import json
from requests.compat import urljoin
import pprint


# api key = 8d9239b1f398f7ea
def get_json():

    home = ('http://api.wunderground.com/api/8d9239b1f398f7ea/')
    current_conditions = ('conditions/')
    future_forecast = ('forecast10day/')
    url_combo1 = (home + current_conditions + future_forecast)
    # print(url_combo1)

    sunrise_sunset = ('astronomy/')
    alerts = ('alerts/')
    active_hurricanes = ('currenthurricane/')
    query = ('q/')
    url_combo2 = (url_combo1 + sunrise_sunset + alerts + active_hurricanes + query)
    # print(url_combo2)

    zip_code = input('Enter zip to check the weather: ')
    zip_code = zip_code+'/'
    # print(zip_code)
    j_son = ('.json')
    url_combo3 = (url_combo2 + zip_code + j_son)
    # print(url_combo3)

    # master_url = urljoin(url_combo1, url_combo2, url_combo3)
    # print("MASTER URL = ", url_combo3)

    response = requests.get(url_combo3)
    # print(response)
    json_data = response.json()
    # pprint.pprint(json_data)
    # json_parsed = json.loads(json_data)
    # pprint.pprint(json_parsed)


    print("Current Temperature: {}".format(json_data['current_observation']['temp_f']))

    print("Sunrise at {} ".format(json_data['sun_phase']['sunrise']))
    print("Sunset at {}".format(json_data['sun_phase']['sunset']))# print(value)/
    print("There are {} active hurricanes".format(json_data['currenthurricane']))

# dict(zip([1, 3], [2, 4]))
    # for key in json_data:
    #     pprint.pprint(key['forecast'])#['currenthurricane']['alers']['sun_phase']['moon_phase']['current_observation']

get_json()
