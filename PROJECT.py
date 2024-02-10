from bs4 import BeautifulSoup
import requests

# Function to Open File and Store URL's into an array
# Must specify complete file path or have the current working directory be where the file is located
def Pull_URLs(filename):
    f = filename
    openFile = open(f,"r")
    url = openFile.read().splitlines()
    openFile.close()
    return url

# Pull the html from a url of a webpage
def Pull_HTML(url):
    pageContent=requests.get(url).text
    return pageContent

# OLD: Scrapes the html for an h1 tag including the title, then scrapes it for a specific div class containing the content needed.
# This div content is placed in another BeautifulSoup object and scraped for p tags containing text.
# For whatever reason the div tag would provide the correct data, but periods wouldn't have spaces after them.
# On one test article, instead of having one space after a sentence, it had 2 spaces after every one?
# ----------------------------------------------------------------------------------------------------------------
# FIXED: Scrapes for h1 tag for the title. Scrapes for a specific div tag and then pulls the p tags from that div element and the respective text.
def Scrape(pageContent):
    soup = BeautifulSoup(pageContent, 'lxml')
    articleName = soup.find_all('h1')
    articleContent = soup.find('div',class_="article-body__content").findAll('p')

    title=articleName[0].text
    totalContent=''
    for content in articleContent:
        totalContent = totalContent+' '+content.text
    
    outputData=[title,totalContent]
    return outputData

def outputDataFile(outputData, filename)->None:

    f = open(str(filename),"x")
    f.write(str(outputData))
    f.close()

def articleScraper(urlFile) -> None:
    urls=Pull_URLs(urlFile)
    for url in urls:
        rawHTML=Pull_HTML(url)
        outputData=Scrape(rawHTML)
        fileName=str(outputData[0])+".txt"
        output=outputData[1]
        outputDataFile(output, filename)
        print("Done!")

articleScraper("C:/Users/joshu/Documents/CS325/PROJECT/list.txt")