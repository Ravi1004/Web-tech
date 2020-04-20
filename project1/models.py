from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    _tablename_ = "users"
    username = db.Column(db.String, primary_key=True)
    password = db.Column(db.String, nullable=False)
    user_created_on = db.Column(db.DateTime, nullable=False)

    def _init_(self, username, password):
        self.username = username
        self.password = password
        self.user_created_on = datetime.now()
