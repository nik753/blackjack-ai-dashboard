import joblib

# LOAD TRAINED MODEL

model = joblib.load(
    "blackjack_ai.pkl"
)

def predict_blackjack(
    player_total,
    dealer_card,
    running_count
):

    prediction = model.predict(
        [[
            player_total,
            dealer_card,
            running_count
        ]]
    )

    probability = model.predict_proba(
        [[
            player_total,
            dealer_card,
            running_count
        ]]
    )

    win_probability = (
        probability[0][1] * 100
    )

    return (
        prediction[0],
        round(win_probability, 2)
    )