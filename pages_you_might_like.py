import json

with open("codebook_data_2.json","r") as file:
    data = json.load(file)

# print(data["users"])

liked_pages = {}

print("User liked pages")
for user in data["users"]:
    print(f"User ID: {user["id"]} Liked pages: {user["liked_pages"]}")
    liked_pages[user["id"]] = user["liked_pages"]

# print(liked_pages)
suggested_pages = {}

for current_user in data["users"]:
    suggested_pages[current_user["id"]] = []
    for current_user_page in current_user["liked_pages"]:
        for other_user in data["users"]:
            for other_user_page in other_user["liked_pages"]:
                if other_user_page == current_user_page and current_user["id"] != other_user["id"]:
                    suggested_pages[current_user["id"]] = other_user["liked_pages"]
                    
# print(suggested_pages)

for user in data["users"]:
    user["suggested_pages"] = [page for page in suggested_pages[user["id"]] if page not in liked_pages[user["id"]]]

# print(data["users"])

print("\nUser suggested pages")
for user in data["users"]:
    print(f"User ID: {user["id"]} Suggested_pages: {user["suggested_pages"]}")