import os
import json
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from percy import percy_screenshot

USER_NAME = os.environ.get("BROWSERSTACK_USERNAME", "BROWSERSTACK_USERNAME")
ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY", "BROWSERSTACK_ACCESS_KEY")

def test_session(capability):
    # create an automate session by creating a remote webdriver
    driver = webdriver.Remote("https://hub-cloud.browserstack.com/wd/hub", capability)
    try:
      # [percy note: important step] 
      # set the desired window size on which we want the screenshot
      width, height = 1280, 1024
      driver.set_window_size(width, height)

      # navigate to required website
      driver.get('https://bstackdemo.com/')
      WebDriverWait(driver, 10).until(EC.title_contains('StackDemo'))

      # click on the apple products
      WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
         (By.XPATH, '//*[@id="__next"]/div/div/main/div[1]/div[2]/label/span'))).click()

      # [percy note: important step]
      # Percy Screenshot 1
      # take percy_screenshot using the following command
      percy_screenshot(driver, name = 'screenshot_1')

      # Get text of current product
      item_on_page = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="10"]/p'))).text
      
      # clicking on 'Add to cart' button
      WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="10"]/div[4]'))).click()
      
      # Check if the Cart pane is visible
      WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(
          (By.CSS_SELECTOR, '.float-cart__content')))

      # Get text of product in cart
      item_in_cart = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
          (By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div[2]/div/div[3]/p[1]'))).text
      
      # [percy note: important step]
      # Percy Screenshot 2
      # take percy_screenshot using the following command
      percy_screenshot(driver, name = 'screenshot_2')

      if item_on_page == item_in_cart:
          # Set the status of test as 'passed' if item is added to cart
          driver.execute_script(
              'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "iPhone 12 has been successfully added to the cart!"}}')
      else:
          # Set the status of test as 'failed' if item is not added to cart
          driver.execute_script(
              'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "iPhone 12 not added to the cart!"}}')
    except Exception as e:
       message = f'Error occured while executing script : {str(e.__class__)} {str(e.__msg__)}'
       print(message)
       driver.execute_script(
          'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": ' + json.dumps(message) + '}}')
    finally:
       # Stop the driver
       driver.quit()

if __name__ == "__main__":
   chrome_on_windows_11 = {
    'bstack:options' : {
      "deviceName": "Samsung Galaxy S22 Ultra",
      "osVersion" : "12",
      "browserVersion" : "latest",
      "projectName" : "My Project",
      "buildName" : "test percy_screenshot",
      "sessionName" : "BStack first_test",
      "local" : "false",
      "userName": USER_NAME,
      "accessKey": ACCESS_KEY,
    },
    "browserName" : "Chrome",
  }
   
   capabilities_list = [chrome_on_windows_11]
   print(list(map(test_session, capabilities_list)))
