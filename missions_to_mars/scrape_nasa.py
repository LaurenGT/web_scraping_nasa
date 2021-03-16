from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    time.sleep(10)

    articles = {}

    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    articles['title'] = soup.find("div", class_="content_title").text
    articles['teaser'] = soup.find("div", class_="article_teaser_body").text
    # article_image = soup.find_one("div", class_="list_image")

    # print(article_title)

    browser.quit

    return articles
