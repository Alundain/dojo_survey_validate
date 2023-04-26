from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Survey:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.comment = data['comment']