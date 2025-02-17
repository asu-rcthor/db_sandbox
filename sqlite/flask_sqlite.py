#!/usr/bin/env python3
# This prototype was borrowed from pwn.college's Talking Web and Web Security modules.

import flask
import sqlite3
import tempfile

app = flask.Flask(__name__)

class TemporaryDB:
    def __init__(self):
        self.db_file = tempfile.NamedTemporaryFile("x", suffix=".db")

    def execute(self, sql, parameters=()):
        connection = sqlite3.connect(self.db_file.name)
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        result = cursor.execute(sql, parameters)
        connection.commit()
        return result

db = TemporaryDB()
db.execute("""CREATE TABLE tblname AS SELECT "THING" AS content""")

@app.route("/")
def landing():
    out = ""
    with open("query.html", "r") as f:
        out = f.read()
    return out

# you might need node or php to make htmls work fine?
# i prefer python. sorry T_T
@app.route("/thing")
def query():
    return f"""<!DOCTYPE HTML>
    <html>
        <head>
            <title>Query for building</title>
        </head>
        <body>
        </body>
    </html>
    """

port = 1337
app.config['SERVER_NAME'] = f"screwj00.localhost:{port}"
app.run("screwj00.localhost", port)