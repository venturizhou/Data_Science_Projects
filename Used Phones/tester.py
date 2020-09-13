from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from requests import get
import pandas as pd
from time import sleep

df = pd.DataFrame(columns=['OS', 'Carrier', 'Color', 'Storage', 'ListDate', 'SaleDate',
                           'Views', 'Quanity', 'Price', 'Condition', 'Description', 'Damage', 'Sold'])

def grab_info(URL, df):
    page = get(URL)
    soup = BeautifulSoup(page.content, 'lxml')

    price = soup.select('div[class*="listing_price"]')[0].find('span').text
    attributes = soup.find_all('div', attrs={'class': 'listing_attr'})
    condition = soup.find('span', attrs={'class': 'speclabel'}).text
    description = soup.find_all('div', attrs={'class': 'desc_block'})[
        0].text.strip('\n')
    try:
        damage = soup.find_all('div', attrs={'class': 'desc_block'})[
        1].text.strip('\n')
    except IndexError:
        damage = "NaN"
   
    lst = [attribute.find(
        'span', attrs={'class': 'value'}).text for attribute in attributes]
    lst = list(map(lambda x: ''.join(char for char in x if char.isalnum()), lst))
    lst.append(price)
    lst.append(condition)
    lst.append(description)
    lst.append(damage)
    if soup.select('div[class*="disabled"]'):
        lst.append('Yes')
    else:
        lst.append('No')
    df.loc[URL[-9::]] = lst

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

grab_info('https://swappa.com/listing/view/LUBQ33062', df)
print(df)

# driver = webdriver.Chrome()
# driver.get("https://swappa.com/mobile/buy/apple-iphone-11/unlocked")
# scroll_down()

# listings = driver.find_elements_by_css_selector("a[href*='listing'")
# listingstext = [listing.get_attribute("href") for listing in listings]
# print(dict(enumerate(listingstext)))

# for links in listingstext:
#     driver.get(links)
#     sleep(5)
#     grab_info(links,df)
#     sleep(3)
# links.send_keys(Keys.CONTROL + 't')
# current = driver.current_url
# print(current)
# sleep(5)
# grab_info(current, df)
# driver.quit()
# sleep(5)

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
