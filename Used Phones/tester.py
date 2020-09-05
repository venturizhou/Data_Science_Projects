from selenium import webdriver

PATH = "C:/Users/venturi/Work/Data_Science_Projects/Used Phones/msedgedriver.exe"
driver = webdriver.Edge(PATH)

driver.get("https://swappa.com")

def scrape_iPhone_11():
    # driver.find_element_by_css_selector("[title='Cheap iPhone 11'").click()
    ##unlocked iPhones
    driver.find_element_by_css_selector("[title='Cheap iPhone 11']").click()
    driver.find_element_by_css_selector("[title*='unlocked']").click()
    temp = driver.find_element_by_id('section_more').find_elements_by_partial_link_text("listing")
    print(temp)
    # driver.find_element_by_css_selector("[title*='AT&T']").click()
    # driver.find_element_by_css_selector("[title*='Sprint']").click()
    # driver.find_element_by_css_selector("[title*='T-Mobile']").click()
    # driver.find_element_by_css_selector("[title*='Verizon']").click()

driver.find_element_by_css_selector("[title=iPhones").click()
driver.find_element_by_css_selector("[title='Cheap iPhone 11']").click()
# driver.find_element_by_css_selector("[title*='Unlocked']").click()
link = driver.find_element_by_css_selector("a[href*='unlocked']")
print(link.get_attribute('innerHTML'))
# scrape_iPhone_11()
# driver.quit()

