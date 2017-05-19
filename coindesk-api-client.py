import requests
from datetime import date,timedelta

coindeskApi = "http://api.coindesk.com/v1/bpi/"

def get_currencies():
    coindeskCurrencies = requests.get(coindeskApi + "supported-currencies.json").json()
    currencyList = []
    for dict in coindeskCurrencies:
        currencyList.append(dict["currency"])
    return currencyList

def get_current_price(currency):
    return float(requests.get(coindeskApi + "currentprice/" + currency + ".json").json()["bpi"][currency]["rate"] \
        .replace(",", ""))

def get_historical_price(
        currency
        , start=date.today()-timedelta(days=31)
        , end=date.today()
        ):
    startString = "%02d" % start.year + "-" + "%02d" % start.month + "-" + "%02d" % start.day
    endString = "%02d" % end.year + "-" + "%02d" % end.month + "-" + "%02d" % end.day
    return requests.get(coindeskApi + "historical/close.json?currency=" + currency + "&start=" + startString +  "&end=" + endString).json()["bpi"]

