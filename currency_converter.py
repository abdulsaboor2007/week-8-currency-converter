import requests

print("===== CURRENCY CONVERTER =====")

try:
    amount = float(input("Enter amount: "))
    from_currency = input("Convert from (example USD): ").strip().upper()
    to_currency = input("Convert to (example PKR): ").strip().upper()

    if amount < 0:
        print("Amount cannot be negative.")
    elif from_currency == "" or to_currency == "":
        print("Currency code cannot be empty.")
    elif from_currency == to_currency:
        print("Converted amount:", amount, to_currency)
    else:
        url = f"https://api.frankfurter.dev/v2/rate/{from_currency}/{to_currency}"
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()
            exchange_rate = data["rate"]
            converted_amount = amount * exchange_rate

            print("\n===== CONVERSION RESULT =====")
            print("Rate date:", data["date"])
            print("1", from_currency, "=", exchange_rate, to_currency)
            print(amount, from_currency, "=", round(converted_amount, 2), to_currency)
        else:
            print("Currency code was not found.")

except ValueError:
    print("Please enter a valid numeric amount.")
except requests.exceptions.RequestException:
    print("Internet or API connection error.")
