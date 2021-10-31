# Scraping Hearts

This is a quick web scraping project that involved using _Python_ to extract specific data (the fixtures and results) from a website [Heart of Midlothian FC fixtures and results](https://www.heartsfc.co.uk/fixtures/first-team/fixtures-and-results), create a _pandas_ data frame and save this data frame as a _.csv_ file.

### Language and Packages used
**Language:** Python 3.9

**Packages used:** requests, BeauftifulSoup, pandas, numpy, datetime, parse, re
    
### Skills and Knowledge Required
* Python
* Web scraping
* Data cleaning
* Regular expressions
* Feature engineering
* Conditional logic
* Virtual environments
* Git and GitHub

### Aim of project
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
* **Extracting the data:** data had to be cleaned after/whilst extracting to make it readable and to obtain only the desired information.
* **Feature engineering:** Additional variables were created by using conditional logic; this provided information (a win, loss or draw) that is crucial to understanding the story during data anlysis.
* **Date:** the date had to be converted to a datetime object after being scraped. 

# Summary
* A script was created that scrapes the relevant data and places it into a data frame.
* This project could be advanced by scraping previous season’s data, extracting specific information about each game (shots, pass completion, possession % etc.) 

![image](https://user-images.githubusercontent.com/65425846/139596456-af7c288f-1935-4c3e-85de-5297588b44da.png)
