# realswift
Break free from DOM with AI-powered automation. Eliminate the traditional, often repetitive, and manual process of specifying or identifying specific elements (like buttons, links, or fields) on a web page using Document Object Model (DOM) selectors.


This project designed for automating user interactions with opencv2 using the pyautogui library and some custom utility functions. The script provides several functions to simulate user actions, such as typing, clicking, scrolling, and hovering, within a specified window or area.

Prerequisites
Before using this script, make sure you have the following prerequisites installed:

Python: Ensure you have Python installed on your system.

Required Python packages: Install the necessary packages, which are listed in the requirements.txt file. You can install them using pip:

````
pip install -r requirements.txt
````
Configuration: Adjust the configuration parameters in the config.py file to match your specific use case.

Usage
The script provides the following functions:


| Method | Parameter | Description |
|--------|-----------|-------------|
| `type` | `txtToEnter` | The text to type. |
|        | `txtToFind` | The element to find and click on. |
|        | `exactmatch` | Whether to perform an exact match for the element (boolean). |
|        | `object` | The element object to interact with. |
|        | `item` | The index of the item to interact with. |
|        | `relative_word_in_x_direction` | A reference word in x-axis direction to uniquely idenfity element. |
|        | `relative_word_in_y_direction` | A reference word in y-axis direction to uniquely idenfity element. |
| `click` | `txtToFind` | The element to find and click on. |
|        | `exactmatch` | Whether to perform an exact match for the element (boolean). |
|        | `object` | The element object to interact with. |
|        | `item` | The index of the item to interact with. |
|        | `relative_word_in_x_direction` | A reference word in x-axis direction to uniquely idenfity element. |
|        | `relative_word_in_y_direction` | A reference word in y-axis direction to uniquely idenfity element. |
|        | `hover` | Whether to hover over the element instead of clicking it (boolean). |
| `scroll` | `direction` | The direction of scrolling ("up", "down", "left", "right"). |
|        | `clicks` | The number of times to scroll. |
|        | `txtToFind` | The element to find during scrolling. |
| `hover` | `txtToFind` | The element to find and hover over. |
|        | `exactmatch` | Whether to perform an exact match for the element (boolean). |
|        | `object` | The element object to interact with. |
|        | `item` | The index of the item to interact with. |
|        | `relative_to_word_in_x` | A reference word for x-axis positioning. |
|        | `relative_to_word_in_y` | A reference word for y-axis positioning. |
|        | `hover` | Whether to hover over the element (boolean). |

To use these functions, simply import the script and call the desired function with the appropriate arguments.




