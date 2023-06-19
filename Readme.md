# Web Scraping Using Python (BeautifulSoup)


## Introduction: What is Web Scraping?
Web scraping is a technique to automatically access and extract large amounts of information from a website, which can save a huge amount of time and effort. <br>

In this project we are going to use amazon product (ps5) search result link as the source of our raw data [link](https://www.amazon.in/s?k=playstation+5&sprefix=pla%2Caps%2C464&ref=nb_sb_ss_ts-doa-p_1_3).


## Prerequisites
1. Python 3.6+
2. install BeautifulSoup ```pip install beautifulsoup4```
3. install Requests ```pip install requests```
4. install Pandas ```pip install pandas```
5. the user-agent of your browser. To get the user-agent, just search for "my user agent" on Google and copy the user-agent string.
6. product search url from amazon


## Process of Web Scraping
1. Importing the required libraries
2. Specifying the URL containing the dataset and passing it to `requests.get()` to get the HTML content of the page.
3. Using BeautifulSoup to parse the HTML content
4. Extracting the required information from the data
5. Saving the pandas dataframe as a CSV file called `Amazon Data.csv`


## Project Specifications
1. It contains a python file `scraper.py` which contains the rough codes to be used in the final notebook file.
2. It contains a jupyter notebook file `Amazon Web Scraper.ipynb` which contains the final codes to be used in the project.
    * function to Extract Product Title
    * function to Extract Product Price
    * function to Extract Product Rating
    * function to Extract Number of User Reviews
    * function to Extract Product Availability
3. It contains a csv file `Amazon Data.csv` which contains the final data extracted from the website.


## About me
I am Mohd Mohitur Rahaman, and currently, I am pursuing MCA from KIIT University, Bhubaneswar. Talking about my previous educational background, I did my BSC in Mathematics at Malda College.

- [Mohd Mohitur Rahaman](https://linktr.ee/mohitur)


## Feedback
If you have any feedback, you can make the changes and create a pull request or, please reach out to me at [here](mohitur669@gmail.com) or [LinkedIn](https://www.linkedin.com/in/mohitur02).