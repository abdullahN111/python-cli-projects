


currency_exchange_rates = {
    "USD": 1,  # Base currency
    "EUR": 0.92,
    "PKR": 278,
    "INR": 83.30,
    "BTK": 109.50,
    "AUD": 1.52,
    "TRY": 32.08,
    "CNY": 7.23,
    "SAR": 3.75,
    "QAR": 3.65,
    "KWD": 0.31,
    "AED": 3.67
}


print("\n<--Welcome to Currency Exchange Rates Market-->")
print("Enter the currency code you want to convert.\n")

while True:
    amount = int(input("Enter the amount you want to convert: "))
    from_currency = input("From which currency you want to conver: ").upper()
    to_currency = input("To which currency you want to conver: ").upper()
    
    for key, value in currency_exchange_rates.items():
        