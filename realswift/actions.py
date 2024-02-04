import time
import datetime
import shutil
import pyautogui
from config_module import config
from image_utils import _find_image,_take_screenshot
from ocr_utils import _perform_ocr,_analyse_ocr_results
import browser_utils as br
timeout = config.timeout
offsetx = config.offsetx
offsety = config.offsety
screenshots_folder = config.screenshots_folder
output_path = config.output_path
mousespeed = config.mousespeed
found = False
flag_executed = False

def recapture():
    """
        Capture a screenshot and perform Optical Character Recognition (OCR) on it.
    """
    _take_screenshot()
    _perform_ocr()
def type( txtToEnter, txtToFind="", exactmatch=True, object="", item=0, relative_to_word_in_x="",
         relative_to_word_in_y=""):
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


def click(txtToFind, exactmatch=True, object="", item=0, relative_word_in_x_direction="", relative_word_in_y_direction="",
          hover=False):
    """
    Click on a specified element.

    Args:
        txtToFind (str): The element to find and click on.
        exactmatch (bool): Whether to perform an exact match for the element.
        object (str): The element object to interact with.
        item (int): The index of the item to interact with.
        relative_word_in_x_direction (str): A reference word in x-axis direction to uniquely identify the element.
        relative_word_in_y_direction (str): A reference word in y-axis direction to uniquely identify the element.
        hover (bool): Whether to hover over the element instead of clicking it.
    """
    midpoint = _wait_for_element(txtToFind, exactmatch, object, item, relative_word_in_x_direction, relative_word_in_y_direction)
    x = midpoint[0] - offsetx
    y = midpoint[1] - offsety
    br._activate_window
    pyautogui.moveTo(x, y, mousespeed)
    if hover == True:
        print(f"mouse hovered on the element '{txtToFind}'")
    else:
        br._activate_window
        pyautogui.click()
        print(f"element '{txtToFind}' clicked")


def scroll( direction, clicks=1, txtToFind="",action="move",exactmatch=True):
    """
    Scroll the screen in a specified direction.

    Args:
        direction (str): The direction of scrolling ("up", "down", "left", "right").
        clicks (int): The number of times to scroll.
        txtToFind (str): The element to find during scrolling.
        action (str): Action to be performed after scrolling values = ("move","click").. default 'move'.
        exactmatch (bool): Whether to perform an exact match for the element.
    """
    global results
    scroll_duration = 0.1
    midpoint = False
    found = False
    start_time = time.time()
    while not found and time.time() - start_time < timeout:
        if not txtToFind == "":
            _take_screenshot()
            _perform_ocr()
            midpoint = _wait_for_element(txtToFind, exactmatch, "", 0, "", "", True)
        if txtToFind != "":
            if not midpoint:
                print(f"element '{txtToFind}' not found after scrolling in {direction} direction...scrolling further")
            else:
                print(f"element '{txtToFind}' found after scrolling in {direction} direction")
                found = True
                break
        if direction == "up":
            print(f"scrolling {direction}...")
            for _ in range(clicks):
                pyautogui.press('up')
                time.sleep(scroll_duration)
        elif direction == "down":
            print(f"scrolling {direction}...")
            for _ in range(clicks):
                pyautogui.press('down')
                time.sleep(scroll_duration)
        elif direction == "left":
            print(f"scrolling {direction}...")
            for _ in range(clicks):
                pyautogui.press('left')
                time.sleep(scroll_duration)
        elif direction == "right":
            print(f"scrolling {direction}...")
            for _ in range(clicks):
                pyautogui.press('right')
                time.sleep(scroll_duration)
        if txtToFind == "":
            break
    results = []
    if found:
        x = midpoint[0] - offsetx
        y = midpoint[1] - offsety
        br._activate_window
        pyautogui.moveTo(x, y, mousespeed)
        if action == "click":
            br._activate_window
            pyautogui.click()
            print(f"element '{txtToFind}' clicked")



def hover(txtToFind, exactmatch=True, object="", item=0, relative_to_word_in_x="", relative_to_word_in_y="",
          hover=True):
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
    click(txtToFind, exactmatch, object, item, relative_to_word_in_x, relative_to_word_in_y, hover)

def _wait_for_element(txt, exactmatch, object, item, relative_to_word_in_x, relative_to_word_in_y, scroll=False):
    """
    Wait for a page element to appear.

    Args:
        txt (str): The text to wait for on the page.
        exactmatch (bool): Whether to perform an exact match for the element.
        object (str): The element object to interact with.
        item (int): The index of the item to interact with.
        relative_to_word_in_x (str): A reference word in x-axis direction to uniquely identify the element.
        relative_to_word_in_y (str): A reference word in y-axis direction to uniquely identify the element.
        scroll (bool): Whether to perform scrolling if the element is not found.

    Returns:
        tuple: The coordinates of the found element.
    """
    start_time = time.time()
    global found
    found = False
    exc = None
    stck = None

    while not found and time.time() - start_time < timeout:
        try:
            if not object == "":
                if not relative_to_word_in_x == "":
                    midpointR = _analyse_ocr_results(relative_to_word_in_x, exactmatch, )
                    midpoint = _find_image(object, item, midpointRY=midpointR[1])
                elif not relative_to_word_in_y == "":
                    midpointR = _analyse_ocr_results(relative_to_word_in_y, exactmatch, )
                    midpoint = _find_image(object, item, midpointRX=midpointR[0])
                else:
                    midpoint = _find_image(object)
                found = True
                break
            else:
                if not relative_to_word_in_x == "":
                    midpointR = _analyse_ocr_results(relative_to_word_in_x, exactmatch, item)
                    midpoint = _analyse_ocr_results(txt, exactmatch, item, midpointRY=midpointR[1])
                elif not relative_to_word_in_y == "":
                    top_leftR = _analyse_ocr_results(relative_to_word_in_y, exactmatch, item, y_axis=True)
                    midpoint = _analyse_ocr_results(txt, exactmatch, item, top_leftRX=top_leftR)
                else:
                    midpoint = _analyse_ocr_results(txt, exactmatch, item)
                found = True
                print(f"element '{txt}' found at location {midpoint} on the webpage")
                try:
                    now = datetime.datetime.now()
                    new_file_name = f"analysed_screenshot_{now.strftime('%Y-%m-%d-%H-%M-%S')}.png"
                    shutil.copyfile(output_path, screenshots_folder + "/old_" + screenshots_folder + "/" + new_file_name)
                except Exception as e:
                    print(f"unable to copy analysed_screenshot to old_{screenshots_folder}.. getting exception {e}")
                break
        except Exception as e:
            print(f"element '{txt}' not found...reading text from the webpage again")
            exc = e
        time.sleep(1)
        if not scroll:
            _take_screenshot()
        if object == "" and not scroll:
            _perform_ocr()
        elif object != "":
            if relative_to_word_in_y != "" or relative_to_word_in_x != "":
                _perform_ocr()
        if scroll:
            midpoint = False
            break
    if not found and not scroll:
        print(f"element '{txt}' not found within {timeout} secs...exiting the script")
        raise exc
        exit(1)
    return midpoint
