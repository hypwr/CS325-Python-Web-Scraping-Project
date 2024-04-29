# This module also uses the Single Responsibility Principle, allowing functions to remain focused and easily bug testable.
# This allowes the code to be more readable and more maintainable.
# This module's main purpose is to scrape the raw html and to output the cleaned data.
# This module also uses the Open-Closed Principle, allowing future scraper classes to be created to scrape for different
# elements in a webpage.
# This module's functions expect a few different things as inputs:
#  -  Scrape function: expects HTML content from the pull functions as a string, returns the cleaned data.
#  -  The outputDataFunctions simply expect a string containing the data to be stored,
#     and the name of the file they should be stored as (as strings).

from xml.etree import ElementTree as ET
from bs4 import BeautifulSoup
import os
from abc import ABC, abstractmethod

# This showcases the OCP, abstraction allows the class to be manipulated to fulfill other scraping duties.
class Scraper(ABC):
    @abstractmethod
    def Scrape(self, pageContent):
        raise NotImplementedError("Subscrapers must have a implimented scraping method.")

class h1Scraper(Scraper):
# Scrapes for h1 tag for the title. Scrapes for a specific div tag and then pulls the p tags from that div element and the respective text.
# Utilizes the beautiful soup libaries built in commands and finding/cleaning methods.
# Possible issue if quotes are found in the title, unsure of how to reproduce issue with one unrelated article.
### Follows the Single Responsiblity Princple:
### This functions sole role is to scrape the raw HTML content, making it clean.
    def Scrape(self, pageContent):
        try:
            soup = BeautifulSoup(pageContent, 'lxml')
            articleName = soup.find_all('h1')
            articleContent = soup.find('div',class_="article-body__content").findAll('p')

            title=articleName[0].text
            totalContent=''
            for content in articleContent:
                totalContent = totalContent+' '+content.text
# If you want to change the output data to be more readable in the text file, then change the line above to: totalContent = totalContent+content.text+'\n'
            outputData=[title,totalContent]
            return outputData
        except:
            print("Scraping Error")
            pass

class Output():
    def __init__(self):
        self.rel_directory=os.getcwd()

# Takes the cleaned article content and stores it in a file named (Article Title Here).txt
### Follows the Single Responsiblity Princple:
### This functions sole role is to output the clean data into a seperate file.
    def outputDataFile(self, outputData, filename)->None:
        try:
            f = open(self.rel_directory+"/Data/processed/"+str(filename),"x",encoding='utf-8')
            f.write(str(outputData))
            f.close()
        except:
            print("Unable to create file/file already exists.")
            pass

# Takes the dirty article content and stores it in a file named "RAW_(Article Title Here).txt"
### Follows the Single Responsiblity Princple:
### This functions sole role is to output the raw HTML as seperate files.
    def outputDataFileRAW(self, outputDataRAW, filename)->None:
        try:
            f = open(self.rel_directory+"/Data/raw/RAW_"+str(filename),"x",encoding='utf-8')
            f.write(str(outputDataRAW))
            f.close()
        except:
            print("Unable to create file/file already exists.")
            pass

# Takes the ChatGPT response content and stores it in a file named Summary_(Article Title Here).txt
### Follows the Single Responsiblity Princple:
### This functions sole role is to output the ChatGPT summary into a seperate file.
    def outputDataFileSUM(self, outputData, filename)->None:
        try:
            f = open(self.rel_directory+"/Data/gpt_summary/SUMMARY_"+str(filename),"x",encoding='utf-8')
            f.write(str(outputData))
            f.close()
        except:
            print("Unable to create file/file already exists.")
            pass

# This function takes an array of content that should be formatted in the method of title, article content, title, article content, etc. This then 
# is inputted into an xml tree which can be used to create an HTML file. Every article in the content array will have the header as it's title and
# the content listed in a <p> element following it.
    def summaryHTMLoutput(self, contentArray)->None:
        iterations = int(len(contentArray)/2)
        pos = 0
        root = ET.Element("html")

        head = ET.SubElement(root, "head")
        title = ET.SubElement(root, "title")
        title.text = "Summary HTML Page"
        body = ET.SubElement(root, "body")

        # This segment iterates through the array length/2 times. 
        for i in range(iterations):
            header = contentArray[pos]
            paragraph = contentArray[pos+1]
            pos+=2

            h1 = ET.SubElement(body, "h1")
            h1.text = header
            p = ET.SubElement(body, "p")
            p.text = paragraph

        # This attempts to create an HTML file for all the summaries to be contained.
        try:
            f = open(self.rel_directory+"/Data/gpt_summary/SUMMARY_HTML_ALL.html","x",encoding='utf-8')
            f.close()
        except:
            print("HTML file creation error/already exists.")


        with open(self.rel_directory+"/Data/gpt_summary/SUMMARY_HTML_ALL.html","wb") as f:
            tree = ET.ElementTree(root)
            tree.write(f, encoding="utf-8")
            f.close()
        
    