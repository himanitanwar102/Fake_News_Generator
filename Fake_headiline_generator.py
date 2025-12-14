import random

# Categories with data
data = {
    "funny": {
        "subjects": ["Group of Monkeys", "A Cat", "School Teacher", "Funny Youtuber"],
        "actions": ["dances with", "eats", "runs behind", "laughs at"],
        "places": ["a pizza", "a mirror", "inside classroom", "on the road"]
    },
    "political": {
        "subjects": ["Prime Minister", "Opposition Leader", "Government"],
        "actions": ["announces", "criticizes", "approves"],
        "places": ["new policy", "budget plan", "public scheme"]
    },
    "sports": {
        "subjects": ["Virat Kohli", "Indian Team", "Cricket Coach"],
        "actions": ["wins", "loses", "celebrates"],
        "places": ["the final match", "IPL trophy", "practice session"]
    }
}

print("📰 Fake News Headline Generator")
print("Choose category: funny / political / sports")

category = input("Enter category: ").lower().strip()

# Default category handling
if category not in data:
    print("Invalid category, defaulting to funny.")
    category = "funny"

count = 0  # headline counter

while True:
    subject = random.choice(data[category]["subjects"])
    action = random.choice(data[category]["actions"])
    place = random.choice(data[category]["places"])

    headline = f"BREAKING NEWS: {subject} {action} {place}"
    print("\n" + headline)

    count += 1

    choice = input("\nGenerate another headline? (yes/no): ").strip().lower()
    if choice == "no":
        break

print(f"\nTotal headlines generated: {count}")
print("Thanks for using the Fake News Headline Generator 😊")

