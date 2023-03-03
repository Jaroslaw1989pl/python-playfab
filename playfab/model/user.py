# build-in modules
from datetime import datetime
# custom modules
from .db import PostgreSQL


class User(PostgreSQL):

    def __init__(self, email, password):
        super().__init__()

        self.email = email
        self.password = password

    def add(self):
        query = "INSERT INTO users (email, email_update, pass, pass_update) VALUES (%s, %s, %s, %s)"
        values = (self.email, datetime.now(), self.password, datetime.now())
        super().insert(query, values)