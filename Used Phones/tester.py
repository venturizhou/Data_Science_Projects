from selenium import webdriver
import pandas as pd

# PATH = '/home/venturi/Documents/Data_Science_Projects/Used Phones/geckodriver'
driver = webdriver.Chrome()

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

def scrape_iPhone_11_unlocked(driver):
    driver.get("https://swappa.com/mobile/buy/apple-iphone-11/unlocked")
    temp = driver.find_element_by_id('section_more').find_elements_by_class_name("listing_row")
    for link in temp:
        link.click()
        
    print(temp)



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

scrape_iPhone_11_unlocked(driver)