import cv2
import numpy as np
import pygetwindow as gw
import pyautogui
from config_module import config
browser = config.browser
screenshot_path = config.screenshot_path


def _take_screenshot():
    """
    Captures a screenshot of the active window and saves it to a file.

    The function identifies the active window, captures a screenshot of that window, and saves it as an image.

    Args:
        None

    Returns:
        None
    """
    if browser == "chrome":
        active_window = gw.getWindowsWithTitle("Google Chrome")
    elif browser == "edge":
        active_window = gw.getWindowsWithTitle(" Edge")

    if active_window is not None:
        active_window = active_window[0]
        active_window.activate()
        #_activate_window()
        # Get the position and size of the active window
        window_x, window_y, window_width, window_height = active_window.left, active_window.top, active_window.width, active_window.height

        # Take a screenshot of the active window
        screenshot = pyautogui.screenshot(region=(window_x, window_y, window_width, window_height))

        # Save the screenshot to a file
        screenshot.save(screenshot_path)

        # Optionally, you can display the screenshot
        # screenshot.show()
    else:
        print("No active window found.")


def _find_image(object, item=0, midpointRX=-1, midpointRY=-1):
    """
    Finds an image in the captured screenshot and returns its midpoint coordinates.

    The function searches for a specified image within the captured screenshot and returns the midpoint coordinates
    if a match is found.

    Args:
        object (str): The filename of the image to search for.
        item (int): Index of the match if there are multiple matches. Defaults to 0.
        midpointRX (int): Expected X-coordinate of the midpoint. Defaults to -1.
        midpointRY (int): Expected Y-coordinate of the midpoint. Defaults to -1.

    Returns:
        tuple: A tuple containing the X and Y coordinates of the midpoint if a match is found, or None if no match is found.
    """
    _take_screenshot()
    larger_image = cv2.imread("target/screenshot.png")
    template = cv2.imread(f'../objects/{object}.png')
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
        print(f'{midpointX},{midpointY}')
        if not midpointRX == -1:
            if abs(midpointRX - midpointX) < 5:
                midpoint = midpointX, midpointY
        elif not midpointRY == -1:
            print(f'midpoint diff of {midpointRY},{midpointY}=={abs(midpointRY - midpointY)}')
            if abs(midpointRY - midpointY) < 5:
                midpoint = midpointX, midpointY
        elif item == i:
            midpoint = midpointX, midpointY
        cv2.rectangle(larger_image, top_left, bottom_right, (0, 0, 255), 2)
        i += 1
    cv2.imwrite("target/objectOutput.png", larger_image)
    print(f"Confidence: {max_val}")
    return midpoint
