from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app


class VIP:
    def __init__(self, data):
        self.id = data["id"]
        self.your_name = data["your_name"]
        self.your_dogs_name = data["your_dogs_name"]
        self.gender = data["gender"]
        self.email = data["email"]

    @classmethod
    def get_all(cls, data):
        query = "SELECT * FROM users;"
        results = connectToMySQL("dogs").query_db(query, data)

        users = []
        for row in results:
            users.append(VIP(row))

        return users
