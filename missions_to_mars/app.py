from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scrape_nasa

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"
mongo = PyMongo(app)

@app.route('/')
def index():
    marsArticle = mongo.db.mars.find_one()
    return render_template('index.html', listings=marsArticle)

@app.route('/scrape')
def scraper():
    articles = mongo.db.mars.find_one()
    data = scrape_nasa.scrape()
    articles.update({}, data, upsert=True)
    return redirect(url_for("index"), code=302)


if __name__ == "__main__":
    app.run(debug=True)