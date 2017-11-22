#!/usr/bin/python3

from flask import Flask, render_template
from plugins.wombat_inventory.inventory import inventory

app = Flask(__name__)
app.register_blueprint(inventory)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=80)