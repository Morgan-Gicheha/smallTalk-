users = [
            {"username": "john_doe", "email": "john@example.com", "age": 30},
            {"username": "jane_smith", "email": "jane@example.com", "age": 17},
            {"username": "alice_jones", "email": "alice@example.com", "age": 25},
        ]

class UserProfile:
    def __init__(self, data=None):
        self.data = data

        if data:
            self.username = data.get("username")
            self.email = data.get("email")
            self.age = data.get("age")


    def add_user(self):
        users.append(self.data)
        return {"status": "000", "message": "User added"}

    def get_all_users(self):
        return {"status": "000", "response": users}
