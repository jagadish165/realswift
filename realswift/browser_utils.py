import os
import subprocess
import time
import shutil
import pygetwindow as gw
from config_module import config
edge_browser_path = config.edge_browser_path
chrome_browser_path = config.chrome_browser_path
browser = config.browser
screenshots_folder = config.screenshots_folder
options = config.options.split(";")
def init_browser(url):
   # try:
    if os.path.isdir(screenshots_folder):
        shutil.rmtree(screenshots_folder)
    os.mkdir(screenshots_folder)
    os.mkdir(screenshots_folder+ "/old_" + screenshots_folder)
# except Exception as e:
#    print(f"{e}")


    if browser == "chrome":
        os.system("taskkill /f /im chrome.exe")
        subprocess.Popen([chrome_browser_path, url]+options)
    elif browser == "edge":
        os.system("taskkill /f /im msedge.exe")
        subprocess.Popen([edge_browser_path, url]+options)
    time.sleep(2)

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

