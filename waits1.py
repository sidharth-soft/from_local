from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by  import By
from selenium.webdriver.support import expected_conditions as EC


path="C:\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.get("http://www.theTestingWorld.com/testings")
#implict wait
#it is applicable to all the find elements

# driver.implicitly_wait(20)
# time.sleep(20)
#
# s=driver.find_element_by_id('countryId')
# s1=driver.find_element_by_id('stateID')
# s2=driver.find_element_by_id('countryId')


#excplicit wait

wait = WebDriverWait(driver,30)
wait.until(EC.text_to_be_present_in_element((By.ID,'countryId'),"India"))
obj = Select(driver.find_element_by_id("countryId"))
obj.select_by_visible_text("India")


driver.save_screenshot("C:/Users/jejayakr/Desktop/frame1handling.jpg")


exit(0)
driver.get_screenshot_as_file("C:/Users/jejayakr/Desktop/screenshot1.png")
