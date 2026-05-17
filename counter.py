running_count = 0

def get_card_value(card):

    if card in ["J", "Q", "K"]:
        return 10

    if card == "A":
        return 11

    return int(card)


def update_running_count(card):

    global running_count

    value = get_card_value(card)

    # Hi-Lo system
    if value in [2,3,4,5,6]:
        running_count += 1

    elif value in [10,11]:
        running_count -= 1

    return running_count