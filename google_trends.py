from pytrends.request import TrendReq

def get_latest_trending_words():
    pytrends = TrendReq(hl='en-US', tz=360)
    kw_list = ["Blockchain", "AI"]
    pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')
    pytrends.interest_over_time()
    print(pytrends)
    # pytrends = TrendReq(hl='en-US', tz=360, timeout=(10,25), proxies=['https://34.203.233.13:80',], retries=2, backoff_factor=0.1, requests_args={'verify':False})

if __name__ == "__main__":
    trending_words = get_latest_trending_words()
    print("Latest trending words from Google:")
    # for idx, word in enumerate(trending_words, 1):
    #     print(f"{idx}. {word}")
