from dotenv import load_dotenv
import os
from serpapi import GoogleSearch
import requests
import json

load_dotenv()
serpapi_api_key = os.getenv("SERPAPI_P_KEY")

# data_type: TIMESERIES, GEO_MAP, GEO_MAP_0, RELATED_TOPICS, RELATED_QUERIES

# Playground
# https://serpapi.com/playground?engine=google_trends&q=volcano&data_type=RELATED_QUERIES


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

def call_open_ai_api(dataInput:str):
    requestData = {
        "prompt": "Create a 200 lines article about the following:" + "\n" + dataInput,
        "engine": "text-davinci-003",
        "password": "aeZak1939pska"
    }
    headers = {
        'Content-Type': 'application/json'
    }
    # print(headers)
    # print(requestData)
    response = requests.post('https://eric-sales-bot.onrender.com/chat', headers=headers, json=requestData)
    # print(response.content)
    content = response.content
    response_content_str = content.decode('utf-8')
    data = json.loads(response_content_str)
    return data


if __name__ == "__main__":
    keyword = input("Enter Keyword to search: ")
    related_queries = get_related_queries(keyword, 'rising')

    print("\n Rising Searches:")
    for i, query in enumerate(related_queries):
        print(f"{i} : {query}")
    choice = int(input("enter choice: "))
    open_api_response = call_open_ai_api(related_queries[choice])["response"]
    print(open_api_response)

# pip install google-serp-api
# pip install google-search-results
# https://serpapi.com/search.json?engine=google_trends&q=coffee,milk,bread,pasta,steak&data_type=TIMESERIES