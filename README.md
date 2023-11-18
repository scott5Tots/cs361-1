# cs361
Software Engineering 1
Fall term 2023<br>

To make HTTP requests to converter.py, implement the code below: <br>

```
import requests

def convert_currency(amount, from_currency, to_currency):
    url = "http://localhost:5000/convert"
    data = {
        "amount": amount,
        "from_currency": from_currency,
        "to_currency": to_currency
    }
    response = requests.post(url, json=data)
    if response.ok:
        return response.json()['converted_amount']
    else:
        return "Error: " + response.json().get('error', 'Unknown error')

def main():
    amount = float(input("Enter the amount you want to convert: "))
    from_currency = input("From Currency (e.g., 'USD', 'EUR'): ").upper()
    to_currency = input("To Currency (e.g., 'USD', 'EUR'): ").upper()
    result = convert_currency(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} is {result} in {to_currency}")

if __name__ == "__main__":
    main()

```
