from bs4 import BeautifulSoup
import requests

# Function to Open File and Store URL's into an array
# Must specify complete file path or have the current working directory be where the file is located
def Pull_URLs(filename):
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
def Pull_HTML(url):
    try:
        pageContent=requests.get(url).text
        return pageContent
    except:
        print("Unable to pull page content or URL was invalid.")
        pass

# OLD: Scrapes the html for an h1 tag including the title, then scrapes it for a specific div class containing the content needed.
# This div content is placed in another BeautifulSoup object and scraped for p tags containing text.
# For whatever reason the div tag would provide the correct data, but periods wouldn't have spaces after them.
# On one test article, instead of having one space after a sentence, it had 2 spaces after every one?
# ----------------------------------------------------------------------------------------------------------------
# FIXED: Scrapes for h1 tag for the title. Scrapes for a specific div tag and then pulls the p tags from that div element and the respective text.
# Utilizes the beautiful soup libaries built in commands and finding/cleaning methods.
# Possible issue if quotes are found in the title, unsure of how to reproduce issue with one unrelated article.
def Scrape(pageContent):
    try:
        soup = BeautifulSoup(pageContent, 'lxml')
        articleName = soup.find_all('h1')
        articleContent = soup.find('div',class_="article-body__content").findAll('p')

        title=articleName[0].text
        totalContent=''
        for content in articleContent:
            totalContent = totalContent+' '+content.text
        
        outputData=[title,totalContent]
        return outputData
    except:
        print("Scraping Error")
        pass

# Takes the cleaned article content and stores it in a file named (Article Title Here).txt
def outputDataFile(outputData, filename)->None:
    try:
        f = open(str(filename),"x",encoding='utf-8')
        f.write(str(outputData))
        f.close()
    except:
        print("Unable to create file/file already exists.")
        pass

# Uses all the previously defined functions to streamline the process, it takes the URL file, pulls the HTML, scrapes the HTML,
# names the file, and places the content into the file. The files should be outputted into the current working directory the program is in.
# The program does take a bit of time as it has to pull the data from each website.
def articleScraper(urlFile) -> None:
    try:
        urls=Pull_URLs(urlFile)
        for url in urls:
            rawHTML=Pull_HTML(url)
            outputData=Scrape(rawHTML)
            filename=str(outputData[0])+".txt"
            output=outputData[1]
            outputDataFile(output, filename)
        print("Article content has been stored!")
    except:
        print("An error has occured, unable to scrape every document.")
        pass

# articleScraper("list.txt")
# Asks for the file name/path and then calls articleScraper
def main() -> None:
    print("Input the name of the file or its path containing the URLs:")
    urlFile=input()
    articleScraper(urlFile)

# Run main.
main()