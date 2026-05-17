import os
import requests

# CREATE cards folder

os.makedirs("cards", exist_ok=True)

# CARD VALUES

values = [
    "A","2","3","4","5","6",
    "7","8","9","0",
    "J","Q","K"
]

# SUITS

suits = ["S","H","D","C"]

# DOWNLOAD ALL CARDS

for value in values:

    for suit in suits:

        card = f"{value}{suit}"

        url = f"https://deckofcardsapi.com/static/img/{card}.png"

        response = requests.get(url)

        with open(f"cards/{card}.png", "wb") as file:

            file.write(response.content)

        print(f"Downloaded {card}")

print("All cards downloaded successfully!")