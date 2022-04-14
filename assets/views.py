from .utils.helper import StateDataHandler, NationDataHandler
from flask import render_template
from flask import Blueprint
from flask import request
import datetime

views = Blueprint("views", __name__)

@views.route("/index", methods=["GET"])
@views.route("/", methods=["GET"])
def index():
    if request.method == "GET":
        data_state = StateDataHandler()
        data_nation = NationDataHandler()
        return render_template("index.html", title = "Dashboard", year = datetime.datetime.now().strftime("%Y"), state_cases = data_state.case, state_deaths = data_state.death, nation_cases = data_nation.case, nation_deaths = data_nation.death)
        # return render_template("index.html", title = "Dashboard", year = datetime.datetime.now().strftime("%Y"), state_cases = [], state_deaths = [], nation_cases = data_nation.case, nation_deaths = data_nation.death)