from selenium import webdriver
from bs4 import BeautifulSoup
from requests import get
import pandas as pd

# PATH = '/home/venturi/Documents/Data_Science_Projects/Used Phones/geckodriver'
# driver = webdriver.Chrome()


# driver.get("https://swappa.com")


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

def grab_info(URL):
    page = get(URL)
    soup = BeautifulSoup(page.content,'lxml')
    price = soup.find('div', attrs={'class':'listing_price listing_price_closed'}).find('span').text
    attributes = soup.find_all('div', attrs={'class':'listing_attr'})
    lst = [attribute.find('span',attrs={'class':'value'}).text for attribute in attributes]
    lst = list(map(lambda x:''.join(char for char in x if char.isalnum()),lst))
    
    print(f'Attributes List: {lst}')
    print(f'Price: ${price}')
    
    
grab_info('https://swappa.com/listing/view/LUJS78801')

# driver.find_element_by_css_selector("[title='Buy and sell iPhones'").click()
# driver.find_element_by_css_selector("[title='Buy used iPhone 11 Pro']").click()
# driver.find_element_by_css_selector("[title*='Unlocked']").click()                                                                                                    
# temp = driver.find_element_by_id(
#     'section_more').find_elements_by_partial_link_text("listing")
# print(temp)
# link = driver.find_element_by_css_selector("a[href*='unlocked']")
# print(link.get_attribute('innerHTML'))
# scrape_iPhone_11()
# driver.quit()

# scrape_iPhone_11_unlocked(driver)