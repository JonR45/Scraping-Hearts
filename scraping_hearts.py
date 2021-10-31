#!/usr/bin/env python3
#  python3 web scraping mini project that scrapes the Heart of Midlothian FC fixtures and results to date for the 2021/2022 season
# creates a dataframe and exports the data to a .csv file

# import the packages
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from datetime import date
from dateutil.parser import parse
import re

print("\nInstalled packages.\nConnecting to base site...")

# define the url of the base site
base_site = "https://www.heartsfc.co.uk/fixtures/first-team/fixtures-and-results"

# send a request to the webpage
response = requests.get(base_site)
# check status of request
print(f"\nResponse code: {response.status_code}")

# get the HTML from the webpage
html = response.content

# create a BeautfulSoup object
soup = BeautifulSoup(html, 'html.parser')

print("\nCreating HTML file...")

# create an HTML file so we can inspect it
with open('Hearts_fixtures_and_results_HTML_parser.html', 'wb') as file:
    file.write(soup.prettify('utf-8'))

print("\nExtracting the fixtures and results...")

# locate the div that contains the info we'll extract
divs = soup.findAll("div", {"class": "fixtureItem"}, limit=None)

# extract date and convert into a datetime object
match_date = [div.find("h5").string for div in divs]
# use dateutil.parser parse to turn dates into datetime data type
date_formatted = [parse(i) for i in match_date]
date_formatted = [i.date() for i in date_formatted]

# make a list of competitions
competition = [div.find("small").string for div in divs]

# Home or Away fixture - list comprehension to extract a list of H's and A's and then strip to het just the 'H' or 'A'
home_away = [div.find("div", {"class": "fixtureItemClass"}).text.lstrip().rstrip() for div in divs]

# get venue
venue = [div.findAll("p")[2].string for div in divs]

# home and away teams
teams = [div.find_all("span") for div in divs]

home_team = []
away_team = []

for k, v in teams:
    home_team.append(k)
    away_team.append(v)

home_team = [i.string for i in home_team]
away_team = [i.string for i in away_team]

# get all the scores
scores = [div.find("div", {"class": "fixtureItemMeta"}).text.replace('FT:\n', '').rstrip().lstrip() for div in divs]
# remove the \n from the output
scores = [i.replace('\n', '') for i in scores]
# remove the blank sapces
scores = [i.replace(' ', '') for i in scores]

# create a dataframe
data = {'Date': match_date, 'Date_formatted': date_formatted, 'Competition': competition, 'Home_or_Away': home_away, 
        'Venue': venue, 'Home_team': home_team, 'Away_team': away_team, 'Score': scores}
df = pd.DataFrame(data)

# create Match day 1-39 so we can use it as an index
match_day =[]
for i in range(0, len(df['Date'])):
    match_day.append(f"Match_day_{i+1}")

# set match_day as index
df = df.set_axis(labels=match_day, axis=0)

# create a win/loss/draw feature - first need to create a home and away goals column
# create empty lists to be populated
Home_team_goals = []
Away_team_goals = []

# loop through scores and extract the first character in the string (e.g. 0 from '0-2') as the home goal and the 3rd character
# as the Away team's goals
for i in scores:
    if i[0] != 'K':
        Home_team_goals.append(i[0])
        Away_team_goals.append(i[2])
    elif i[0] == 'K':
        Home_team_goals.append(i)
        Away_team_goals.append(i)
        
# add the data to our dataframe and check the output
df['Home_team_goals'] = Home_team_goals
df['Away_team_goals'] = Away_team_goals

# convert home and away team goals from string to integer data type (so it can be used later for conditional logic); in order to
# do this we first need to tidy the data up a bit, so use a regex to identify the KO time pattern
reg_ex_pattern = re.compile(r'KO:\d{2}:\d{2}')

# replace the regex pattern with '0' and 'TBD' where appropriate
df['Home_team_goals'] = df['Home_team_goals'].str.replace(reg_ex_pattern, '0', regex=True)
df['Away_team_goals'] = df['Away_team_goals'].str.replace(reg_ex_pattern, '0', regex=True)
df['Score'] = df['Score'].str.replace(reg_ex_pattern, 'TBD', regex=True)

# convert Home team goals data from string to integer
df['Home_team_goals'] = df['Home_team_goals'].astype(int)
df['Away_team_goals'] = df['Away_team_goals'].astype(int)

# create a win/loss/draw column
df['Win/Loss/Draw'] = ""

# use conditional logic (numpy.select()) to populate the win/loss/draw column based on the home and away team goals columns
conditions = [
        (df['Home_team'] == 'Heart of Midlothian') & (df['Home_team_goals'] > df['Away_team_goals']),
        (df['Home_team'] == 'Heart of Midlothian') & (df['Home_team_goals'] < df['Away_team_goals']),
        (df['Home_team'] == 'Heart of Midlothian') & (df['Home_team_goals'] == df['Away_team_goals']),
        (df['Home_team'] != 'Heart of Midlothian') & (df['Home_team_goals'] > df['Away_team_goals']),
        (df['Home_team'] != 'Heart of Midlothian') & (df['Home_team_goals'] < df['Away_team_goals']),
        (df['Home_team'] != 'Heart of Midlothian') & (df['Home_team_goals'] == df['Away_team_goals'])
]
    
choices = ['W', 'L', 'D', 'L', 'W', 'D']
    
df['Win/Loss/Draw'] = np.select(conditions, choices)

# drop the score column as it is no longer necessary
df = df.drop('Score', axis=1)

# reorder the columns
columns = ['Date', 'Date_formatted', 'Competition', 'Home_or_Away', 'Venue',
       'Home_team', 'Away_team', 'Home_team_goals', 'Away_team_goals','Win/Loss/Draw',
       ]
df = df[columns]

# use np.select to change the 0 goals and 'D' values to 'TBD' for games that haven't been played yet
# the condition checks today's date vs the formatted date and if the date is after today's date then fill the relevant columsn with 'TBD'
condition = [df['Date_formatted'] >= date.today()]
choice = ['TBD']
    
df['Home_team_goals'] = np.select(condition, choice, default=df['Home_team_goals'])
df['Away_team_goals'] = np.select(condition, choice, default=df['Away_team_goals'])
df['Win/Loss/Draw'] = np.select(condition, choice, default=df['Win/Loss/Draw'])

print("\nCreating a .csv file")

# export the dataframe to csv
df.to_csv('hearts_fixtures_results.csv')

print("\nProgram complete. Hearts Hearts Glorious Hearts!")