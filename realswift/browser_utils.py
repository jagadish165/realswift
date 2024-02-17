import os
import subprocess
import sys
import time
import shutil
from config_module import config

browser_path = config.browser_path
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
    os.mkdir(screenshots_folder + "/old_" + screenshots_folder)
    # except Exception as e:
    #    print(f"{e}")

    proc = subprocess.Popen([browser_path, url] + options, stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL,
                            close_fds=True)
    time.sleep(2)


def tear_down():
    proc.kill
    exit(0)


def _activate_window():
    if sys.platform == "win32":
        import pygetwindow as gw
        try:
            if browser == "chrome":
                active_window = gw.getWindowsWithTitle("Google Chrome")
                active_window[0].activate()
            elif browser == "edge":
                active_window = gw.getWindowsWithTitle("Edge")
                active_window[0].activate()
            elif browser == "firefox":
                active_window = gw.getWindowsWithTitle("Firefox")
                active_window[0].activate()
        except Exception as e:
            print(f"window activation failed with error {e}")
        return active_window[0]
