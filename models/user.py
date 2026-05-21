class User:
    def __init__(self, user_id, username, email, password_hash):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password_hash = password_hash

    def __repr__(self):
        return f"User({self.user_id}, {self.username}, {self.email})"