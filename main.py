"""
Blind Auction Project
--------------------
This script runs a simple blind auction in the command line.
Participants enter their names and bids, and the highest bidder wins.
The auction continues until no more participants wish to bid.
"""

import os

bidders = {}
any_other = True

# FOR QUICK DEBUG
# inputs = iter(["Milos", "25", "y", "Lukas", "10", "n"])
# def input(prompt=""):
#     val = next(inputs)
#     print(f"{prompt}{val}")
#     return val


# Collect bids from participants until no more want to bid
while any_other:
    name = input("Write your name: ")
    bid = int(input("Enter your bid: $"))

    bidders[name] = bid
    someone_else = input("Is there someone else who wants to bid? y/n ")
    if someone_else == "n":
        any_other = False
    else:
        # Clear the screen for the next bidder
        os.system("cls" if os.name == "nt" else "clear")


# Find the highest bid and determine the winner
winner = ""
stored_value = 0
for key, value in bidders.items():
    if value > stored_value:
        stored_value = value
        winner = key


# Announce the winner
os.system("cls" if os.name == "nt" else "clear")
print("=" * 50)
print(f"Highest bid was ${stored_value} by {winner}. Congratulations!")
print("=" * 50)
