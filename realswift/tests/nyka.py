from realswift.browser_utils import init_browser
from realswift.actions import *

init_browser("https://www.nykaa.com")
hover("Mom & Baby")
hover("Bath & Body")
click("Hand Wash")
scroll("down",5,"Price")
click("Price")
scroll("down",5)
click("500",exactmatch=False)
#time.sleep(2)
scroll("down",4,"Discount","click")
scroll("down",5,"30% And","click",False)
scroll("down",4)
click("Bath & Body",exactmatch=False,item=2)