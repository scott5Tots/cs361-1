from flask import Flask, request, jsonify
from forex_python.converter import CurrencyRates, CurrencyCodes

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_currency():
    data = request.json
    amount = data['amount']
    from_currency = data['from_currency']
    to_currency = data['to_currency']

    c = CurrencyRates()
    try:
        converted_amount = c.convert(from_currency, to_currency, amount)
        return jsonify({"converted_amount": converted_amount})
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(port=5000)