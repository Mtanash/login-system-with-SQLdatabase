class User:
    def __init__(self, username=None, email=None, password=None):
        super().__init__()
        self.username = username
        self.email = email
        self.password = password

    def initialise_user(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def remove_user(self):
        self.username = None
        self.email = None
        self.password = None

    def __str__(self):
        return f"user name => {self.username}, email => {self.email}"
