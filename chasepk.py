#!/usr/bin/env python
# coding: utf-8

# In[2]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome("C:\\Users\\muham\\OneDrive\\Desktop\\imp\\selenium\\chromedriver.exe")

driver.get("https://chase.pk/instantsearchplus/result/?q=surf")



title = "chase.pk"
name = "Name"
Brand = "brand"

link= "links"
main_price = "Prize"
old_price = "N/A"
discount_percentage = "N/A" 
stock = "Y"

def gomart():
    try: 
        
        main = driver.find_elements_by_class_name("isp_grid_product")
        for x in main:
                 
            name = x.find_element_by_class_name("isp_product_title")
            print(name.text)
            
            
            site_element = x.find_element_by_tag_name('a')

            Link = site_element.get_attribute('href')
            print(Link)

            
            
            Brand =x.find_element_by_class_name("isp_search_term_highlight")
            print(Brand.text)

                
                
            main_price =x.find_element_by_class_name("money")
            print(main_price.text)
    except:
        pass
    finally:
        driver.quit()
        
gomart()


# In[ ]:





# In[ ]:




