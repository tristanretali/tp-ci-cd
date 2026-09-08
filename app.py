from flask import Flask
import mysql.connector
import os

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/db")
def check_db():
    conn = mysql.connector.connect(
        host=os.environ.get("DB_HOST", "mysql-test"),
        user="root",
        password=os.environ.get("DB_PASSWORD", "root"),
    )
    conn.close()
    return "<p>Connexion à la base de données réussie !</p>"


if __name__ == "__main__":
    app.run("0.0.0.0", port=4000)
