import os
import subprocess
import time
import shutil
import pygetwindow as gw
from config_module import config
edge_browser_path = config.edge_browser_path
chrome_browser_path = config.chrome_browser_path
browser = config.browser
def init_browser(url):
    try:
        shutil.rmtree("target")
        os.mkdir("target")
        os.mkdir("target/old_ss")
    except Exception as e:
        print(f"{e}")


    if browser == "chrome":
        os.system("taskkill /f /im chrome.exe")
        subprocess.Popen([chrome_browser_path, "--incognito", url])
    elif browser == "edge":
        os.system("taskkill /f /im msedge.exe")
        subprocess.Popen([edge_browser_path, "--inprivate", url])
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

