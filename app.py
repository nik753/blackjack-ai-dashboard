import streamlit as st

from counter import update_running_count
from predictor import predict_blackjack

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Blackjack AI Dashboard",
    layout="wide"
)

# -----------------------------------
# CASINO TABLE STYLE
# -----------------------------------

st.markdown(
    """
    <style>

    .stApp {
        background-color: #0b3d0b;
        color: white;
    }

    h1, h2, h3 {
        color: white;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------------
# SESSION STATE
# -----------------------------------

if "running_count" not in st.session_state:
    st.session_state.running_count = 0

if "card_history" not in st.session_state:
    st.session_state.card_history = []

if "player_cards" not in st.session_state:
    st.session_state.player_cards = []

# -----------------------------------
# TITLE
# -----------------------------------

st.title("♠ Blackjack AI Dashboard")

st.markdown(
    "### Real-Time Card Counting & ML Prediction"
)

st.markdown("---")

# -----------------------------------
# CARD OPTIONS
# -----------------------------------

cards = [
    "A","2","3","4","5","6",
    "7","8","9","0",
    "J","Q","K"
]

# -----------------------------------
# TOP DASHBOARD
# -----------------------------------

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Running Count",
        st.session_state.running_count
    )

with col2:

    st.metric(
        "Cards Played",
        len(st.session_state.card_history)
    )

with col3:

    deck_strength = (
        "Strong"
        if st.session_state.running_count > 3
        else "Neutral"
        if st.session_state.running_count >= 0
        else "Weak"
    )

    st.metric(
        "Deck Strength",
        deck_strength
    )

st.markdown("---")

# -----------------------------------
# MAIN LAYOUT
# -----------------------------------

left, right = st.columns([2,1])

# ===================================
# LEFT SIDE
# ===================================

with left:

    st.subheader("🎴 Blackjack Table")

    # -------------------------------
    # PLAYER CARD INPUT
    # -------------------------------

    selected_player_card = st.selectbox(
        "Add Your Card",
        cards,
        key="player"
    )

    if st.button("Add Player Card"):

        st.session_state.player_cards.append(
            selected_player_card
        )

        count = update_running_count(
            selected_player_card
        )

        st.session_state.running_count = count

        st.session_state.card_history.append(
            selected_player_card
        )

    # -------------------------------
    # PLAYER CARDS DISPLAY
    # -------------------------------

    st.markdown("## Your Cards")

    card_cols = st.columns(
        max(1, len(st.session_state.player_cards))
    )

    for i, card in enumerate(
        st.session_state.player_cards
    ):

        with card_cols[i]:

            suit = "S"

            card_code = f"{card}{suit}"

            image_path = (
                f"cards/{card_code}.png"
            )

            st.image(
                image_path,
                width=120
            )

    # -------------------------------
    # PLAYER TOTAL
    # -------------------------------

    total = 0

    aces = 0

    for card in st.session_state.player_cards:

        if card in ["J","Q","K"]:

            total += 10

        elif card == "A":

            total += 11

            aces += 1

        else:

            total += int(card)

    while total > 21 and aces > 0:

        total -= 10

        aces -= 1

    st.metric(
        "Player Total",
        total
    )

    st.markdown("---")

    # -------------------------------
    # DEALER CARD
    # -------------------------------

    dealer_card = st.selectbox(
        "Dealer Visible Card",
        cards
    )

    st.markdown("## Dealer Card")

    dealer_suit = "H"

    dealer_code = (
        f"{dealer_card}{dealer_suit}"
    )

    dealer_path = (
        f"cards/{dealer_code}.png"
    )

    st.image(
        dealer_path,
        width=120
    )

# ===================================
# RIGHT SIDE
# ===================================

with right:

    st.subheader("🤖 AI Dashboard")

    st.markdown("### Card History")

    st.write(
        st.session_state.card_history
    )

    st.markdown("---")

    # -------------------------------
    # DEALER VALUE
    # -------------------------------

    dealer_value = (
        10
        if dealer_card in ["J","Q","K"]
        else 11
        if dealer_card == "A"
        else int(dealer_card)
    )

    # -------------------------------
    # AI PREDICTION
    # -------------------------------

    if st.button("Predict Move"):

        result, probability = predict_blackjack(
            total,
            dealer_value,
            st.session_state.running_count
        )

        st.metric(
            "AI Win Probability",
            f"{probability}%"
        )

        # ---------------------------
        # CONFIDENCE BAR
        # ---------------------------

        if probability >= 70:

            st.progress(100)

        elif probability >= 50:

            st.progress(65)

        else:

            st.progress(30)

        # ---------------------------
        # AI RESULT
        # ---------------------------

        if probability >= 70:

            st.success(
                "✅ AI Says: RAISE"
            )

        elif probability >= 50:

            st.warning(
                "⚠ AI Says: PLAY CAREFULLY"
            )

        else:

            st.error(
                "❌ AI Says: PACK"
            )

        # ---------------------------
        # MOVE SUGGESTION
        # ---------------------------

        if total >= 17:

            st.info(
                "Suggested Move: STAND"
            )

        elif total <= 11:

            st.info(
                "Suggested Move: HIT"
            )

        else:

            st.info(
                "Suggested Move: ANALYZE"
            )

    st.markdown("---")

    # -------------------------------
    # RESET BUTTON
    # -------------------------------

    if st.button("Reset Table"):

        st.session_state.running_count = 0

        st.session_state.card_history = []

        st.session_state.player_cards = []

        st.rerun()