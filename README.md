# DASHBOARD COVID19 MALAYSIA

[![MOH](https://img.shields.io/badge/Epidemic_Reference-MOH_Public_Data-orange)](https://github.com/MoH-Malaysia/covid19-public)
[![CITF](https://img.shields.io/badge/Vaccination_Reference-CITF_Malaysia_Public_Data-blue)](https://github.com/CITF-Malaysia/citf-public)
[![GitHub](https://img.shields.io/badge/API_GitHub_Reference-API_Covid_MY-black)](https://github.com/afiqharith/api-covid-malaysia)

<div align="center" style="border:solid; border-size: 0.4vmin; border-color:black">
  <img src="assets/public/images/web.png">
</div>

### 1. To run locally in Python3 environment

Run:

```sh
$ pip3 install -r requirements.txt
$ python3 wsgi.py
```

### 2. To run locally in Docker

Run:

```sh
$ docker build -t dashboardcovidmy .
$ docker run -p 5000:5000 -d dashboardcovidmy .
```

### 3. Deployment

[![render](https://img.shields.io/badge/Dashboard_Covid_MY-render-088F8F)](https://dashboard-covidmy.onrender.com)
