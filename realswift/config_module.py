import json
import os


class MyPackageConfig:
    def __init__(self):
        self.chrome_browser_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
        self.edge_browser_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"
        self.offsetx = 0
        self.offsety = 0
        self.mousespeed = 0.2
        self.screenshot_path = 'target/screenshot.png'
        self.timeout = 60
        self.browser = 'chrome'
        self.output_path = 'target/output.jpg'
    def load_from_file(self, file_path):
        # Load configuration from a file (e.g., JSON)
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                config_data = json.load(file)
                print('properties loaded from config.json file')
                self.chrome_browser_path = config_data.get('chrome_browser_path', self.chrome_browser_path)
                self.offsetx = config_data.get('offsetx', self.offsetx)
                self.offsety = config_data.get('offsety', self.offsety)
                self.edge_browser_path = config_data.get('edge_browser_path', self.edge_browser_path)
                self.mousespeed = config_data.get('mousespeed', self.mousespeed)
                self.screenshot_path = config_data.get('screenshot_path', self.screenshot_path)
                self.timeout = config_data.get('timeout', self.timeout)
                self.browser = config_data.get('browser', self.browser)
                self.output_path = config_data.get('output_path', self.output_path)
# Usage example
# Create an instance of the configuration class
config = MyPackageConfig()
config.load_from_file('config.json')