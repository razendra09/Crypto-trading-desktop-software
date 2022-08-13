import logging
import requests

logger = logging.getLogger()

# Get the Latest Market Data of Various Coins Pairs
def get_contracts():
    response_object = requests.get("https://fapi.binance.com/fapi/v1/exchangeInfo")

    contracts = []

    for contract in response_object.json()['symbols']:
        contracts.append(contract['pair'])

        return contracts

print(get_contracts())
