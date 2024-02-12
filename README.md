# realswift
AI automation tool leverages a cognitive approach inspired by the human brain's intuitive understanding of web interfaces.

*Attention: Please note that this project requires substantial CPU and GPU resources to ensure faster outcomes. The higher the Computer specifications, the faster the results can be obtained.*

Break free from DOM (Xpaths,CSS etc.,) with AI-powered automation. Eliminate the traditional, often repetitive, and manual process of specifying or identifying specific elements (like buttons, links, or fields) on a web page using Document Object Model (DOM) selectors.



This project is crafted to automate user interactions with OpenCV2 utilizing the PyAutoGUI library alongside custom utility functions. The script offers various functionalities to replicate user actions, including typing, clicking, scrolling, and hovering, within a designated window or defined area.
Prerequisites
Before using this script, make sure you have the following prerequisites installed:

Python: 

Ensure you have Python <=3.11 installed on your system.(above 3.11 doesn't work for some of the pyTorch components)

Required dependency packages: 

Install the necessary packages, which are listed in the requirements.txt file. You can install them using pip:
````
pip install -r requirements.txt
````
Install pytorch:
````
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
````
Install realswift latest version:
````
pip install realswift
````

Create .py files and run the following example scripts.

**Example Script 1:**

Scenario: 
* Open Amazon India website.
* Search for "apple watch".
* Scroll down and select "Apple Watch Ultra 2".
* View bank offers and details.
* Navigate back.
* Proceed to checkout.

````
from realswift.actions import *
from realswift.browser_utils import open_browser

open_browser("https://www.amazon.in")
click("Search Amazon.in")
type("apple watch")
press_keys("enter")
scroll_find_click("Apple Watch Ultra 2","down",10,exactmatch=False)
click("Bank offer")
click("See details >",item=1,offsety=3)
click("Offer 2")
scroll("down",4)
click("Back")
click("Bank offer")
scroll_find_click("Buy Now",scrolls=4)
````

**Example Script 2:**

Scenario:
* Opens Nykaa.com
* Hovers over "Mom & Baby" and "Bath & Body".
* Clicks on "Hand Wash".
* Scrolls to find prices and products under ₹500.
* Scrolls to find discounts and products with 30% discount or less.
* Scrolls back to "Bath & Body" category and clicks on the second item.
````
from realswift.browser_utils import open_browser
from realswift.actions import *

open_browser("https://www.nykaa.com")
hover("Mom & Baby")
hover("Bath & Body")
click("Hand Wash")
scroll_find_click("Price","down",5)
scroll_find_click("500","down",5,False)
scroll_find_click("Disdcount","down",5)
scroll_find_click("30% And","down",5,False)
scroll_find("Bath & Body","down",5,False)
click("Bath & Body",exactmatch=False,item=2)
````
Configuration: Create a config.json file and adjust the following default configuration parameters in the config.json file.

(Note:- You can skip creating config.json or skip adding one or more parameters to take below default values)
````
{
  "chrome_browser_path": "C:/Program Files/Google/Chrome/Application/chrome.exe",
  "edge_browser_path": "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
  "offsetx_default": 0,
  "offsety_default": 0,
  "mousespeed": 0.2,
  "screenshots_folder": "screenshots",
  "img_objects_folder": "img_objects",
  "retries": 5,
  "browser": "chrome",
  "options": "--start-maximized"
}
````
# Automation Functions Documentation

markdown

| Method                | Parameter                      | Description                                       | Default Value |
|-----------------------|--------------------------------|---------------------------------------------------|---------------|
| `press_keys`          | `keyToPress`                   | The keyboard button to press.                    | None(*Mandatory parameter*)          |
|                       | `noOfPresses`                  | The number of times to press the key.            | 1             |
| `type_keys`           | `txtToEnter`                   | The text to type.                                 | None(*Mandatory parameter*)          |
| `type`                | `txtToEnter`                   | The text to type.                                 | None(*Mandatory parameter*)          |
|                       | `txtToFind`                    | The element to find and type.                     | None(*Mandatory parameter*)          |
|                       | `exactmatch`                   | Whether to perform an exact match for the element.| True          |
|                       | `item`                         | The index of the item to interact with.           | 0             |
|                       | `relative_to_word_in_x`        | A reference word in the x-axis direction.        | ""            |
|                       | `relative_to_word_in_y`        | A reference word in the y-axis direction.        | ""            |
|                       | `offsetx`                      | Offset for the identified x-coordinate.          | config.offsetx_default |
|                       | `offsety`                      | Offset for the identified y-coordinate.          | config.offsety_default |
| `click`               | `txtToFind`                    | The element to find and click on.                | None(*Mandatory parameter*)          |
|                       | `exactmatch`                   | Whether to perform an exact match for the element.| True          |
|                       | `item`                         | The index of the item to interact with.           | 0             |
|                       | `relative_word_in_x_direction` | A reference word in the x-axis direction.        | ""            |
|                       | `relative_word_in_y_direction` | A reference word in the y-axis direction.        | ""            |
|                       | `offsetx`                      | Offset for the identified x-coordinate.          | config.offsetx_default |
|                       | `offsety`                      | Offset for the identified y-coordinate.          | config.offsety_default |
| `click_img_object`    | `object`                       | The image object to interact with.               | None(*Mandatory parameter*)          |
|                       | `item`                         | The index of the item to interact with.           | 0             |
|                       | `relative_word_in_x_direction` | A reference word in the x-axis direction.        | ""            |
|                       | `relative_word_in_y_direction` | A reference word in the y-axis direction.        | ""            |
|                       | `offsetx`                      | Offset for the identified x-coordinate.          | config.offsetx_default |
|                       | `offsety`                      | Offset for the identified y-coordinate.          | config.offsety_default |
| `scroll_find_click`   | `txtToFind`                    | The element to find during scrolling.            | None(*Mandatory parameter*)          |
|                       | `direction`                    | The direction of scrolling ("up", "down", etc.).  | "down"        |
|                       | `scrolls`                      | The number of times to scroll.                   | 1             |
|                       | `exactmatch`                   | Whether to perform an exact match for the element.| True          |
|                       | `offsetx`                      | Offset for the identified x-coordinate.          | config.offsetx_default |
|                       | `offsety`                      | Offset for the identified y-coordinate.          | config.offsety_default |
| `scroll_find`         | `txtToFind`                    | The element to find during scrolling.            | None(*Mandatory parameter*)          |
|                       | `direction`                    | The direction of scrolling ("up", "down", etc.).  | "down"        |
|                       | `scrolls`                      | The number of times to scroll.                   | 1             |
|                       | `exactmatch`                   | Whether to perform an exact match for the element.| True          |
| `scroll`              | `direction`                    | The direction of scrolling ("up", "down", etc.).  | "down"        |
|                       | `scrolls`                      | The number of times to scroll.                   | 1             |
| `hover`               | `txtToFind`                    | The element to find and hover over.               | None(*Mandatory parameter*)          |
|                       | `exactmatch`                   | Whether to perform an exact match for the element.| True          |
|                       | `item`                         | The index of the item to interact with.           | 0             |
|                       | `relative_word_in_x_direction` | A reference word in the x-axis direction.        | ""            |
|                       | `relative_word_in_y_direction` | A reference word in the y-axis direction.        | ""            |
|                       | `offsetx`                      | Offset for the identified x-coordinate.          | config.offsetx_default |
|                       | `offsety`                      | Offset for the identified y-coordinate.          | config.offsety_default |
| `hover_img_object`    | `object`                       | The image object to interact with.               | None(*Mandatory parameter*)          |
|                       | `item`                         | The index of the item to interact with.           | 0             |
|                       | `relative_word_in_x_direction` | A reference word in the x-axis direction.        | ""            |
|                       | `relative_word_in_y_direction` | A reference word in the y-axis direction.        | ""            |
|                       | `offsetx`                      | Offset for the identified x-coordinate.          | config.offsetx_default |
|                       | `offsety`                      | Offset for the identified y-coordinate.          | config.offsety_default |

- For more details on each function and their usage, refer to the respective function's docstring in the script.

## Created by: 

Jagadish Dabbiru [[Linked In](https://www.linkedin.com/in/jagadish-dabbiru)] 

For queries/support: realswiftsupport165@gmail.com


