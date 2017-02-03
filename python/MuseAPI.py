import csv
import json
import requests
from apiKey import apiKey

access_token = apiKey

class MuseAPI:
    '''
    This class will be used to interact with the Muse API.
    Request all new job pages from API with specified fields. Return JSON/other workable format.
    '''
    prefix_url = "https://api-v2.themuse.com/"
    default_fields = ["page","company","level","category","location"]

    def __init__(self,access_token):
        self.access_token = access_token
        self.specs = {"page":0}

    def get_request(self,path,params={}):
        params['access_token'] = self.access_token
        url = self.prefix_url + path
        print "URL: ", url
        # Make a request with the given url and parameters
        # Return the JSON form of the request
        r = requests.get(url, params=params)
        return r.json()



    def get_first_jobs_page(self):
        self.setSpec("page",10)
        return self.get_request("jobs",self.specs)


    def get_all_jobs(self):
        self.setSpec("page",0)
        results = self.get_request("jobs",self.specs)
        while(len(results["results"]) > 0):
            print len(results)
            self.setSpec("page",self.specs["page"]+1)
            results = self.get_request("jobs",self.specs)



    def setSpec(self,specification,value):
        '''
        specification: string
        value: primitive/string
        '''
        self.specs[specification] = value

    def setSpecs(self,specs):
        '''
        specs: dictionary (string : primitive/string)
        '''
        for k,v in specs.items():
            self.specs[k] = v



def main():
    mapi = MuseAPI(access_token)
    print mapi.get_all_jobs()
    # print mapi.get_request("jobs",mapi.specs)

if __name__ == '__main__':
    main()
