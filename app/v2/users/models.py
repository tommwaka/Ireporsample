from app.db_config import init_db
import time, datetime




class UsersModel(object):

    def __init__(self):

        self.db = init_db()

    def save(self, firstname, lastname, email, username, password):
        user = {
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "username": username,
            "password": password,
            
        }
        _record = self.user_exists(user['username'])
        if _record:
            return "User already exists"
        else:
            query = """INSERT INTO users (firstname, lastname, email, username, password) VALUES
                        (%(firstname)s, %(lastname)s, %(email)s, %(username)s, %(password)s )"""
            curr = self.db.cursor()
            curr.execute(query, user)
            self.db.commit()
            return user

    def user_exists(self, username):
        curr = self.db.cursor()
        query = "SELECT username, password FROM users WHERE username='{}';".format(username)
        curr.execute(query)
        return curr.fetchone()
