
#This helper function generates a attractive heading based on what's passed in
def heading_generator(heading):
    print(f"\n\n{heading} -----------------\n\n")

#This helper function simulates and returns cards that are allowed in the atm system
def allowed_cards_system():
    cards = [
        {"card_number": "1888-8888-8888", "pin": "8888"},
        {"card_number": "1233-3338-8682", "pin": "0120"},
        {"card_number": "1001-4522-2299", "pin": "2288"},
        {"card_number": "4218-8419-1006", "pin": "4110"},
        {"card_number": "2010-2012-2026", "pin": "9931"},
    ]

    return cards

#This helper function asks for a user's pin and checks if it's valid
def ask_for_pin(card):

    print(f"\n\tEnter your pin below.")
    pin = input("\tPin: ")

    if pin.isdigit():
         
    else:
        print(f"\t{pin} isn't a valid pin. Try again")

def read_inserted_card(card):
    allowed_cards = allowed_cards_system()

    if card in allowed_cards["card_number"]:
        pin = ask_for_pin(card)
    else:
        print(f"\tYour card is not allowed. --Eject Card")


#1. ATM withdrawal system
def atm_withdrawal_system():
    heading_generator("1.  ATM withdrawal system")
    card = read_inserted_card("1888-8888-8888")

#This function loads all of the programs for task 4
def task_4():
    atm_withdrawal_system()

task_4()