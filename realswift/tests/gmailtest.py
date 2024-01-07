from realswift.browser_utils import init_browser
from realswift.actions import *

init_browser("https://www.google.com/gmail/about/")
click("Create an account")
click("Enter your name")
recapture()
type("John","First name")
type( "Dheere","Last name (Optional)")
click("Next")
type("11","Day")
click("Month")
click("April")
type( "1990","Year")
click("Gender")
click("Male")
click("Next")