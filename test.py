
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
					 
					 
driver = webdriver.Remote(
   command_executor="http://127.0.0.1:4444/wd/hub",
   desired_capabilities={
            "browserName": "chrome",
        })

driver1 = webdriver.Remote(
   command_executor="http://127.0.0.1:4444/wd/hub",
   desired_capabilities={
            "browserName": "chrome",
        })

driver2 = webdriver.Remote(
   command_executor="http://127.0.0.1:4444/wd/hub",
   desired_capabilities={
            "browserName": "chrome",
        })

  
try:
    driver.implicitly_wait(30)
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.send_keys("documentation")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    print('this is running on a grid0')
    
    driver1.implicitly_wait(30)
    driver1.get("http://www.python.org")
    assert "Python" in driver1.title
    elem1 = driver1.find_element_by_name("q")
    elem1.send_keys("documentation")
    elem1.send_keys(Keys.RETURN)
    assert "No results found." not in driver1.page_source
    print('this is running on a grid1')
    
    driver2.implicitly_wait(30)
    driver2.get("http://www.python.org")
    assert "Python" in driver2.title
    elem2 = driver.find_element_by_name("q")
    elem2.send_keys("documentation")
    elem2.send_keys(Keys.RETURN)
    assert "No results found." not in driver2.page_source
    print('this is running on a grid2')
    
finally:
    driver.quit()
    driver1.quit()
    driver2.quit()