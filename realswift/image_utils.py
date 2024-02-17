import os
import sys
import cv2
import numpy as np
import browser_utils as br
import pyautogui
from config_module import config
browser = config.browser
screenshots_path = config.screenshots_path
img_objects_folder = config.img_objects_folder
element_ss_path = config.element_ss_path

def _take_screenshot():
    """
    Captures a screenshot of the active window and saves it to a file.

    The function identifies the active window, captures a screenshot of that window, and saves it as an image.

    Args:
        None

    Returns:
        None
    """
    if sys.platform == "win32":
        try:
            active_window = br._activate_window()
        except Exception as e:
            print("unable to activate browser window.. trying again")
            try:
                active_window = br._activate_window()
            except Exception as e:
                print(f"unable to activate browser window..Caught exception {e}")
                exit(1)
        window_x, window_y, window_width, window_height = active_window.left, active_window.top, active_window.width, active_window.height

        screenshot = pyautogui.screenshot(region=(window_x, window_y, window_width, window_height))

        screenshot.save(screenshots_path)

    elif sys.platform == "linux":
        from wand.image import Image
        os.system(f"import -window root {screenshots_path}")
    else:
        print(f"Currently {sys.platform} platform is not supported")
        exit(1)
def _find_image(object, item_position=1, midpointRX=-1, midpointRY=-1):
    """
    Finds an image in the captured screenshot and returns its midpoint coordinates.

    The function searches for a specified image within the captured screenshot and returns the midpoint coordinates
    if a match is found.

    Args:
        object (str): The filename of the image to search for.
        item_position (int): Index of the match if there are multiple matches. Defaults to 0.
        midpointRX (int): Expected X-coordinate of the midpoint. Defaults to -1.
        midpointRY (int): Expected Y-coordinate of the midpoint. Defaults to -1.

    Returns:
        tuple: A tuple containing the X and Y coordinates of the midpoint if a match is found, or None if no match is found.
    """
    _take_screenshot()
    larger_image = cv2.imread(screenshots_path)
    template = cv2.imread(f'{img_objects_folder}/{object}')
    result = cv2.matchTemplate(larger_image, template, cv2.TM_CCORR_NORMED)
    # cv2.normalize(result, result, 0, 1, cv2.NORM_MINMAX)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    confidence_threshold = 0.999  # Adjust as needed
    loc = np.where(result >= confidence_threshold)
    i = 0
    # Draw rectangles around the matches
    for pt in zip(*loc[::-1]):  # pt marks the location of the match
        h, w = template.shape[:2]
        top_left = pt
        bottom_right = (pt[0] + w, pt[1] + h)
        midpointX = (top_left[0] + bottom_right[0]) // 2
        midpointY = (top_left[1] + bottom_right[1]) // 2
        if not midpointRX == -1:
            if abs(midpointRX - midpointX) < 5:
                midpoint = midpointX, midpointY
                break
        elif not midpointRY == -1:
            #print(f'midpoint diff of {midpointRY},{midpointY}=={abs(midpointRY - midpointY)}')
            if abs(midpointRY - midpointY) < 5:
                midpoint = midpointX, midpointY
                break
        elif item_position == i + 1:
            midpoint = midpointX, midpointY
            break
        i += 1
    cv2.rectangle(larger_image, top_left, bottom_right, (0, 0, 255), 2)
    cv2.imwrite(element_ss_path, larger_image)
    print(f"element '{object}' found at the location {midpointX},{midpointY} on the webpage with confidence: {max_val}")
    return midpoint
