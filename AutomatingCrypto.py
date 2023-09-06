from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import os 
from time import time
from time import sleep


def api_runner():
    global df 
    #API FROM THE WEBSITE
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest' 
    parameters = {
    'start':'1',
    'limit':'15',
    'convert':'USD'
    }
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '0ad53085-1cb2-4eb8-ad9e-3ffbd7e56509',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        #print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

    type(data)

    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    #add column with time and date : 
    df = pd.json_normalize(data['data'])
    df['timestamp'] = pd.to_datetime('now')

    #Adding This Infomation to csv file 
    if not os.path.isfile(r"/Users/nahlaburweiss/Desktop/Data Analysis/Auto/API"):
        df.to_csv(r'/Users/nahlaburweiss/Desktop/Data Analysis/Auto/API.csv' , header='column_names' )
    else : 
        df.to_csv(r'/Users/nahlaburweiss/Desktop/Data Analysis/Auto/API.csv' , header=False , mode='a' )
        

#Automation : 

for i in range(333):
    api_runner()
    print('API Runner completed')
    sleep((60*5))
exit()