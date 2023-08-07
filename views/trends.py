from dotenv import load_dotenv
import os
from serpapi import GoogleSearch
import requests
import json
from flask import request, jsonify, Blueprint

from views.openai_view import get_openai_response

load_dotenv()
serpapi_api_key = os.getenv("SERPAPI_P_KEY")

# data_type: TIMESERIES, GEO_MAP, GEO_MAP_0, RELATED_TOPICS, RELATED_QUERIES

# Playground
# https://serpapi.com/playground?engine=google_trends&q=volcano&data_type=RELATED_QUERIES



serpapi_bp = Blueprint('serpapi', __name__)
@serpapi_bp.route('/')
def status():
    return jsonify({"status": "active"})

@serpapi_bp.route('/serpapi')
def get_trends():
    return jsonify({"status": "active"})

# status_type = rising | top
def get_related_queries(keywords:str, status_type:str):
    params = {
        "engine": "google_trends",
        "q": keywords,
        "data_type": "RELATED_QUERIES",
        "api_key": "f2519cfbe9a6ffed3dd087b4edee2170a8481a92f0092b5a4ccceb818c7e2dd9"
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    related_queries = [i["query"] for i in results["related_queries"][status_type]]
    # related_queries = [i["query"] for i in results["related_queries"]["top"]]
    return related_queries
