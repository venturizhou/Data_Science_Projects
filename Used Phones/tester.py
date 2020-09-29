from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from requests import get
import pandas as pd
from time import sleep

# only used if not reading in front existing dataframe
# df = pd.DataFrame(columns=['Model', 'Platform', 'Carrier', 'Color', 'Storage', 'ListDate', 'ExpiredDate', 'SaleDate',
#                            'Views', 'Quantity', 'Price', 'Condition', 'Description', 'Damage', 'Sold'])

# surface
# df = pd.read_csv(r'C:\Users\ventu\WSL\Python\Data_Science_Projects\Used Phones\storage.csv')
# df = df.set_index('Listing')

# linux
df = pd.read_csv('/home/venturi/Projects/Data_Science_Projects/Used Phones/storage.csv')
df = df.set_index('Listing')

def grab_info(URL, df):
    page = get(URL)
    soup = BeautifulSoup(page.content, 'lxml')
    temp = dict.fromkeys(['Model', 'Platform', 'Carrier', 'Color', 'Storage', 'ListDate', 'ExpiredDate', 'SaleDate',
                          'Views', 'Quantity', 'Price', 'Condition', 'Title', 'Description', 'Damage', 'Sold'])
    for k in temp.keys():
        try:
            temp[k] = soup.find('span', string=k).find_next_sibling(
                'span').text.strip('\n\t')
        except AttributeError:
            temp[k] = None
    temp['Price'] = soup.select(
        'div[class*="listing_price"]')[0].find_next('span').text
    temp['ListDate'] = soup.find('span', string='Listed').find_next_sibling(
        'span').text.strip('\n\t')
    try:
        temp['ExpiredDate'] = soup.find('span', string='Expires').find_next_sibling(
            'span').text.strip('\n\t')
    except AttributeError:
        temp['ExpiredDate'] = None
    temp['Quantity'] = soup.find(
        'span', string='Quantity Available').find_next_sibling('span').text.strip('\n\t')
    temp['Description'] = soup.find('div', attrs={'class': 'desc_block'}).text.strip('\n\t')
    temp['Condition'] = soup.find('span', attrs={'class': 'speclabel'}).text
    if temp['Condition'] != 'Mint':
        try:
            temp['Damage'] = soup.find(
                'div', attrs={'class': 'desc_block'}).find_next_sibling('div').text.strip('\n\t')
        except AttributeError:
            temp['Damage'] = None
    temp['Title'] = soup.find(
        'div', attrs={'class': 'col-xs-12 col-md-8'}).find_next('h3').text
    temp['Model'] = soup.find('ul', attrs={'class': 'breadcrumb'}).find_next(
        "li").find_next("li").find_next("li").text.strip('\n\t')
    if soup.select('div[class*="listing_price_closed"]'):
        temp['Sold'] = 'Yes'
        temp['SaleDate'] = soup.find('span', string='Closed').find_next_sibling(
            'span').text.strip('\n\t')    
    df.loc[URL[-9::]] = temp

def Egrab_info(url, df):
    page = get(url)
    soup = BeautifulSoup(page.content, 'lxml')
    temp = dict.fromkeys(['Model', 'Platform', 'Carrier', 'Color', 'Storage', 'ListDate', 'ExpiredDate', 'SaleDate',
                          'Views', 'Quantity', 'Price', 'Condition', 'Title', 'Description', 'Damage', 'Sold'])

    listingnumber = soup.find(id='descItemNumber').text
    temp['Model'] = soup.find('td', string='Model').find_next_sibling('td').text
    temp['Platform'] = soup.find('td', attrs={'class':''})
    temp['Carrier'] 
    temp['Color']

    df.loc[listingnumber] == temp

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

# comment out if on surface
# driver = webdriver.Edge(r'edgedriver_arm64\msedgedriver.exe')

# comment out if on linux desktop
driver = webdriver.Chrome()
carriers = ['/att', '/sprint', '/unlocked', '/verizon', '/t-mobile']
surls = ["https://swappa.com/buy/apple-iphone-11", "https://swappa.com/buy/apple-iphone-11-pro", "https://swappa.com/buy/apple-iphone-11-pro-max",
         "https://swappa.com/buy/apple-iphone-xr", "https://swappa.com/buy/apple-iphone-xs", "https://swappa.com/buy/apple-iphone-xs-max", "https://swappa.com/buy/apple-iphone-x",
         "https://swappa.com/buy/apple-iphone-se-2nd-gen", "https://swappa.com/buy/samsung-galaxy-note-10-plus", "https://swappa.com/buy/samsung-galaxy-s10-plus",
         "https://swappa.com/buy/samsung-galaxy-s10", "https://swappa.com/buy/samsung-galaxy-s20-plus", "https://swappa.com/buy/samsung-galaxy-s20-ultra",
         "https://swappa.com/buy/samsung-galaxy-note-20-ultra-5g", "https://swappa.com/buy/google-pixel-4-xl", "https://swappa.com/buy/google-pixel-4",
         "https://swappa.com/buy/oneplus-8-pro", "https://swappa.com/buy/oneplus-8", "https://swappa.com/buy/oneplus-7-pro", "https://swappa.com/buy/oneplus-7t"]

#all items
for carrier in carriers:
    for urls in map(lambda x: x+carrier, surls):
        driver.get(urls)
        scroll_down()
        listings = driver.find_elements_by_css_selector("a[href*='listing'")
        listingstext = [listing.get_attribute("href") for listing in listings]
        for links in listingstext:
            grab_info(links, df)
            sleep(3)

#only sold items
# for carrier in carriers:
#     for urls in map(lambda x: x+carrier, surls):
#         driver.get(urls)
#         scroll_down()
#         listings = driver.find_elements_by_css_selector("a[href*='listing'")
#         listingstext = [listing.get_attribute("href") for listing in listings]
#         for links in listingstext[-5::]:
#             grab_info(links, df)
#             sleep(3)

# surface
# df.to_csv(r'C:\Users\ventu\WSL\Python\Data_Science_Projects\Used Phones\storage.csv')
# linux desktop
df.to_csv('Data_Science_Projects/Used Phones/storage.csv')
