import sys
import requests

def get_bitcoin_price():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()
        data = response.json()
        return float(data['bpi']['USD']['rate_float'])
    except (requests.RequestException, KeyError, ValueError):
        print("Error: Unable to fetch Bitcoin price.")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Invalid Response")
        sys.exit(1)

    try:
        num_bitcoins = float(sys.argv[1])
    except ValueError:
        print("Number of bitcoins must be a valid number.")
        sys.exit(1)

    bitcoin_price = get_bitcoin_price()
    total_cost = num_bitcoins * bitcoin_price
    print(f"Current cost of {num_bitcoins:,.4f} Bitcoins: ${total_cost:,.4f}")

if __name__ == "__main__":
    main()
