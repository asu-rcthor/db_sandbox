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
# but at the same time we're making a react app in expo
# i prefer python. sorry T_T
# perhaps figure things out eventually
@app.route("/thing")
def query():
    myquery = "" # SQL response
    return f"""<!DOCTYPE HTML>
    <html>
        <head>
            <title>Query for building</title>
        </head>
        <body>
            <h1>Results</h1>
            <p>{myquery}</p>
        </body>
    </html>
    """

port = 1337
app.config['SERVER_NAME'] = f"screwj00.localhost:{port}"
app.run("screwj00.localhost", port)