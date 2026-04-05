import json

with open("codebook_data_2.json","r") as file:
    data = json.load(file)

print("User and friends")
for user in data["users"]:
    print(f"User ID: {user["id"]} Friends: {user["friends"]}")

user_friends = {}

for user in data["users"]:
    user_friends[user["id"]] = set(user["friends"])

suggestion = set()
for user in data["users"]:
    print(f"User ID: {user["id"]}")
    for friend in user["friends"]: 
        for mutual in user_friends[friend]:
            if mutual != user["id"] and mutual not in user_friends[user["id"]]:
                suggestion.add(mutual)
                print(suggestion)
    user["suggestions"] = suggestion
    suggestion = set()

for user in data["users"]:
    print(f"User ID: {user["id"]} Suggested friends: {user["suggestions"] if user["suggestions"] else "None"}")