royal = {'J', 'Q', 'K', 'A'}

def tenaize(player_cards):
    ace = False
    pair = False
    if player_cards[0] in royal:
        player_cards[0] = 10
        if player_cards[0] == 'A':
            ace = True
    if player_cards[1] in royal:
        player_cards[1] = 10
        if player_cards[1] == 'A':
            ace = True
        pair = player_cards[0] == player_cards[1]
    return (player_cards, ace, pair)

def table(player_sum, aceFlag, pairFlag, delaer_card):
    if not aceFlag:
        if (player_sum >= 17 or (player_sum == 16

def main():
    player_cards = (0,0)
    start = ""
    while (start != "start"):
        start = input("Hi! welcome to blackjack assistant!\nPlease hit start to begin")
    print("Awesome! Let's begin\n Please note that royal cards goes by their first letter.\nFor eaxample, King will 'K'")
    while (1):
        player_cards[0] = input("Whats your first card?")
        dealer_card = input("Whats the dealer's first card?")
        player_cards[1] = input("Whats your second card?")
        tmp = tenaize (player_cards)
        res = table(tmp[0][0] + tmp[0][1], tmp[1], tmp[2], dealer_card)
