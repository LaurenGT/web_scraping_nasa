from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    time.sleep(10)

    mars_info = {}

    # scrape for most recent news story
    news_url = "https://mars.nasa.gov/news/"
    browser.visit(news_url)

    time.sleep(5)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    mars_info['title'] = soup.find_all("div", class_="content_title")[1].text
    print(soup.find("div", class_="article_teaser_body"))
    mars_info['teaser'] = soup.find("div", class_="article_teaser_body").text    

    # scrape for featured image
    featured_image_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
    browser.visit(featured_image_url)

    time.sleep(5)

    visit_image = browser.links.find_by_partial_href("featured").click()
    base_img_url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/"

    html_img=browser.html
    soup=BeautifulSoup(html_img,"html.parser")
    image = soup.find('img', class_='fancybox-image')
    src_img = image['src']
    reference_img_url = base_img_url + src_img
    mars_info['reference_img_url'] = reference_img_url

    # scrape for cerberus hemisphere image
    hem_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hem_url)

    time.sleep(5)

    visit_cerb = browser.links.find_by_partial_text("Cerberus").click()
    base_hem_url = "https://astrogeology.usgs.gov/"

    html_cerb=browser.html
    soup=BeautifulSoup(html_cerb,"html.parser")
    cerb_image = soup.find('img', class_='wide-image')
    src_img = cerb_image['src']
    cerb_url = base_hem_url + src_img
    mars_info['cerb_hem'] = cerb_url

    # scrape for schiaparelli hemisphere image
    hem_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hem_url)

    time.sleep(5)

    visit_schi = browser.links.find_by_partial_text("Schiaparelli").click()
    base_hem_url = "https://astrogeology.usgs.gov/"

    html_schi=browser.html
    soup=BeautifulSoup(html_schi,"html.parser")
    schi_image = soup.find('img', class_='wide-image')
    src_img = schi_image['src']
    schi_url = base_hem_url + src_img
    mars_info['schi_hem'] = schi_url

    # scrape for syrtis major hemisphere image
    hem_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hem_url)

    time.sleep(5)

    visit_syr = browser.links.find_by_partial_text("Syrtis").click()
    base_hem_url = "https://astrogeology.usgs.gov/"

    html_syr=browser.html
    soup=BeautifulSoup(html_syr,"html.parser")
    syr_image = soup.find('img', class_='wide-image')
    src_img = syr_image['src']
    syr_url = base_hem_url + src_img
    mars_info['syr_hem'] = syr_url

    # scrape for valles marineris hemisphere image
    hem_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hem_url)

    time.sleep(5)

    visit_vall = browser.links.find_by_partial_text("Valles").click()
    base_hem_url = "https://astrogeology.usgs.gov/"

    html_vall=browser.html
    soup=BeautifulSoup(html_vall,"html.parser")
    vall_image = soup.find('img', class_='wide-image')
    src_img = vall_image['src']
    vall_url = base_hem_url + src_img
    mars_info['vall_hem'] = vall_url

    # scrape info table
    facts_url = "https://space-facts.com/mars/"
    browser.visit(facts_url)

    time.sleep(5)

    html_table=browser.html
    soup=BeautifulSoup(html_table,"html.parser")

    facts_table = soup.find_all('table', class_="tablepress tablepress-id-p-mars")[0]('tr')

    # ultimate_facts = dict()
    key=[]
    value=[]
    for tr in facts_table:
        col_one = tr.find('td', class_="column-1").text
        col_two = tr.find('td', class_="column-2").text
        # ultimate_facts[col_one] = col_two
        key.append(col_one)
        value.append(col_two)

    # ultimate_df = pd.DataFrame(ultimate_facts)
    # ultimate_df.columns=['Description','Mars']
    # ultimate_df.set_index('Description', inplace=False)
    mars_info["data_zip"] = dict(zip(key,value))
    # mars_info["data_zip"] = ultimate_df.to_html(classes="table table-striped")
    # print(mars_info["data_zip"])

    browser.quit()

    return mars_info
    