from realswift.browser_utils import open_browser
from realswift.actions import *

open_browser("https://www.nykaa.com")
hover("Mom & Baby")
hover("Bath & Body")
click("Hand Wash")
scroll_find_click("Price","down",5)
scroll_find_click("500","down",5,False)
scroll_find_click("Discount","down",5)
scroll_find_click("30% And","down",5,False)
scroll_find("Bath & Body","down",5,False)
click("Bath & Body",exactmatch=False,item_position=2)
