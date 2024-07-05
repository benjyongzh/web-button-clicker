from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
prefs = {"profile.default_content_settings.popups": 0,    
        "download.default_directory":"Desktop", ### Set the path accordingly
        "download.prompt_for_download": False, ## change the downpath accordingly
        "download.directory_upgrade": True}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=options)

#resale prices
#https://beta.data.gov.sg/collections/189/datasets/d_8b84c4ee58e3cfc0ece0d773c8ca6abc/view
#button className = "css-1u67ipt"

#HDB building polygons
#https://beta.data.gov.sg/collections/2033/datasets/d_16b157c52ed637edd6ba1232e026258d/view
#button className = "css-1u67ipt"
driver.get("https://beta.data.gov.sg/collections/189/datasets/d_8b84c4ee58e3cfc0ece0d773c8ca6abc/view")

WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "css-1u67ipt")))

driver.get_element(By.CLASS_NAME, "css-1u67ipt").click()

time.sleep(5)

driver.quit()