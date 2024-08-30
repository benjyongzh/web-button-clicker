#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import argparse
import glob
import os
import shutil
from utils import get_current_file_count,wait_for_download,format_filename,add_id_rows,get_latest_file

# set args
parser = argparse.ArgumentParser(description="Script that clicks a button on a URL to download a file")
parser.add_argument("--url", required=True, type=str,help="Enter URL of website with button to click")
parser.add_argument("--buttonxpath", required=True, type=str, help="Enter XPath of HTML element of button to click")
parser.add_argument("--target", default="Downloads/", type=str, help="Enter relative file location to download file to")
parser.add_argument("--filename", default="downloadfile", type=str, help="Enter filename to save as")
parser.add_argument("--timeout", default=20, type=int, help="Enter timeout for downloading file")
args = parser.parse_args()

#webdriver options
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--disable-dev-shm-usage")
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
prefs = {"download.default_directory":args.target, ### Set the path accordingly
         "savefile.default_directory": args.target,
        "download.prompt_for_download": False, ## change the downpath accordingly
        "download.directory_upgrade": True,
        "profile.default_content_settings.popups":0
        }
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=options)

# start download
driver.get(args.url)
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, args.buttonxpath))).click()

# wait until download is done
file_count = get_current_file_count(args.target)
wait_for_download(args.timeout, args.target, file_count)
driver.quit()
print("file downloaded to: ", args.target)

print(get_latest_file(args.target))

'''

# filename formatting
filename = format_filename(args.filename)

# change filename
files_path = os.path.join(args.target, '*')
print(files_path)
list_of_files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)
print("number of files:", len(list_of_files))
latest_file = list_of_files[0]
oldext = os.path.splitext(latest_file)[1]
shutil.move(latest_file,os.path.join(args.target,filename + oldext))

# add id columns
add_id_rows(args.target + "/" + filename, "_with-id")
'''