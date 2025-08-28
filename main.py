import os
bidders = {}
any_other = True

# DEBUGG
# inputs = iter(["Milos", "25", "y", "Lukas", "10", "n"])
# def input(prompt=""):
#     val = next(inputs)
#     print(f"{prompt}{val}")
#     return val


while any_other:
    name = input("Write your name: ")
    bid = int(input("Enter your bid: $"))

    bidders[name] = bid
    someone_else = input("Is there someone else who wants to bid? y/n ")
    if someone_else == "n":
        any_other = False
    else:
        os.system("cls" if os.name == "nt" else "clear")


winner = ""
stored_value = 0
for key, value in bidders.items():
    if value > stored_value:
        stored_value = value
        winner = key

os.system("cls" if os.name == "nt" else "clear")
print("="* 50)
print(f"Highest bid was ${stored_value} by {winner}. Congratulations!")
print("="* 50)