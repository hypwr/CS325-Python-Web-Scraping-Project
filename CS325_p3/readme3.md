# Project 3
## By Josh Erwin
### Overview
Project 3 adds the addition of AI summarization through the Gemini API. This program asks the AI, "Please take the following article and summarize it in 50 words or less, here is the article: " followed by the article content. This question can be changed as one sees fit.
One major thing you must do to use the program is navigate to the 'module1' folder and open the GeminiAPI.py file. At the top of this file, you will see a variable called GOOGLE_API_KEY. This variable should be set equal to your Google API key. To get a Google API key for free (assuming your Google account does not already have one) go to "https://ai.google.dev/tutorials/get_started_web". Then scroll down until you see the box "Get an API key". Follow its directs and then once you have a key, copy and paste the key into the quoted area on the GOOGLE_API_KEY variable.
Please remember to update your requirements.yml as this was changed during this section of the project.
### API Guide
Here is a more indepth guide on how to use the API.
First, the key generation (follow the link above and you need a Google Account):
![image](https://github.com/hypwr/CS325-Python-Web-Scraping-Project/assets/147878375/9eca993a-56de-4521-9e8d-1418ed19e2c2)
Then click the button "Create API key":
![image](https://github.com/hypwr/CS325-Python-Web-Scraping-Project/assets/147878375/b6ff2ee7-fe9f-4797-857f-5349481c79c6)
IMPORTANT Keep these keys secure and copy the key:
![image](https://github.com/hypwr/CS325-Python-Web-Scraping-Project/assets/147878375/f9d0c959-1db0-492b-9bee-fa344ef52b6b)
Replace the highlighted section with your Google API Key:
![image](https://github.com/hypwr/CS325-Python-Web-Scraping-Project/assets/147878375/82e3caaa-7175-4fd8-ba7b-d3f4717aff8a)
Then using a class structure like the one below, you can call the API (in this case, using the geminiSummary function):
![image](https://github.com/hypwr/CS325-Python-Web-Scraping-Project/assets/147878375/1a1abca2-d451-4cc7-89f2-1cf5c36ea7bb)
Google has a very simple and easy library to use for it's Gemini API, so if you want to ask it something different, just change the message variable and it should output the response.
