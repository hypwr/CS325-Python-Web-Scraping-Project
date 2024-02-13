# CS325 Web Scraper - Project 1
## By Josh Erwin
### Quick Rundown
This python based webscraper utilizes the BeautifulSoup4 library to scrape a html file for an article's title and content. To use this program, you'll need two things: 
1. A ".txt" file containing URLs of specific webpages containing the article you want to scrape (with a single URL on each line of the file). These URLs must be from the https://www.nbcnews.com/ website.
2. A python environment matching that of the one in the requirements.yml file.

  I chose business and economic based articles for this scraper, but it should work with most articles on the website. If used with another website, it most likely won't work correctly. To make things easy, make sure the URL file is in the same folder as the current working directory; Otherwise when the program asks for your URL file, you can specify the file's direct path to be 100% sure it will use and find the correct file. If the program cannot find the URL file, it will throw an error. Once a correct URL file is inputted, the file's URLs will be read one by one and scrapped for their content. New files will be created in the current working directory named the title of each file's respective article. If the file name already exists, the program throw an error. The outputted text files will contain clean content of the article in one continuous line. 

If you need an example of how to format the .txt document, refer to list.txt in this repository, it shows the correct format.

### Detailed Instructions
1. Create a .txt file and place the URL's of the articles you wish to scrape in this file one by one. This means after pasting a URL, hit enter or newline. Furthermore, make sure these are from www.nbcnews.com and are preferably from the business section. Once you're done with this file, save it in a specific folder of your choosing.
2. Now download Scraper.py from the github repository. To do this you can click on this file in github and there should be a button near the top right of the screen with 3 dots, clicking on this should show the download button. For convience you can save this in the same folder you saved the URL file in.
3. Ensure your python environment is set up correctly. To do this you will need an environment manager such as anaconda or miniconda3 (what I used), but you can use any environment manager of your choosing. To make sure the program will work properly, download the requirements.yml file and import it as a new environment. Make sure you are then using the environment, for conda you can use the "conda activate 'environment_name'".
4. Use the 'dir' and 'cd' commands to navigate your working directory to the folder containing both the Scraper.py program and the URL file. If you have file explorer open, you can streamline the process by clicking on the top bar showing your navigation and copying the path. Then use the 'cd' command to transition the current working directory to the correct folder. Example: 'cd C:\Users\joshu\Documents\CS325\PROJECT'
5. Now you should be able to run the following command: 'python Scraper.py' and hit enter. You should be propted to input the file name of the URL file. Simply type in its exact name, including the .txt at the end. (Hit enter.) The program should then correctly run, however if an error occurs, a message will appear explaining what probably went wrong.
6. Your scraped files should now appear in the same folder as the program and the URL file. You can open them and see your content. If you want to make it more readable, you can copy and paste the article into a google docs or word file.
