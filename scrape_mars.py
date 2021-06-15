from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape_info():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    
    # Scrape article 
    
    # Set URL
    url = "https://redplanetscience.com/"
    browser.visit(url)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the title and paragraph of the recent article
    news_title = soup.find('div', class_='content_title')
    news_text = soup.find('div', class_='article_teaser_body')    
    
    # Scrape image

    # Set URL
    url = "https://spaceimages-mars.com/"
    browser.visit(url)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the featured image 
    relative_image_path = soup.find('a', class_="showimg").get('href')
    mars_image = url + relative_image_path

    # Scrape facts

    # Set URL
    url = 'https://galaxyfacts-mars.com/'

    # Scrape table
    tables = pd.read_html(url)
    tables
    
    # convert table to dataframe
    df = tables[0]
    
    # convert dataframe to HTML table
    html_table = df.to_html()
    
     # Store data in a dictionary
    mars_data = {
        "news_title": news_title,
        "news_text": news_text,
        "mars_image": mars_image,
        "facts_table": html_table,
        "hemispheres": {1:{"title": "Valles Marineris Hemisphere", "img_url": "https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg"}, 
                        2:{"title": "Cerberus Hemisphere", "img_url": "https://marshemispheres.com/images/full.jpg"},
                        3:{"title": "Schiaparelli Hemisphere", "img_url": "https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg"},
                        4:{"title": "Syrtis Major Hemisphere", "img_url": "https://marshemispheres.com/images/syrtis_major_enhanced-full.jpg"}}

    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data

