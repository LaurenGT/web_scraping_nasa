from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scrape_nasa

app = Flask(__name__)



if __name__ == "__main__":
    app.run(debug=True)