from database import Database
from user import User
from getpass import getpass


class App:
    def __init__(self, database=None, current_user=None):
        super().__init__()
        self.database = database
        self.current_user = current_user
        self.get_databse_info_from_user()

    def get_databse_info_from_user(self):
        db_username = input("Enter database username: ")
        db_password = getpass("Enter database password: ")
        db_name = input("Enter database name: ")
        self.initialise_values(db_username, db_password, db_name)

    def initialise_values(self, db_username, db_password, db_name):
        self.database = Database()
        self.current_user = User()
        self.database.connect_to_database(db_username, db_password, db_name)

    def main(self):
        while True:
            user_input = input("Enter command: ").lower()
            if user_input == "exit":
                break
            elif user_input == "login":
                self.database.login(input("Enter username: "),
                                    getpass("Enter password: "))
            elif user_input == "logout":
                if self.database.current_user:
                    self.database.current_user.remove_user()
                print("There is no current user logged in!")
            elif user_input == "register":
                self.database.register(input("Enter username: "),
                                       input("Enter email: "),
                                       getpass("Enter password: "))
            elif user_input == "print_user":
                print(self.database.current_user)
            else:
                print("Enter a valid command!")


app = App()
app.main()
