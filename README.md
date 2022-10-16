# Scraping Hearts

![Scraping Hearts project banner](https://github.com/JonR45/Scraping-Hearts/blob/97d4e6d72975b545795f0c7a5026cacff97ab9cc/scraping_hearts_project_banner_2.png)

[Jupyter notebook (includes outputs, descriptions etc.)](https://github.com/JonR45/Scraping-Hearts/blob/main/scraping_hearts.ipynb)

[Code only (no outputs)](https://github.com/JonR45/Scraping-Hearts/blob/main/scraping_hearts.py)

This is a web scraping mini-project that involved using _Python_ to extract the fixtures and results from [Heart of Midlothian FC fixtures and results](https://www.heartsfc.co.uk/fixtures/first-team/fixtures-and-results), create a _pandas_ data frame and save this data frame as a _.csv_ file.

# Language and Libraries
**Language:** Python 3.9

**Libraries:** requests, BeauftifulSoup, pandas, numpy, datetime, parse, re
    
# Skills and Knowledge Required
* Python
* Web scraping
* Data cleaning
* Regular expressions
* Feature engineering
* Conditional logic
* Virtual environments
* Git and GitHub

# Aim of project
* The aim was to get the following information about each fixture into the data frame:
    * Date
    * Competition
    * Home or Away fixture (H or A)
    * Venue
    * Home team
    * Away team
    * Home team goals
    * Away team goals
    * Result (Win, loss or draw)

# Challenges 
**Extracting the data:** data had to be cleaned after/whilst extracting to make it readable and to obtain only the desired information.

**Feature engineering:** Features were created by using conditional logic that provided additional context to the already available data, would be useful for stroy telling with data, and would be useful if the project were to be advanced into the realms of machine learning. 

**Date:** the date had to be converted to a datetime object after being scraped. 

# Summary
* A script was created that scrapes the relevant data, places it into a data frame and exports it to a .csv.
* This project could be advanced by scraping previous seasons' data, extracting specific information about each game (shots, pass completion, possession % etc.) and further feature engineering to enable a deep analysis of Heart of Midlothian’s recent history. 
* This would also enable historic trends to be identified, and potentially a machine learning algorithm to be written that predicts results of future matches. 
