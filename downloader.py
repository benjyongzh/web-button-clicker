from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import argparse
import time
from datetime import datetime
import glob
import os
import shutil


parser = argparse.ArgumentParser(description="Script that clicks a button on a URL")
parser.add_argument("--url", required=True, type=str,help="Enter URL of website with button to click")
parser.add_argument("--buttonclass", required=True, type=str, help="Enter a unique classname of HTML element of button to click")
parser.add_argument("--target", default="downloads", type=str, help="Enter relative file location to download file to")
parser.add_argument("--filename", default="downloadfile", type=str, help="Enter filename to save as")
args = parser.parse_args()

# print("args: ",args.url, args.buttonclass, args.target)

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
prefs = {"profile.default_content_settings.popups": 0,    
        "download.default_directory":args.target, ### Set the path accordingly
        "download.prompt_for_download": False, ## change the downpath accordingly
        "download.directory_upgrade": True}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=options)

#resale prices
#https://beta.data.gov.sg/collections/189/datasets/d_8b84c4ee58e3cfc0ece0d773c8ca6abc/view
#button className = "css-1u67ipt"
#python3 downloader.py --url=https://beta.data.gov.sg/collections/189/datasets/d_8b84c4ee58e3cfc0ece0d773c8ca6abc/view --buttonclass=css-1u67ipt --target=resale-prices --filename=resale-prices

#HDB building polygons
#https://beta.data.gov.sg/collections/2033/datasets/d_16b157c52ed637edd6ba1232e026258d/view
#button className = "css-1u67ipt"
#python3 downloader.py --url=https://beta.data.gov.sg/collections/2033/datasets/d_16b157c52ed637edd6ba1232e026258d/view --buttonclass=css-1u67ipt --target=building-polygons --filename=building-polygons

driver.get(args.url)
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, args.buttonclass)))
driver.find_element(By.CLASS_NAME, args.buttonclass).click()

#! wait until download is done. should not use a fixed amount of time
time.sleep(5)
driver.quit()

# filename formatting
currentDateTime = datetime.now()
datetime_filename_format = "%Y%m%d-%H%M%S"
date_text = currentDateTime.strftime(datetime_filename_format)
filename = date_text + "_" + args.filename

# change file name
files_path = os.path.join(args.target, '*')
list_of_files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True) 
latest_file = list_of_files[0]
oldext = os.path.splitext(latest_file)[1]
# os.rename(latest_file, filename + oldext)
shutil.move(latest_file,os.path.join(args.target,filename + oldext))