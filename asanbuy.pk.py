#!/usr/bin/env python
# coding: utf-8

# In[6]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome("C:\\Users\\muham\\OneDrive\\Desktop\\imp\\selenium\\chromedriver.exe")
url = "https://asanbuy.pk/?s=bonus&post_type=product"

driver.get(url)
title = "Asanbuy.pk"
name = "Name"
Brand = "brand"

link= "links"
main_price = "Prize"
old_price = "old price"
discount_percentage = "N/A" 
stock = "Y"

def gomart():
    try: 
        
        main = driver.find_elements_by_class_name("product-content")
        for x in main:
                 
            name = x.find_element_by_tag_name("h3")
            print(name.text)
            
            
            site_element = x.find_element_by_tag_name('a')

            Link = site_element.get_attribute('href')
            print(Link)

            
            
#             Brand =x.find_element_by_class_name("meta-brand")
#             print(Brand.text)

#             old_price = x.find_element_by_class_name("woocommerce-Price-currencySymbol")
#             print(old_price.text)    
                
            main_price =x.find_element_by_class_name("price")
            print(main_price.text)
            
            
    except:
        pass
    finally:
        driver.quit()
        
gomart()


# In[ ]:




