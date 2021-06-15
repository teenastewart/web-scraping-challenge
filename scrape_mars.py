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
    news_title = soup.find('div', class_='content_title').text
    news_text = soup.find('div', class_='article_teaser_body').text    
    
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
    # Grab the first row
    new_header = df.iloc[0]
    # Re-define dataframe as table minus first row
    df = df[1:] 
    # reset the header to the first row
    df.columns = new_header 
    # Reset index
    df = df.reset_index(drop=True)
    # convert dataframe to HTML table
    html_table = df.to_html()
    
     # Store data in a dictionary
    mars_data = {
        "news_title": news_title,
        "news_text": news_text,
        "mars_image": mars_image,
        "facts_table": html_table,
        "hemispheres": {"Valles":{"title": "Valles Marineris Hemisphere", "img_url": "https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg"}, 
                        "Cerberus":{"title": "Cerberus Hemisphere", "img_url": "https://marshemispheres.com/images/full.jpg"},
                        "Schiaparelli":{"title": "Schiaparelli Hemisphere", "img_url": "https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg"},
                        "Syrtis":{"title": "Syrtis Major Hemisphere", "img_url": "https://marshemispheres.com/images/syrtis_major_enhanced-full.jpg"}}

    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data

