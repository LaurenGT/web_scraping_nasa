from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape_article():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    time.sleep(10)

    mars_info = {}

    news_url = "https://mars.nasa.gov/news/"
    browser.visit(news_url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    mars_info['title'] = soup.find_all("div", class_="content_title")[1].text
    mars_info['teaser'] = soup.find("div", class_="article_teaser_body").text    

    # return articles

    # mars_facts_url = "https://space-facts.com/mars/"
    # browser.visit(mars_facts_url)

    browser.quit

    featured_image_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
    browser.visit(featured_image_url)

    visit_image = browser.links.find_by_partial_href("featured").click()
    base_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/"

    html=browser.html
    soup=BeautifulSoup(html,"html.parser")
    image = soup.find('img', class_='fancybox-image')
    src_img = image['src']
    reference_img_url = base_url + src_img

    return reference_img_url

    browser.quit