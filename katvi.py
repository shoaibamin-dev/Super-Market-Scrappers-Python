from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome("C:\\Users\\muham\\OneDrive\\Desktop\\imp\\selenium\\chromedriver.exe")


url = "https://katvi.pk/category/fresh-fruits/3"

driver.get(url)


title = "grozar.pk"
name = "Name"
Brand = "brand"

link= "links"
main_price = "Prize"
old_price = "N/A"
discount_percentage = "N/A" 
stock = "Y"

def gomart():
    try: 
        
        main = driver.find_elements_by_class_name("col-12")
        for x in main:
                 
            name = x.find_element_by_class_name("card-title")
            print(name.text)
            
            
            site_element = x.find_element_by_tag_name('a')

            Link = site_element.get_attribute('href')
            print(Link)

            
            
            #  Brand =x.find_element_by_class_name("product-cats")
            #  print(Brand.text)

                
            old_price = x.find_element_by_class_name("price-wrapper")
            print(old_price.text)    
            main_price =x.find_element_by_class_name("mr-2")
            print(main_price.text)
    except:
        pass
    finally:
        driver.quit()
        
gomart()