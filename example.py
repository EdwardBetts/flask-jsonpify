"""
Flask-Jsonpify example
===================
This is a tiny Flask Application demonstrating Flask-Jsonpify, an extension to
Flask's jsonify function, returning JSON-Padded responses when a callback is
specified as request's arguments.

:copyright: (C) 2013 by Cory Dolphin.
:license:   MIT/X11, see LICENSE for more details.
"""
from flask import Flask

try:
    import flask_jsonpify.jsonify
except:
    from flask.ext.jsonpify import jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify(foo='bar')

@app.route("/user/<user_id>")
def show_user(user_id):
    return jsonify(user={"name":"johnny droptables", "id":user_id})

@app.route("/users")
def list_users():
    return jsonify([{"name":"johnny droptables-%i"%i, "id":i} for i in range(10)])

if __name__ == "__main__":
    app.run(debug=True)
