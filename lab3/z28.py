class User:
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        self.users[username] = password

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            return "Zalogowano pomyślnie!"
        else:
            return "Błąd logowania."

# Test
u = User()
u.register("user1", "password123")
print(u.login("user1", "password123"))
print(u.login("user1", "wrongpassword"))
