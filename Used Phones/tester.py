from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from requests import get
import pandas as pd
from time import sleep

df = pd.DataFrame(columns=['Platform', 'Carrier', 'Color', 'Storage', 'ListDate', 'SaleDate',
                           'Views', 'Quantity', 'Price', 'Condition', 'Description', 'Damage', 'Sold'])


def grab_info(URL, df):
    page = get(URL)
    soup = BeautifulSoup(page.content, 'lxml')
    temp = dict.fromkeys(['Platform', 'Carrier', 'Color', 'Storage', 'ListDate', 'SaleDate',
                          'Views', 'Quantity', 'Price', 'Condition', 'Title', 'Description', 'Damage', 'Sold'])

    for k in temp.keys():
        try:
            temp[k] = soup.find('span', string=k).find_next_sibling(
                'span').text.strip('\n\t')
        except AttributeError:
            temp[k] = None

    temp['Price'] = soup.select(
        'div[class*="listing_price"]')[0].find('span').text
    temp['ListDate'] = soup.find('span', string='Listed').find_next_sibling(
        'span').text.strip('\n\t')
    try:
        temp['ExpiredDate'] = soup.find('span', string='Expires').find_next_sibling(
            'span').text.strip('\n\t')
    except AttributeError:
        temp['ExpiredDate'] = None

    temp['Quantity'] = soup.find(
        'span', string='Quantity Available').find_next_sibling('span').text.strip('\n\t')
    temp['Description'] = soup.find('div', attrs={'class': 'desc_block'}).text
    temp['Condition'] = soup.find('span', attrs={'class': 'speclabel'}).text
    if temp['Condition'] != 'Mint':
        try:
            temp['Damage'] = soup.find(
                'div', attrs={'class': 'desc_block'}).find_next_sibling('div').text
        except AttributeError:
            temp['Damage'] = None
    temp['Title'] = soup.find(
        'div', attrs={'class': 'col-xs-12 col-md-8'}).find_next('h3').text
    if soup.select('div[class*="disabled"]'):
        temp['Sold'] = 'Yes'
    df.loc[URL[-9::]] = temp


def scroll_down():
    """A method for scrolling the page."""
    # Get scroll height.
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to the bottom.
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load the page.
        sleep(2)
        # Calculate new scroll height and compare with last scroll height.
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

driver = webdriver.Chrome()

surls = ("https://swappa.com/mobile/buy/apple-iphone-11/att", "https://swappa.com/mobile/buy/apple-iphone-11/sprint", "https://swappa.com/mobile/buy/apple-iphone-11/t-mobile",
         "https://swappa.com/mobile/buy/apple-iphone-11/unlocked", "https://swappa.com/mobile/buy/apple-iphone-11/verizon", "https://swappa.com/mobile/buy/apple-iphone-11-pro/att",
         "https://swappa.com/mobile/buy/apple-iphone-11-pro/sprint", "https://swappa.com/mobile/buy/apple-iphone-11-pro/t-mobile",
         "https://swappa.com/mobile/buy/apple-iphone-11-pro/unlocked", "https://swappa.com/mobile/buy/apple-iphone-11-pro/verizon", 
         "https://swappa.com/mobile/buy/apple-iphone-11-pro-max/att", "https://swappa.com/mobile/buy/apple-iphone-11-pro-max/sprint", 
         "https://swappa.com/mobile/buy/apple-iphone-11-pro-max/t-mobile", "https://swappa.com/mobile/buy/apple-iphone-11-pro-max/unlocked", 
         "https://swappa.com/mobile/buy/apple-iphone-11-pro-max/verizon", "https://swappa.com/mobile/buy/apple-iphone-xr/att","https://swappa.com/mobile/buy/apple-iphone-xr/sprint",
         "https://swappa.com/mobile/buy/apple-iphone-xr/t-mobile","https://swappa.com/mobile/buy/apple-iphone-xr/unlocked","https://swappa.com/mobile/buy/apple-iphone-xr/verizon")


for urls in surls: 
    driver.get(urls)
    scroll_down()
    listings = driver.find_elements_by_css_selector("a[href*='listing'")
    listingstext = [listing.get_attribute("href") for listing in listings]
    for links in listingstext:
        grab_info(links, df)
        sleep(3)

# print(df)
# def scrape_iPhone_11():
# driver.find_element_by_css_selector("[title='Cheap iPhone 11'").click()
# unlocked iPhones
# driver.find_element_by_css_selector("[title='Cheap iPhone 11']").click()
# driver.find_element_by_css_selector("[title*='unlocked']").click()
# temp = driver.find_element_by_id(
#     'section_more').find_elements_by_partial_link_text("listing")
# print(temp)
# driver.find_element_by_css_selector("[title*='AT&T']").click()
# driver.find_element_by_css_selector("[title*='Sprint']").click()
# driver.find_element_by_css_selector("[title*='T-Mobile']").click()
# driver.find_element_by_css_selector("[title*='Verizon']").click()

# def scrape_iPhone_11_unlocked(driver):
#     driver.get("https://swappa.com/mobile/buy/apple-iphone-11/unlocked")
#     temp = driver.find_element_by_id('section_more').find_elements_by_class_name("listing_row")
#     for link in temp:
#         link.click()
#         URL = driver.current_url
#         grab_info(URL)
#     print(temp)

# grab_info('https://swappa.com/listing/view/LUJS78801', df)
# print(df)

# driver.find_element_by_css_selector("[title='Buy and sell iPhones'").click()
# driver.find_element_by_css_selector("[title='Buy used iPhone 11 Pro']").click()
# driver.find_element_by_css_selector("a[href*='unlocked']").click()
# temp = driver.find_element_by_id(
#     'section_more').find_elements_by_partial_link_text("listing")
# print(temp)
# link = driver.find_element_by_css_selector("a[href*='unlocked']")
# print(link.get_attribute('innerHTML'))
# scrape_iPhone_11()
# driver.quit()

# scrape_iPhone_11_unlocked(driver)
df.to_csv('Data_Science_Projects/Used Phones/storage.csv')
