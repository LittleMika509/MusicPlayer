users = ["Mark", "Tom", "Bob", "Alice", "Tom", "Bill", "Tom", "Alex", "Shaun", "Mark"]

Tom = users.count("Tom")
Mark = users.count("Mark")
Alice = users.count("Alice")
John = users.count("John")

users.pop(2)
for user in users:
    if user == "Tom":
        users.remove("Tom")
    else:
        users = users
print(users)




