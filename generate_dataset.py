import pandas as pd
import random

data = []

for i in range(50000):

    player_total = random.randint(4, 21)

    dealer_card = random.randint(1, 11)

    running_count = random.randint(-10, 10)

    # Simulated blackjack logic

    score = (
        player_total * 2
        + running_count * 3
        - dealer_card
    )

    # Win or Lose

    result = 1 if score > 28 else 0

    data.append([
        player_total,
        dealer_card,
        running_count,
        result
    ])

df = pd.DataFrame(
    data,
    columns=[
        "player_total",
        "dealer_card",
        "running_count",
        "result"
    ]
)

df.to_csv(
    "data/blackjack_dataset.csv",
    index=False
)

print("Dataset Created Successfully")