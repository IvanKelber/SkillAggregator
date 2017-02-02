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

    def __init__(self,access_token):
        self.access_token = access_token



def main():
    mapi = MuseAPI(access_token)

if __name__ == '__main__':
    main()
