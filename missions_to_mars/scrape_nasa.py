from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_article():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    time.sleep(10)

    articles = {}

    news_url = "https://mars.nasa.gov/news/"
    browser.visit(news_url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    articles['title'] = soup.find_all("div", class_="content_title")[1].text
    articles['teaser'] = soup.find("div", class_="article_teaser_body").text    

    return articles
    browser.quit

def scrape_image():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    time.sleep(10)

    img_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
    browser.visit(img_url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    browser.links.find_by_partial_text("FULL IMAGE").click()


    featured_img = soup.find('img', class_="fancybox-image").get("src")

    return featured_img
