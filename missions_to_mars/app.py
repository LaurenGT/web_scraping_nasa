from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scrape_nasa

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"
mongo = PyMongo(app)

@app.route('/')
def index():
    articles = mongo.db.articles.find_one()
    return render_template('index.html', articles=articles)

@app.route('/scrape')
def scraper():
    articles = mongo.db.articles
    data = scrape_nasa.scrape_article()
    articles.update({}, data, upsert=True)
    return redirect(('/'), code=302)


if __name__ == "__main__":
    app.run(debug=True)