from cgitb import reset
import imp
from unittest import result
from flask import render_template
from flask import Blueprint
from flask import request
import json
import datetime
from .utils.helper import DataHandler

views = Blueprint("views", __name__)

states =["Johor", "Kedah", "Kelantan", "Melaka", "Negeri Sembilan", "Pahang", "Perak", "Perlis", "Pulau Pinang", "Sabah", "Sarawak", "Selangor", "Terengganu", "W.P. Kuala Lumpur", "W.P. Labuan", "W.P. Putrajaya"]

@views.route("/index", methods=["GET"])
@views.route("/", methods=["GET"])
def index():
    if request.method == "GET":
        cases = list()
        deaths = list()
        
        for state in states:
            cases.append(DataHandler(state).response_case)
            deaths.append(DataHandler(state).response_death)
        return render_template("index.html", title = "Dashboard", year=datetime.datetime.now().strftime("%Y"), cases = cases, deaths=deaths)