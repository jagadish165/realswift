# Realswift

Realswift is an AI automation tool leverages a cognitive approach inspired by the human brain's intuitive understanding of web interfaces.

#### Attention: 

*Please note that this project requires powerful CPU and GPU resources to get faster execution times. The higher the Computer specifications, the faster the results can be obtained.*

#### Why Realswift?

Break free from DOM identifications (Xpaths,CSS etc.,) with AI-powered automation. Eliminate the traditional, often repetitive, and manual tedious process of specifying or identifying web elements with DOM Xpath, CSS selectors (like buttons, links, or fields).

This project is crafted to automate user interactions with Open Source Computer Vision Library. This offers various functionalities to replicate user actions, including typing, clicking, scrolling, and hovering, within a designated window or defined area.


|        | Linux | macOS | Windows |
|:-------| :---: | :---: | :---:   |
| Chrome | ✅ | ✅ | ✅ |
| Edge   | ✅ | ✅ | ✅ |
| Firfox | ✅ | ✅ | ✅ |



## Getting Started:

### Prerequisites

Ensure you have Python <=3.11 installed on your system.(above 3.11 doesn't work for some of the pyTorch components)

### Installation:

Install realswift latest version:
````
pip install realswift
````
Install pytorch with Cuda for GPU enabled machines:
````
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
````
###### Additional Packages for Linux Users

If you are using Linux, you may need to install the following additional packages:

- **ImageMagick**
- **Xvfb (X virtual framebuffer)**
- **tkinter**
- **xlib**

Set 0 for DISPLAY variable 

````export DISPLAY-:0````

### Usage

Create .py files and run the following example scripts.

**Example Script 1:**

Scenario: 
* Open Amazon India website.
* Search for "apple watch".
* Scroll down and select "Apple Watch Series 9".
* View bank offers and details.
* Navigate back.
* Proceed to checkout.

````
from realswift.actions import *
from realswift.browser_utils import open_browser

open_browser("https://www.amazon.in")                                   #Opens amazon.in browser
click("Search Amazon.in")                                               #Tries to identify "Search Amazon.in" string from the webpage and clicks it  
type_keys("apple watch")                                                #Enters "apple watch" in the search field
press_keys("enter")                                                     #Clicks enter 
scroll_find_click("Apple Watch Series 9","down",10,exactmatch=False)    #Tries to identify "Apple Watch Series 9" substring for each scroll down 10 times 
click("Bank offer")                                                     #Tries to identify "Bank offer" string from the webpage and clicks it
click("See details",item_position=2,exactmatch=False,offsety=3)         #Tries to identify second "See details" string from the webpage and clicks offset of 3 pixels 
click("Offer 2")                                                        #Tries to identify "Offer 2" string from the webpage and clicks it 
scroll("down",4)                                                        #Scrolls down 4 times             
click("Back")                                                           #Tries to identify "Back" string from the webpage and clicks it 
scroll_find_click("Buy Now",scrolls=4)                                  #Tries to identify "Buy now" string by scrolling down 10 times
````

**Example Script 2:**

Scenario:
* Opens Nykaa.com
* Hovers over "Mom & Baby" and "Bath & Body".
* Clicks on "Hand Wash".
* Scrolls to find prices and products under ₹500.
* Scrolls to find discounts and products with 30% discount or less.
* Scrolls back to "Bath & Body" category and clicks on the second item_position.
````
from realswift.browser_utils import open_browser
from realswift.actions import *

open_browser("https://www.nykaa.com")                   #Opens nykaa.com browser
hover("Mom & Baby")                                     #Tries to identify "Mom & Baby" string from the webpage and hovers on it
hover("Bath & Body")                                    #Tries to identify "Bath & Body" string from the webpage and hovers on it
click("Hand Wash")                                      #Tries to identify "Hand Wash" string from the webpage and clicks on it
scroll_find_click("Price","down",5)                     #Tries to identify "Price" string by for each scroll down 5 times and clicks on it 
scroll_find_click("500","down",5,False)                 #Tries to identify "500" substring by for each scroll down 5 times and clicks on it
scroll_find_click("Discount","down",5)                  #Tries to identify "Discount" string by for each scroll down 5 times and clicks on it
scroll_find_click("30% And","down",5,False)             #Tries to identify "30%" substring by for each scroll down 5 times and clicks on it   
scroll_find("Bath & Body","down",5,False)               #Tries to identify "Bath & Body" substring by for each scroll down 5 times and clicks on it   
click("Bath & Body",exactmatch=False,item_position=2)   #Tries to identify 2nd element "Bath & Body" substring from the webpage and clicks on it

````
### Configuration: 

Create a config.json file and adjust the following default configuration parameters in the config.json file.

(Note:- You can skip creating config.json or skip adding one or more parameters to take below default values)
````
{
  "browser_path": "C:/Program Files/Google/Chrome/Application/chrome.exe",
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
### Image Identification

If there are web elements which doesn't have readable text ex:- icons,logos..etc., then use Image identification methods.

Create [img_objects](realswift/tests/img_objects)  folder in the same directory. Take screenshot of the webpage, crop image of the web object and place inside the folder. Click the object using image related functions defined in the lower section. 

### Output:

After the execution, [screenshots](realswift/tests/screenshots) folder will be created in the same directory and **[output.html](https://htmlpreview.github.io/?https://github.com/jagadish165/realswift/blob/main/realswift/tests/screenshots/output.html)** report will be generated inside it. You can check various identified webpage screenshots through out the execution.

## Automation Functions Documentation

| Method                | Parameter                      | Description                                | Default Value               |
|-----------------------|--------------------------------|--------------------------------------------|-----------------------------|
| `press_keys`          | `keyToPress`                   | The keyboard button to press.              | None(*Mandatory parameter*) |
|                       | `noOfPresses`                  | The number of times to press the key.      | 1                           |
| `type_keys`           | `txtToEnter`                   | The text to type.                          | None(*Mandatory parameter*) |
| `type`                | `txtToEnter`                   | The text to type.                          | None(*Mandatory parameter*) |
|                       | `txtToFind`                    | The element to find and type.              | None(*Mandatory parameter*) |
|                       | `exactmatch`                   | Whether to perform an exact match for the element. | True                        |
|                       | `item_position`                | The position of the item to interact with. | 1                           |
|                       | `relative_to_word_in_x`        | A reference word in the x-axis direction.  | ""                          |
|                       | `relative_to_word_in_y`        | A reference word in the y-axis direction.  | ""                          |
|                       | `offsetx`                      | Offset for the identified x-coordinate.    | config.offsetx_default      |
|                       | `offsety`                      | Offset for the identified y-coordinate.    | config.offsety_default      |
| `click`               | `txtToFind`                    | The element to find and click on.          | None(*Mandatory parameter*) |
|                       | `exactmatch`                   | Whether to perform an exact match for the element. | True                        |
|                       | `item_position`                | The position of the item to interact with. | 1                           |
|                       | `relative_word_in_x_direction` | A reference word in the x-axis direction.  | ""                          |
|                       | `relative_word_in_y_direction` | A reference word in the y-axis direction.  | ""                          |
|                       | `offsetx`                      | Offset for the identified x-coordinate.    | config.offsetx_default      |
|                       | `offsety`                      | Offset for the identified y-coordinate.    | config.offsety_default      |
| `click_img_object`    | `object`                       | The image object to interact with.         | None(*Mandatory parameter*) |
|                       | `item_position`                | The position of the item to interact with. | 1                           |
|                       | `relative_word_in_x_direction` | A reference word in the x-axis direction.  | ""                          |
|                       | `relative_word_in_y_direction` | A reference word in the y-axis direction.  | ""                          |
|                       | `offsetx`                      | Offset for the identified x-coordinate.    | config.offsetx_default      |
|                       | `offsety`                      | Offset for the identified y-coordinate.    | config.offsety_default      |
| `scroll_find_click`   | `txtToFind`                    | The element to find during scrolling.      | None(*Mandatory parameter*) |
|                       | `direction`                    | The direction of scrolling ("up", "down", etc.). | "down"                      |
|                       | `scrolls`                      | The number of times to scroll.             | 1                           |
|                       | `exactmatch`                   | Whether to perform an exact match for the element. | True                        |
|                       | `offsetx`                      | Offset for the identified x-coordinate.    | config.offsetx_default      |
|                       | `offsety`                      | Offset for the identified y-coordinate.    | config.offsety_default      |
| `scroll_find`         | `txtToFind`                    | The element to find during scrolling.      | None(*Mandatory parameter*) |
|                       | `direction`                    | The direction of scrolling ("up", "down", etc.). | "down"                      |
|                       | `scrolls`                      | The number of times to scroll.             | 1                           |
|                       | `exactmatch`                   | Whether to perform an exact match for the element. | True                        |
| `scroll`              | `direction`                    | The direction of scrolling ("up", "down", etc.). | "down"                      |
|                       | `scrolls`                      | The number of times to scroll.             | 1                           |
| `hover`               | `txtToFind`                    | The element to find and hover over.        | None(*Mandatory parameter*) |
|                       | `exactmatch`                   | Whether to perform an exact match for the element. | True                        |
|                       | `item_position`                | The position of the item to interact with. | 1                           |
|                       | `relative_word_in_x_direction` | A reference word in the x-axis direction.  | ""                          |
|                       | `relative_word_in_y_direction` | A reference word in the y-axis direction.  | ""                          |
|                       | `offsetx`                      | Offset for the identified x-coordinate.    | config.offsetx_default      |
|                       | `offsety`                      | Offset for the identified y-coordinate.    | config.offsety_default      |
| `hover_img_object`    | `object`                       | The image object to interact with.         | None(*Mandatory parameter*) |
|                       | `item_position`                | The position of the item to interact with. | 1                           |
|                       | `relative_word_in_x_direction` | A reference word in the x-axis direction.  | ""                          |
|                       | `relative_word_in_y_direction` | A reference word in the y-axis direction.  | ""                          |
|                       | `offsetx`                      | Offset for the identified x-coordinate.    | config.offsetx_default      |
|                       | `offsety`                      | Offset for the identified y-coordinate.    | config.offsety_default      |

- For more details on each function and their usage, refer to the respective function's docstring in the script.

## Created by: 

Jagadish Dabbiru [[Linked In](https://www.linkedin.com/in/jagadish-dabbiru)] 

For queries/support: jagadish.dabbiru@gmail.com


