from user import User
from mysql.connector import connect, Error
from getpass import getpass


class Database:
    def __init__(self, user=None, password=None, database_name=None, current_user=None):
        self.user = user
        self.password = password
        self.database_name = database_name
        self.current_user = current_user

    def get_user_entries(self):
        self.user = input("Enter username: ")
        self.password = getpass("Enter password: ")
        self.database_name = input("Enter database name: ")

    def create_database(self):
        self.get_user_entries()
        try:
            with connect(
                host="localhost",
                user=self.user,
                password=self.password,
            ) as connection:
                create_database_query = "CREATE DATABASE users_database"
                with connection.cursor() as cursor:
                    cursor.execute(create_database_query)
        except Error as e:
            print(e)

    def connect_to_database(self, user, password, database_name):
        try:
            with connect(
                host="localhost",
                user=user,
                password=password,
                database=database_name,
            ) as connection:
                print("connected successfuly")
                self.user = user
                self.password = password
                self.database_name = database_name
        except Error as e:
            print(e)

    def create_tables(self):
        try:
            with connect(
                host="localhost",
                user=self.user,
                password=self.password,
                database=self.database_name,
            ) as connection:
                cursor = connection.cursor()
                cursor.execute(
                    "CREATE TABLE users (id INT(10) PRIMARY KEY AUTO_INCREMENT NOT NULL ,username VARCHAR(30) NOT NULL, email VARCHAR(40) NOT NULL, password VARCHAR(30) NOT NULL)")
                connection.commit()
                print("tables created successfuly!")
        except Error as e:
            print(e)

    def register(self, username, email, password):
        try:
            with connect(
                host="localhost",
                user=self.user,
                password=self.password,
                database=self.database_name,
            ) as connection:
                cursor = connection.cursor()
                cursor.execute(
                    "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (username, email, password))
                connection.commit()
                print(f"User {username} registered successfuly!")
        except Error as e:
            print(e)

    def login(self, username, password):
        try:
            with connect(
                host="localhost",
                user=self.user,
                password=self.password,
                database=self.database_name,
            ) as connection:
                cursor = connection.cursor()
                cursor.execute(
                    "SELECT username, email, password FROM users WHERE username = %s AND password = %s", (username, password))
                result = cursor.fetchone()
                if result:
                    print(f"User {username} logged in successfuly!")
                    self.current_user = User(result[0], result[1], result[2])
                    return
                print("Invalid username or password!")
        except Error as e:
            print(e)


# database = Database()
# database.connect_to_database()
# # database.create_tables()
# database.login("mohamed", "123456")
