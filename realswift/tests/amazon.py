##Scenario: Open Amazon.in Search for Apple watch, scroll down to find Apple Watch Series 9, Check Bank offer 2, Click Back

from realswift.actions import *
from realswift.browser_utils import open_browser

open_browser("https://www.amazon.in")
click("Search Amazon.in")
type_keys("apple watch")
press_keys("enter")
scroll_find_click("Apple Watch Series 9","down",10,exactmatch=False)
click("Bank offer")
click("See details",exactmatch=False,item_position=2,offsety=3)
click("Offer 2")
scroll("down",4)
click("Back")
click("Bank offer")
scroll_find_click("Buy Now",scrolls=4)
click("create your amazon account")