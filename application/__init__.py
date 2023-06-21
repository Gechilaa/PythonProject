from flask import Flask, g
import os
import sqlite3

app = Flask(__name__)

app.secret_key = 'tornike_secret_key'

file_dir = os.path.dirname(__file__)
DATABASE = f'{file_dir}/UsersDatabase.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

from application import database_helpers

with app.app_context():
    connection = get_db()
    database_helpers.create_users_table(connection)

from application import routes