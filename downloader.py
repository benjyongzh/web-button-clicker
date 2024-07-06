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

def get_current_file_count(target_dir):
        if os.path.exists(target_dir):
                files = os.listdir(target_dir)
                return len(files)
        else:
                return 0

def wait_for_download(timeout, target_dir, nfiles):
        seconds = 0
        dl_wait = True
        while dl_wait and seconds < timeout:
                time.sleep(1)
                dl_wait = False
                if os.path.exists(target_dir):
                        files = os.listdir(target_dir)
                        if len(files) == nfiles:
                                dl_wait = True
                        for fname in files:
                                if fname.endswith('.crdownload'):
                                        dl_wait = True
                else:
                        dl_wait = True
                seconds += 1

# set args
parser = argparse.ArgumentParser(description="Script that clicks a button on a URL to download a file")
parser.add_argument("--url", required=True, type=str,help="Enter URL of website with button to click")
parser.add_argument("--buttonclass", required=True, type=str, help="Enter a unique classname of HTML element of button to click")
parser.add_argument("--target", default="downloads", type=str, help="Enter relative file location to download file to")
parser.add_argument("--filename", default="downloadfile", type=str, help="Enter filename to save as")
parser.add_argument("--timeout", default=20, type=int, help="Enter timeout for downloading file")
args = parser.parse_args()

#webdriver options
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

# start download
driver.get(args.url)
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, args.buttonclass)))
driver.find_element(By.CLASS_NAME, args.buttonclass).click()

# wait until download is done
file_count = get_current_file_count(args.target)
wait_for_download(args.timeout, args.target, file_count)
driver.quit()

# filename formatting
currentDateTime = datetime.now()
datetime_filename_format = "%Y%m%d-%H%M%S"
date_text = currentDateTime.strftime(datetime_filename_format)
filename = date_text + "_" + args.filename

# change filename
files_path = os.path.join(args.target, '*')
list_of_files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)
latest_file = list_of_files[0]
oldext = os.path.splitext(latest_file)[1]
shutil.move(latest_file,os.path.join(args.target,filename + oldext))