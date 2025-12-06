# 1 - import the random module
import random

# 2 - create subjects
subjects = [
    "Shahrukh Khan",
    "Virat Kohli",
    "Nirmala Sitharaman",
    "Prime Minister",
    "Salman Khan",
    "Pakistan people",
    "Group of Monkeys"
]

actions = [
    "launches",
    "orders",
    "dances with",
    "eats",
    "declares war on",
    "celebrates",
    "sings with"
]



places_or_things = [
    "Delhi pollution",
    "a plate of samosa",
    "inside parliament",
    "at India Gate",
    "during IPL match",
    "at Ganga Ghat",
    "at Rajwada Palace in Indore"
]

# 3 - start the headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)

    user_input = input("\nDo you want another headline? (yes/no)").strip().lower()
    if user_input == "no":
        break

# print goodbye message
print("\nThanks for using the Fake News Headline Generator. Have a fun day!")
