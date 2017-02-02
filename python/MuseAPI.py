import csv
import json
import requests
from apiKey import apiKey

access_token = apiKey

class MuseAPI():
    '''
    This class will be used to interact with the Muse API.
    Request all new job pages from API with specified fields. Return JSON/other workable format.
    '''
    prefix_url = "https://api-v2.themuse.com/"


    def __init__(self,access_token):
        self.access_token = access_token

    def get_request(self,path,params={}):
        params['access_token'] = self.access_token
        url = self.prefix_url + path
        print "URL: ", url
        # Make a request with the given url and parameters
        # Return the JSON form of the request
        r = requests.get(url, params=params)
        return r.json()



def main():
    mapi = MuseAPI(access_token)
    print mapi.get_request("jobs",{"page": 1})

if __name__ == '__main__':
    main()
