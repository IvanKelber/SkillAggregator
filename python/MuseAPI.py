import csv
import json
import requests
import sys
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
        self.specs = {"page":0,"access_token" : self.access_token}

    def get_request(self,path,params={}):
        url = self.prefix_url + path
        # print "URL: ", url
        # Make a request with the given url and parameters
        # Return the JSON form of the request
        r = requests.get(url, params=params)
        return r.json()



    def get_first_jobs_page(self):
        self.setSpec("page",10)
        return self.get_request("jobs",self.specs)


    def get_first_n_pages(self,n=sys.maxint):
        self.setSpec("page",0)
        total_results = []
        while(self.specs["page"] < n):
            print "Collecting page: " + str(self.specs["page"])
            self.setSpec("page",self.specs["page"]+1)
            jobs = self.get_request("jobs",self.specs)
            try:
                total_results += jobs["results"]
            except KeyError:
                break

        return total_results


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
    mapi.setSpec("category",["Engineering","Data Science"])
    data = mapi.get_first_n_pages(1)
    with open('../data/muse_jobs.json','wb') as muse_jobs:
        json.dump(data,muse_jobs,indent=4)


    # print mapi.get_request("jobs",mapi.specs)

if __name__ == '__main__':
    main()
