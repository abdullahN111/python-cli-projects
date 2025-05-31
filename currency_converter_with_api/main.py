from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://api.freecurrencyapi.com/"
API_KEY = "fca_live_eppQEbZqiPXRfqAACBXdfVTZcpV2ixmeteokEBIA"

printer = PrettyPrinter()

def get_currencies():

    endpoint = f"v1/latest?apikey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()["data"]
    data = list(data.items())
    data.sort()
    
    return data
    
def print_currency(currencies):
    for code, currency in currencies:
        print(f"{code}: {currency}")
        
        
def exchange_rate(base_currency, to_currencies):
    endpoint = f"v1/latest?apikey={API_KEY}&base_currency={base_currency}&currencies={to_currencies}"
    url = BASE_URL + endpoint
    response = get(url)
    data = response.json()
    
    if "data" not in data or to_currencies not in data["data"]:
        print("Invalid Currencies")
        return
    
    data = data["data"][to_currencies] 
    print(f"\n{base_currency} > {to_currencies} = {data}")
    
    return data
    


def convert(base_currency, to_currencies, amount):
    rate = exchange_rate(base_currency, to_currencies)
    if rate is None:
        return
    
    try:
        amount = float(amount)
        
    except:
        print("Invalid amount!")
        
    converted_amount = rate * amount
    print(f"{amount}:{base_currency} is equal to {converted_amount}:{to_currencies}")
    return converted_amount

def main():
    currencies = get_currencies()
   
    print("\n<-Welcome to the Currency Converter->\n")
    print("1. List all currencies.")
    print("2. Convert from one currency to another.")
    print("3. Get the exchange rate of two currencies.")
    
    while True:
        command = input("\nEnter a command or press q to quit: ").lower()
        
        if command == "q":
            break
        
        elif command == "1":
            print("\n*All Currencies*\n")
            print_currency(currencies)
        
        elif command == "2":
            base = input("\nEnter base currency: ").upper()
            amount = input("Enter an amount in base currency: ")
            to = input("Enter to currency: ").upper()
            convert(base, to, amount)
            
        elif command == "3":
            base = input("\nEnter base currency: ").upper()
            to = input("Enter to currency: ").upper()    
            exchange_rate(base, to)       
            
        else:
            print("Invalid Command!")  


main()    
        