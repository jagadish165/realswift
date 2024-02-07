import os
import subprocess
import time
import shutil

import psutil
import pygetwindow as gw
from reporter import generate_html
from config_module import config
edge_browser_path = config.edge_browser_path
chrome_browser_path = config.chrome_browser_path
browser = config.browser
screenshots_folder = config.screenshots_folder
options = config.options.split(";")
window_chk = any("--window-size" in element for element in options)
if window_chk:
    options.append("--window-position=0,0")
def open_browser(url):
    global proc
   # try:
    if os.path.isdir(screenshots_folder):
        shutil.rmtree(screenshots_folder)
    os.mkdir(screenshots_folder)
    os.mkdir(screenshots_folder+ "/old_" + screenshots_folder)
# except Exception as e:
#    print(f"{e}")


    if browser == "chrome":
        proc = subprocess.Popen([chrome_browser_path, url]+options,stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    shell=True)
    elif browser == "edge":
        proc = subprocess.Popen([edge_browser_path, url]+options,stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    shell=True)
    time.sleep(2)
def tear_down():
    proc.kill
    exit(0)
def _activate_window():
    try:
        if browser == "chrome":
            active_window = gw.getWindowsWithTitle("Google Chrome")
            active_window[0].activate()
        elif browser == "edge":
            active_window = gw.getWindowsWithTitle("Edge")
            active_window[0].activate()
    except Exception as e:
        print(f"window activation failed with error {e}")

