

from selenium import webdriver
import selenium.webdriver.common.keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome("C:\\Program Files\\chromedriver.exe")

title = "ahsmart.pk"
name = "Name"
Brand = "brand"

link = "links"
main_price = "Prize"
old_price = "N/A"
discount_percentage = "N/A"
stock = "Y"


def gomart():
    try:

        main = driver.find_elements_by_class_name("product-inner")
        for x in main:

            name = x.find_element_by_tag_name("h2")
            print(name.text)

            site_element = x.find_element_by_tag_name('a')

            Link = site_element.get_attribute('href')
            print(Link)

            Brand = x.find_element_by_class_name("meta-brand")
            print(Brand.text)

            main_price = x.find_element_by_class_name("price")
            print(main_price.text)


#         next_btn = WebDriverWait(driver, 20).until(
#             EC.presence_of_element_located((By.LINK_TEXT, "Next")))


#          driver.get(next_btn.get_attribute('href'))

#         gomart()
    except Exception as e:
        print(e)

    finally:
        driver.quit()


gomart()


# In[ ]:
