

class Credentials:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password


class User:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name


class Posts:
    def __init__(self, posts: list):
        self.posts = posts


users = [
    Credentials("demo@gmail.com", "1000"),
    Credentials("abd@gmail.com", "1001"),
    Credentials("uzr@gmail.com", "1002"),
    Credentials("qmr@gmail.com", "1003"),
    Credentials("hmz@gmail.com", "1004"),
    Credentials("shanz@gmail.com", "1005"),
]

user_names = [
    User("Alexa", ""),
    User("Abdullah", "Nadeem"),
    User("Uzair", "Nadeem"),
    User("Qamar", "Siddiqui"),
    User("Hamzah", "Syed"),
    User("Shanzey", "Shah"),
]

posts = [
    Posts(["Post-1", "Post-2"]),
    Posts(["Post-1", "Post-2", "Post-3", "Post-4", "Post-5"]),
    Posts(["Post-1", "Post-2", "Post-3", "Post-4"]),
    Posts(["Post-1", "Post-2"]),
    Posts(["Post-1", "Post-2", "Post-3"]),
    Posts(["Post-1", "Post-2", "Post-3", "Post-4", "Post-5", "Post-6"]),
]


def login(email: str, password: str):
    for index, user in enumerate(users):
        if user.email == email and user.password == password:
            print(f"✅ Login successful for {email}")
            return index  
    print("❌ Invalid credentials")
    return None


email = input("Enter your email: ")
password = input("Enter your password: ")

user_index = login(email, password)  

def get_posts(user_index):
    if user_index is not None:
        user = user_names[user_index] 
        user_posts = posts[user_index].posts  
        print(f"\nWelcome back, {user.first_name}!")
        print("Your Posts:")
        for post in user_posts:
            print(f"- {post}")
    else:
        print("\n❌ Access Denied! Please login first.")


get_posts(user_index)  
