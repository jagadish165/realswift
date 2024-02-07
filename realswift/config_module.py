import json
import os


class MyPackageConfig:
    def __init__(self):
        self.chrome_browser_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
        self.edge_browser_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
        self.offsetx_default = 0
        self.offsety_default = 0
        self.mousespeed = 0.2
        self.screenshots_folder = 'screenshots'
        self.img_objects_folder = 'img_objects'
        self.retries = 5
        self.browser = 'chrome'
        self.options = '--start-maximized'
    def load_from_file(self, file_path):
        # Load configuration from a file (e.g., JSON)
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                config_data = json.load(file)
                print('properties loaded from config.json file')
                self.chrome_browser_path = config_data.get('chrome_browser_path', self.chrome_browser_path)
                self.offsetx_default = config_data.get('offsetx_default', self.offsetx_default)
                self.offsety_default = config_data.get('offsety_default', self.offsety_default)
                self.edge_browser_path = config_data.get('edge_browser_path', self.edge_browser_path)
                self.mousespeed = config_data.get('mousespeed', self.mousespeed)
                self.screenshots_folder = config_data.get('screenshots_folder', self.screenshots_folder)
                self.img_objects_folder = config_data.get('img_objects_folder', self.img_objects_folder)
                self.retries = config_data.get('retries', self.retries)
                self.browser = config_data.get('browser', self.browser)
                self.options = config_data.get('options', self.options)
        self.screenshots_path = self.screenshots_folder + '/screenshot.png'
        self.output_path = self.screenshots_folder + '/identified_text_screenshot.png'
        self.element_ss_path = self.screenshots_folder + '/element_screenshot.png'

# Usage example
# Create an instance of the configuration class
config = MyPackageConfig()
config.load_from_file('config.json')
