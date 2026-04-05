import json

with open("codebook_data.json","r") as file:
    data = json.load(file)

data["users"] = [user for user in data["users"] if user["name"].strip()]

for user in data["users"]:
    user["friends"] = list(set(user["friends"]))

data["users"] = [user for user in data["users"] if user["friends"] or user["liked_pages"]]

print(data["users"])

unique_pages = {}

for page in data["pages"]:
    unique_pages[page["id"]] = page

data["pages"] = list(unique_pages.values())

print(data["pages"])

json.dump(data,open("codebook_data_2.json","w"),indent=4)
