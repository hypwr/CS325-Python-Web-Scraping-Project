####################################################################################
# IT IS REQUIRED THAT THE CURRENT WORKING DIRECTORY IS THE SAME FOLDER AS THIS ONE #
####################################################################################

from bs4 import BeautifulSoup
import requests
import argparse
from module_1 import pull_functions as PF
from module_2 import scrape_output as SO

# This parser function takes the input argument of the file's name, the url file must be stored in the same folder as the CWD and run.py.
def parser():
    parser=argparse.ArgumentParser()
    parser.add_argument(help="filename.txt",dest="file_name",type=str)
    args = parser.parse_args()
    fileName=args.file_name
    return fileName
    
# Uses all the previously defined functions to streamline the process, it takes the URL file, pulls the HTML, scrapes the HTML,
# names the file, and places the content into the file. The files should be outputted into the current working directory the program is in.
# The program does take a bit of time as it has to pull the data from each website.
# This function is essentially the main function, but for cleanliness, readablility, and testability, it is stored in a seperate function.
def articleScraper(urlFile) -> None:
    try:
        pullOBJ=PF.Pull()
        scrapeOBJ=SO.h1Scraper()
        outputOBJ=SO.Output()
        urls=pullOBJ.Pull_URLs(urlFile)
        for url in urls:
            rawHTML=pullOBJ.Pull_HTML(url)
            outputData=scrapeOBJ.Scrape(rawHTML)
            filename=str(outputData[0])+".txt"
            output=outputData[1]
            outputOBJ.outputDataFileRAW(str(rawHTML),filename)
            outputOBJ.outputDataFile(output, filename)
        print("Article content has been stored!")
    except:
        print("An error has occured, unable to scrape every document.")
        pass

# articleScraper("list.txt")
# accepts an argument containing the urlFile, then calls articleScraper
def main() -> None:
    urlFile=parser()
    articleScraper(urlFile)

# Run main.
main()