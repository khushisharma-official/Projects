import random

subjects = [
    "Michelle Obama",
    "Lionel Messi",
    "Lewis Hamilton",
    "Brad Pitt",
    "Donald Trump",
    "Ariana Grande"
]

actions = [
    "sells fruits",
    "danced like barbie",
    "sang baby shark",
    "slept",
    "ate loudly",
    "cracked a joke"
]

objects = [
    "at the street",
    "at the sofi stadium",
    "on obama's lap",
    "at the parliament",
    "at the toilet seat",
    "at my home last night"
]

while True:
    sub = random.choice(subjects)
    act = random.choice(actions)
    obj = random.choice(objects)

    headline = f"BREAKING NEWS : {sub} {act} {obj}"
    print("\n" + headline)

    user_input = input("\n Do you want to continue (yes/no) : ").strip().lower()

    if user_input == "no":
        break


print("\n Thanks for using the Fake Headline generator. Have a good day!")