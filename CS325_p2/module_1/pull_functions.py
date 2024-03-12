# This module uses the Single Resonsibility Principle, allowing functions to remain focused and easily bug testable.
# This allowes the code to be more readable and more maintainable.
# This module's main purpose is to pull the URLs and raw HTML from the webpage, storing them in their own files.
# This module's functions expect a file containing the URLs as input, it will then return those URLs in the file and give them
# to the next function. This next function returns the raw HTML page data for that URL.

import requests

class Pull():
# Function to Open File and Store URL's into an array
# Must specify complete file path or have the current working directory be where the file is located
### Follows the Single Responsiblity Princple:
### This functions sole role is to open the file and return an array of the file contents.
    def Pull_URLs(self, filename):
        f = filename
        try:
            openFile = open(f,"r")
            url = openFile.read().splitlines()
            openFile.close()
            return url
        except:
            print("Unable to find or read file.")
            pass

# Pulls the raw html from a url of a webpage
### Follows the Single Responsiblity Princple:
### This functions sole role is to pull the raw HTML content and return it.
    def Pull_HTML(self, url):
        try:
            pageContent=requests.get(url).text
            return pageContent
        except:
            print("Unable to pull page content or URL was invalid.")
            pass