import csv
import json
import requests

access_token = "" #get this from muse api

class MuseAPI():
    '''
    This class will be used to interact with the Muse API.
    Request all new job pages from API with specified fields. Return JSON/other workable format.
    '''

    def __init__(self,access_token):
        self.access_token = access_token
