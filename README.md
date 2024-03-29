# CS325 Web Scraper - Project 3
## By Josh Erwin
### Switch to the main branch to see project 1.
### Switch to the p2 branch to see project 2.
### Project 3 is inside the CS325_p3 folder.

## NEW TO PROJECT 3
Project 3 adds the addition of AI summarization through the Gemini API. This program asks the AI, "Please take the following article and summarize it in 50 words or less, here is the article: " followed by the article content. This question can be changed as one sees fit.
One major thing you must do to use the program is navigate to the 'module1' folder and open the GeminiAPI.py file. At the top of this file, you will see a variable called GOOGLE_API_KEY. This variable should be set equal to your Google API key. To get a Google API key for free (assuming your Google account does not already have one) go to "https://ai.google.dev/tutorials/get_started_web". Then scroll down until you see the box "Get an API key". Follow its directs and then once you have a key, copy and paste the key into the quoted area on the GOOGLE_API_KEY variable.
Please remember to update your requirements.yml as this was changed during this section of the project.

## NEW TO PROJECT 2
You must now use an argument when using the program. For example, python run.py list.txt, would be the code to run to have the program work on list.txt. However, one major change is that the current working directory of the program must be inside the project folder.

### Quick Rundown
This python based webscraper utilizes the BeautifulSoup4 library to scrape a html file for an article's title and content. It also uses google's Gemini AI API to generate a summary of the article. To use this program, you'll need two things: 
1. A ".txt" file containing URLs of specific webpages containing the article you want to scrape (with a single URL on each line of the file). These URLs must be from the https://www.nbcnews.com/ website.
2. A python environment matching that of the one in the requirements.yml file.

  I chose business and economic based articles for this scraper, but it should work with most articles on the website. If used with another website, it most likely won't work correctly. To make things easy, make sure the URL file is in the same folder as the current working directory; Otherwise when the program asks for your URL file, you can specify the file's direct path to be 100% sure it will use and find the correct file. If the program cannot find the URL file, it will throw an error. Once a correct URL file is inputted, the file's URLs will be read one by one and scrapped for their content. New files will be created in the current working directory named the title of each file's respective article. If the file name already exists, the program throw an error. The outputted text files will contain clean content of the article in one continuous line. 

If you need an example of how to format the .txt document, refer to list.txt in this repository, it shows the correct format. The sample files of list.txt's outputs are avalible as their article names.

### How It Works
This program, as mentioned above, uses the BeautifulSoup4 library as well as lxml and requests libraries to perform the scraping. First, the PULL_URLs() function opens the URL text file, reads it line by line, closes the file, and returns an array containing the URL's. The next function, PULL_HTML(), uses requests to go to each page and rip the HTML from the page. However, this HTML is messy and contains a lot of unused data. So the HTML of the page is returned and then passed into the Scrape() function. This function creates a BeautifulSoup object, named soup for simplicity, that is intitalized with the HTML we ripped previously and the parser method; for this program, the parser method is 'lxml'. 

The Scrape() function then searches for any 'h1' tags in the HTML. For nbcnews.com, the only 'h1' tag to appear on the articles I checked was the title, so the article name is stored for file naming. The rest of the content of the article is under a specific 'div' tag, the class of "article-body__content". We then scrape this part of the HTML for 'p' tags containing the body of the article. The total content of the article is combined into one string, and then both the title and the content are returned by this function. Finally, outputDataFile() opens a new file titled the title of the article, and places the content into it (using utf-8 encoding for special characters). This file is then close and should appear in your current working directory. 

Lastly, the articleScraper() function compacts all of the previously mentioned functions into one nice function that calls all the previous ones in the correct order for each article. Every function has basic error reporting that should give the user an idea as to what went wrong and to prevent the program from crashing on error.

NEW: Now it uses classes from seperate modules to have more organized code, the major change in functionality however is that geminiSummary() is called and a 3rd document is outputed containing a close to 50 word summary on the article.

### Detailed Instructions
1. Create a .txt file and place the URL's of the articles you wish to scrape in this file one by one. This means after pasting a URL, hit enter or newline. Furthermore, make sure these are from www.nbcnews.com and are preferably from the business section. Once you're done with this file, save it in a specific folder of your choosing.
2. Now download Scraper.py from the github repository. To do this you can click on this file in github and there should be a button near the top right of the screen with 3 dots, clicking on this should show the download button. For convience you can save this in the same folder you saved the URL file in.
3. Ensure your python environment is set up correctly. To do this you will need an environment manager such as anaconda or miniconda3 (what I used), but you can use any environment manager of your choosing. To make sure the program will work properly, download the requirements.yml file and import it as a new environment, for anaconda you can you use the "conda create --name 'environment_name' --file requirements.yml". Lastly, make sure you are using the environment; for anaconda you can use the "conda activate 'environment_name'".
4. Open command prompt, (search 'CMD' on windows), or use whatever command line interface you choose. Use the 'dir' and 'cd' commands to navigate your working directory to the folder containing both the Scraper.py program and the URL file. If you have file explorer open, you can streamline the process by clicking on the top bar showing your navigation and copying the path. Then use the 'cd' command to transition the current working directory to the correct folder. Example: 'cd C:\Users\joshu\Documents\CS325\PROJECT'
5. Now you should be able to run the following command: 'python Scraper.py' and hit enter. You should be propted to input the file name of the URL file. Simply type in its exact name, including the .txt at the end. (Hit enter.) The program should then correctly run, however if an error occurs, a message will appear explaining what probably went wrong.
6. Your scraped files should now appear in the same folder as the program and the URL file. You can open them and see your content. If you want to make it more readable, you can copy and paste the article into a google docs or word file.
