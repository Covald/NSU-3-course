import requests

from_currency, to_currency = input("Enter currency - ").upper().split()
response = requests.get(
    f"https://free.currconv.com/api/v7/convert?q={from_currency}_{to_currency}&compact=ultra&apiKey=bc92618f4ee2ba5b0f24")
for i in response.json().values():
    print(f"{from_currency}={i}*{to_currency}")
