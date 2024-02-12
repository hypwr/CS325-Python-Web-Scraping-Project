# CS325 Web Scraper - Project 1
## By Josh Erwin
This python based webscraper utilizes the BeautifulSoup4 library to scrape a html file for an article's title and content. To use this program, you'll need two things: 
1. A ".txt" file containing URLs of specific webpages containing the article you want to scrape (with a single URL on each line of the file).
2. These URLs must be from the https://www.nbcnews.com/ website.

  I chose business and economic based articles for this scraper, but it should work with most articles on the website. If used with another website, it most likely won't work correctly. To make things easy, make sure the URL file is in the same folder as the current working directory; Otherwise when the program asks for your URL file, you can specify the file's direct path to be 100% sure it will use and find the correct file. If the program cannot find the URL file, it will crash. Once a correct URL file is inputted, the file's URLs will be read one by one and scrapped for their content. New files will be created in the current working directory named the title of each file's respective article. If the file name already exists, the program will crash. The outputted text files will contain clean content of the article in one continuous line. 

  URL File Example - list.txt
https://www.nbcnews.com/news/us-news/tesla-recalls-22-million-electric-vehicles-us-concerns-warning-lights-rcna136910
https://www.nbcnews.com/tech/crypto/three-people-indicted-400-million-ftx-hack-conspiracy-rcna136976
https://www.nbcnews.com/business/economy/higher-tax-filing-costs-take-bite-refund-rcna135161
https://www.nbcnews.com/news/us-news/boeing-finds-problems-fuselages-737-jets-latest-manufacturing-issue-rcna137233
https://www.nbcnews.com/business/business-news/ups-cutting-12000-jobs-citing-softer-demand-higher-union-labor-costs-rcna136350
