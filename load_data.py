import json

with open("codebook_data.json","r") as file:
    data = json.load(file)

print("Friends and Connections")
for user in data["users"]:
    print(f"name: {user["name"]} (id: {user["id"]}) - Friends: {user["friends"]} - Liked pages: {user["liked_pages"]} ")


print("Pages")
for page in data["pages"]:
    print(f"id: {page['id']} - Name: {page["name"]}")
