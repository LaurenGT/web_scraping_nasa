from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time

def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    time.sleep(10)

    mars_info = {}

    # scrape for most recent news story
    news_url = "https://mars.nasa.gov/news/"
    browser.visit(news_url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    mars_info['title'] = soup.find_all("div", class_="content_title")[1].text
    print(soup.find("div", class_="article_teaser_body"))
    mars_info['teaser'] = soup.find("div", class_="article_teaser_body").text    

    # scrape for featured image
    featured_image_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
    browser.visit(featured_image_url)

    visit_image = browser.links.find_by_partial_href("featured").click()
    base_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/"

    html=browser.html
    soup=BeautifulSoup(html,"html.parser")
    image = soup.find('img', class_='fancybox-image')
    src_img = image['src']
    reference_img_url = base_url + src_img
    mars_info['reference_img_url'] = reference_img_url

    # scrape for cerberus hemisphere image
    hem_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hem_url)

    visit_cerb = browser.links.find_by_partial_text("Cerberus").click()
    base_url = "https://astrogeology.usgs.gov/"

    html=browser.html
    soup=BeautifulSoup(html,"html.parser")
    cerb_image = soup.find('img', class_='wide-image')
    src_img = cerb_image['src']
    cerb_url = base_url + src_img
    mars_info['cerb_hem'] = cerb_url

    # scrape for schiaparelli hemisphere image
    hem_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hem_url)

    visit_schi = browser.links.find_by_partial_text("Schiaparelli").click()
    base_url = "https://astrogeology.usgs.gov/"

    html=browser.html
    soup=BeautifulSoup(html,"html.parser")
    schi_image = soup.find('img', class_='wide-image')
    src_img = schi_image['src']
    schi_url = base_url + src_img
    mars_info['schi_hem'] = schi_url

    # scrape for syrtis major hemisphere image
    hem_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hem_url)

    visit_syr = browser.links.find_by_partial_text("Syrtis").click()
    base_url = "https://astrogeology.usgs.gov/"

    html=browser.html
    soup=BeautifulSoup(html,"html.parser")
    syr_image = soup.find('img', class_='wide-image')
    src_img = syr_image['src']
    syr_url = base_url + src_img
    mars_info['syr_hem'] = syr_url

    # scrape for valles marineris hemisphere image
    hem_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hem_url)

    visit_vall = browser.links.find_by_partial_text("Valles").click()
    base_url = "https://astrogeology.usgs.gov/"

    html=browser.html
    soup=BeautifulSoup(html,"html.parser")
    vall_image = soup.find('img', class_='wide-image')
    src_img = vall_image['src']
    vall_url = base_url + src_img
    mars_info['vall_hem'] = vall_url
    
    return mars_info
    browser.quit()