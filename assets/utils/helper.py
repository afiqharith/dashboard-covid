from urllib.request import urlopen
import datetime
import json

DEBUG = False

if DEBUG:
    URL = "http://localhost:5000/"
else:
    URL = "https://api-covidmy.onrender.com/"

class StateDataHandler:
    def __init__(self):
        self.available_date = self.method_validate_date()
        self.response1 = urlopen("{0}epidemic/cases?state=all&start_date={1}".format(URL, self.available_date)).read()
        self.response2 = urlopen("{0}epidemic/deaths?state=all&start_date={1}".format(URL, self.available_date)).read()
        self.case, self.death = self.method_data(json.loads(self.response1)), self.method_data(json.loads(self.response2))

    def method_data(self, unpack_json):
        return unpack_json["data"]

    def method_validate_date(self):
        _response = urlopen("{0}epidemic/cases?state=all&start_date={1}".format(URL, datetime.datetime.now().strftime("%Y-%m-%d"))).read()

        if "failed" in str(_response):
            return (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
        else:
            return datetime.datetime.now().strftime("%Y-%m-%d")

class NationDataHandler:
    def __init__(self) -> None:
        self.available_date = self.method_validate_date()
        self.response1 = urlopen("{0}epidemic/cases?start_date={1}".format(URL, self.available_date)).read()
        self.response2 = urlopen("{0}epidemic/deaths?start_date={1}".format(URL, self.available_date)).read()
        self.case, self.death = self.method_data(json.loads(self.response1)), self.method_data(json.loads(self.response2))

    def method_data(self, unpack_json):
        return unpack_json["data"][0]

    def method_validate_date(self):
        _response = urlopen("{0}epidemic/cases?start_date={1}".format(URL, datetime.datetime.now().strftime("%Y-%m-%d"))).read()

        if "failed" in str(_response):
            return (datetime.datetime.now() + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
        else:
            return datetime.datetime.now().strftime("%Y-%m-%d")

if __name__ == "__main__":
    app1 = StateDataHandler()
    print(type(app1.case))

    app2 = NationDataHandler()
    print(type(app2.case))
