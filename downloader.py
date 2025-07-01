#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import argparse
import glob
import os
import shutil
import time
from utils import get_current_file_count,wait_for_download,format_filename,add_id_rows,get_latest_file

# set args
parser = argparse.ArgumentParser(description="Script that clicks a button on a URL to download a file")
parser.add_argument("--url", required=True, type=str,help="Enter URL of website with button to click")
parser.add_argument("--buttonselector", required=True, type=str, help="Enter CSS selector of HTML element of button to click")
parser.add_argument("--target", default="Downloads/", type=str, help="Enter relative file location to download file to")
parser.add_argument("--filename", default="downloadfile", type=str, help="Enter filename to save as")
parser.add_argument("--idcolumn", default=False, type=bool, help="Boolean if you want to add an ID column to the .csv file downloaded")
parser.add_argument("--timeout", default=20, type=int, help="Enter timeout for downloading file")
args = parser.parse_args()

# ensure target folder exists
target_abs = os.path.abspath(args.target)
os.makedirs(target_abs, exist_ok=True)

#webdriver options
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--disable-notifications")
# options.add_argument("--disable-dev-shm-usage")
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
prefs = {
        "download":{
                "default_directory":target_abs, ### Set the path accordingly
                "directory_upgrade": True,
                "prompt_for_download": False, ## change the downpath accordingly
                "extensions_to_open": ""
                },
        "savefile.default_directory": target_abs,
        "safebrowsing.enabled": True,
        "profile.default_content_settings.popups": 0
        }
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=options)

# start download
driver.get(args.url)
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, args.buttonselector))).click()

# wait until download is done
file_count = get_current_file_count(target_abs)
wait_for_download(args.timeout, target_abs, file_count)
driver.quit()
print("file downloaded to: ", target_abs)

# print(get_latest_file(args.target))

# filename formatting
filename = format_filename(args.filename)

# change filename
files_path = os.path.join(target_abs, '*')
# print(files_path)
list_of_files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)
print("number of files:", len(list_of_files))
if not list_of_files:
        raise FileNotFoundError(f"No downloaded files found in: {target_abs}")
latest_file = list_of_files[0]
oldext = os.path.splitext(latest_file)[1]
shutil.move(latest_file,os.path.join(target_abs,filename + oldext))

if args.idcolumn:
        # add id columns
        add_id_rows(target_abs + "/" + filename, "_with-id")