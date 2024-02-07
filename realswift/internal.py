import time
import datetime
import shutil

from config_module import config
from image_utils import _find_image,_take_screenshot
from ocr_utils import _perform_ocr,_analyse_ocr_results
from exceptions import ElementNotFoundException
from realswift.browser_utils import tear_down
from reporter import report

retries = config.retries
screenshots_folder = config.screenshots_folder
screenshots_path = config.screenshots_path
output_path = config.output_path
element_ss_path = config.element_ss_path
mousespeed = config.mousespeed
found = False
flag_executed = False

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
    start_try = 0
    global found
    global new_file_path
    found = False
    exc = None
    stck = None

    while not found and start_try < retries:
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
                break
        except Exception as e:
            print(f"element not found...reading text from the webpage again")
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
        start_try = start_try + 1
    if not found and not scroll:
        try:
            raise ElementNotFoundException(f"element '{txt}' not found within {retries} retries...exiting the script")
        except ElementNotFoundException as ce:
            print(f"Caught an exception: {ce.message}")
            report(f"Element '{txt}' not found", "Failed", "NA", screenshots_path)
            tear_down()
            exit(1)
    try:
        now = datetime.datetime.now()
        new_file_path = f"{screenshots_folder}/old_{screenshots_folder}/element_screenshot_{now.strftime('%Y-%m-%d-%H-%M-%S')}.png"
        shutil.copyfile(element_ss_path, new_file_path)
    except Exception as e:
        print(f"unable to copy analysed_screenshot to old_{screenshots_folder}.. getting exception {e}")

    return midpoint
