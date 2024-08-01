# Day 17: Creating Classes

class User:

    def __init__(self, user_id, username):
        print("new user being created...")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Hanna")
print(f"{user_1.id}: {user_1.username}")

user_2 = User("002", "Zane")
print(f"{user_2.id}: {user_2.username}")

print("")
user_1.follow(user_2)
print(f"{user_1.id}: {user_1.username} has {user_1.following} following, and {user_1.followers} followers.")
print(f"{user_2.id}: {user_2.username} has {user_2.following} following, and {user_2.followers} followers.")
