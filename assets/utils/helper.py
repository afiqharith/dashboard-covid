from os import stat
from random import randrange
import pandas as pd
import datetime
import urllib
from urllib.request import urlopen
import json

URL_DEPLOY = "https://api-covid19-malaysia.herokuapp.com/"
URL_DEBUG = "http://127.0.0.1:5000/"

class DataHandler:
    def __init__(self, state):
        self.response1 = urlopen("{0}epidemic/cases?state={1}&start_date={2}".format(URL_DEPLOY, urllib.parse.quote(state), "2022-01-01")).read()
        self.response_case = self.method_data(json.loads(self.response1))

        self.response2 = urlopen("{0}epidemic/deaths?state={1}&start_date={2}".format(URL_DEPLOY, urllib.parse.quote(state), "2022-01-01")).read()
        self.response_death = self.method_data(json.loads(self.response2))

    def method_data(self, unpack_json):
        return unpack_json["data"][0]

