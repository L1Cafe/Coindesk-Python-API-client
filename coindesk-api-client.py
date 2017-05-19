import requests
from datetime import date, timedelta

coindeskApi = "http://api.coindesk.com/v1/bpi/"


def get_currencies():
    coindesk_currencies = requests.get(coindeskApi + "supported-currencies.json").json()
    currency_list = []
    for currency in coindesk_currencies:
        currency_list.append(currency["currency"])
    return currency_list


def get_current_price(currency):
    return float(requests.get(coindeskApi + "currentprice/" + currency + ".json").json()["bpi"][currency]["rate"]
                 .replace(",", ""))


def get_historical_price(
        currency,
        start=date.today()-timedelta(days=31),
        end=date.today()
        ):
    start_string = "%02d" % start.year + "-" + "%02d" % start.month + "-" + "%02d" % start.day
    end_string = "%02d" % end.year + "-" + "%02d" % end.month + "-" + "%02d" % end.day
    return requests.get(f"{coindeskApi}historical/close.json?"
                        f"currency={currency}&start={start_string}&end={end_string}") \
                        .json()["bpi"]
