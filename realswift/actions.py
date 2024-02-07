import shutil
import time

import pyautogui
import datetime

import browser_utils as br
from config_module import config
from image_utils import _take_screenshot
from internal import _wait_for_element
import internal
from ocr_utils import _perform_ocr
from realswift.exceptions import InvalidScrollOptionException, ElementNotFoundException
from reporter import report
retries = config.retries
screenshots_folder = config.screenshots_folder
screenshots_path = config.screenshots_path
output_path = config.output_path
element_ss_path = config.element_ss_path
offsetx_default = config.offsetx_default
offsety_default = config.offsety_default

mousespeed = config.mousespeed
found = False
flag_executed = False
def recapture():
    """
        Capture a screenshot and perform Optical Character Recognition (OCR) on it.
    """
    _take_screenshot()
    _perform_ocr()
def press_key(keyToPress,noOfPresses=1):
    """
           Simulate pressing a keyborad button.
           available values check here : https://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys

           Args:
               txtToEnter (str): The keyboard button to press.
    """
    pyautogui.press(keyToPress,noOfPresses)
def type( txtToEnter, txtToFind="", exactmatch=True, object="", item=0, relative_to_word_in_x="",
         relative_to_word_in_y="",offsetx=offsetx_default,offsety=offsety_default):
    """
        Simulate typing a string and clicking on a specified element.

        Args:
            txtToEnter (str): The text to type.
            txtToFind (str): The element to find and click on.
            exactmatch (bool): Whether to perform an exact match for element.
            object (str): The element object to interact with.
            item (int): The index of the item to interact with.
            relative_to_word_in_x (str): A reference word in x-axis direction to uniquely identify the element.
            relative_to_word_in_y (str): A reference word in y-axis direction to uniquely identify the element.
    """
    start_time = datetime.datetime.now()

    if not txtToFind == "":
        midpoint = _wait_for_element(txtToFind, exactmatch, object, item, relative_to_word_in_x, relative_to_word_in_y)
        x = midpoint[0] - offsetx
        y = midpoint[1] - offsety
        br._activate_window
        pyautogui.moveTo(x, y, mousespeed)
    br._activate_window
    pyautogui.click()
    br._activate_window
    pyautogui.typewrite(txtToEnter)
    print(f"typed '{txtToEnter}'")

    time_diff = datetime.datetime.now() - start_time
    time_diff = str(time_diff)[:-4]
    _take_screenshot()
    try:
        now = datetime.datetime.now()
        new_file_path = f"{screenshots_folder}/old_{screenshots_folder}/element_screenshot_{now.strftime('%Y-%m-%d-%H-%M-%S')}.png"
        shutil.copyfile(screenshots_path, new_file_path)
    except Exception as e:
        print(f"unable to copy analysed_screenshot to old_{screenshots_folder}.. getting exception {e}")
    report(f"Typed '{txtToEnter}'","Passed",time_diff,new_file_path)

def click(txtToFind, exactmatch=True, item=0, relative_word_in_x_direction="", relative_word_in_y_direction="",offsetx=offsetx_default,offsety=offsety_default):
    """
    Click on a specified element.

    Args
        txtToFind (str): The element to find and click on.
        exactmatch (bool): Whether to perform an exact match for the element.
        object (str): The element object to interact with.
        item (int): The index of the item to interact with.
        relative_word_in_x_direction (str): A reference word in x-axis direction to uniquely identify the element.
        relative_word_in_y_direction (str): A reference word in y-axis direction to uniquely identify the element.
    """
    start_time = datetime.datetime.now()

    midpoint = _wait_for_element(txtToFind, exactmatch,"", item, relative_word_in_x_direction, relative_word_in_y_direction)
    x = midpoint[0] - offsetx
    y = midpoint[1] - offsety
    br._activate_window
    pyautogui.moveTo(x, y, mousespeed)
    pyautogui.click()
    print(f"clicked on the element '{txtToFind}'")

    time_diff = datetime.datetime.now() - start_time
    time_diff = str(time_diff)[:-4]
    report(f"Clicked on the element '{txtToFind}'","Passed",time_diff,internal.new_file_path)

def click_img_object(object, item=0, relative_word_in_x_direction="", relative_word_in_y_direction="",offsetx=offsetx_default,offsety=offsety_default):
    """
    Click on a specified image object.

    Args
        txtToFind (str): The element to find and click on.
        exactmatch (bool): Whether to perform an exact match for the element.
        object (str): The element object to interact with.
        item (int): The index of the item to interact with.
        relative_word_in_x_direction (str): A reference word in x-axis direction to uniquely identify the element.
        relative_word_in_y_direction (str): A reference word in y-axis direction to uniquely identify the element.
    """
    start_time = datetime.datetime.now()

    midpoint = _wait_for_element("", True, object, item, relative_word_in_x_direction, relative_word_in_y_direction)
    x = midpoint[0] - offsetx
    y = midpoint[1] - offsety
    br._activate_window
    pyautogui.moveTo(x, y, mousespeed)
    pyautogui.click()
    print(f"clicked on the img object '{object}'")

    time_diff = datetime.datetime.now() - start_time
    time_diff = str(time_diff)[:-4]
    report(f"Clicked on the img object '{object}''","Passed",time_diff,internal.new_file_path)


def scroll_find_click(txtToFind,direction="down", scrolls=1,exactmatch=True,offsetx=offsetx_default,offsety=offsety_default):
    """
        Scroll the screen in a specified direction and find text and click

        Args:
            txtToFind (str): The element to find during scrolling.
            direction (str): The direction of scrolling ("up", "down", "left", "right").
            scrolls (int): The number of times to scroll.
            exactmatch (bool): Whether to perform an exact match for the element.
        """
    start_time = datetime.datetime.now()
    midpoint = scroll_find(txtToFind,direction,scrolls,exactmatch)
    x = midpoint[0] - offsetx
    y = midpoint[1] - offsety
    br._activate_window
    pyautogui.moveTo(x, y, mousespeed)
    pyautogui.click()
    time_diff = datetime.datetime.now() - start_time
    time_diff = str(time_diff)[:-4]
    print(f"scrolled and clicked on the element '{txtToFind}'")
    report(f"Scrolled and clicked on the element '{txtToFind}'","Passed",time_diff,internal.new_file_path)

def scroll_find( txtToFind="",direction="down", scrolls=1,exactmatch=True):
    """
    Scroll the screen in a specified direction and find text.

    Args:
        txtToFind (str): The element to find during scrolling.
        direction (str): The direction of scrolling ("up", "down", "left", "right").
        scrolls (int): The number of times to scroll.
        exactmatch (bool): Whether to perform an exact match for the element.
    """
    global results
    midpoint = False
    found = False
    start_try = 0
    retries = scrolls
    while not found and start_try < retries:
        if not txtToFind == "":
            _take_screenshot()
            _perform_ocr()
            midpoint = _wait_for_element(txtToFind, exactmatch, "", 0, "", "", True)
        if txtToFind != "":
            if not midpoint:
                print(f"element '{txtToFind}' not found after scrolling in {direction} direction...scrolling further")
            else:
                #print(f"element '{txtToFind}' found after scrolling in {direction} direction")
                found = True
                break
        scroll(direction,scrolls)
        start_try = start_try + 1
    if not found:
        try:
            raise Exception(f"element '{txtToFind}' not found within {retries} scrolls...exiting the script")
        except ElementNotFoundException as ce:
            print(f"Caught an exception: {ce.message}")
            report(f"Element '{txtToFind}' not found", "Failed", "NA", screenshots_path)
            br.tear_down()
            exit(1)
        exit(1)
    results = []
    return midpoint

def scroll(direction="down",scrolls=1):
    scroll_duration = 0.1
    if direction == "up":
        print(f"scrolling {direction}...")
        for _ in range(scrolls):
            pyautogui.press('up')
            time.sleep(scroll_duration)
    elif direction == "down":
        print(f"scrolling {direction}...")
        for _ in range(scrolls):
            pyautogui.press('down')
            time.sleep(scroll_duration)
    elif direction == "left":
        print(f"scrolling {direction}...")
        for _ in range(scrolls):
            pyautogui.press('left')
            time.sleep(scroll_duration)
    elif direction == "right":
        print(f"scrolling {direction}...")
        for _ in range(scrolls):
            pyautogui.press('right')
            time.sleep(scroll_duration)
    else:
        try:
            raise InvalidScrollOptionException("not a valid scroll input")
        except InvalidScrollOptionException as ce:
            print(f"Caught an exception: {ce.message}")
            exit(1)


def hover(txtToFind, exactmatch=True, object="", item=0, relative_word_in_x_direction="", relative_word_in_y_direction="",offsetx=offsetx_default,offsety=offsety_default):
    """
        Hover over a specified element.

        Args:
            txtToFind (str): The element to find and hover over.
            exactmatch (bool): Whether to perform an exact match for the element.
            object (str): The element object to interact with.
            item (int): The index of the item to interact with.
            relative_to_word_in_x (str): A reference word in x-axis direction to uniquely identify the element.
            relative_to_word_in_y (str): A reference word in y-axis direction to uniquely identify the element.
            hover (bool): Whether to hover over the element.
    """
    start_time = datetime.datetime.now()

    midpoint = _wait_for_element(txtToFind, exactmatch, object, item, relative_word_in_x_direction,
                                 relative_word_in_y_direction)
    x = midpoint[0] - offsetx
    y = midpoint[1] - offsety
    br._activate_window
    pyautogui.moveTo(x, y, mousespeed)
    print(f"hovered on the element '{txtToFind}'")

    time_diff = datetime.datetime.now() - start_time
    time_diff = str(time_diff)[:-4]
    report(f"Hovered on the element '{txtToFind}'","Passed",time_diff,internal.new_file_path)


