from flask import Flask


def second_import():
    from app import routes


app = Flask(__name__)
second_import()
