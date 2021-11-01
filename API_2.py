#import necessary modules, libraries, and packages
#Utilizing API chosen at random from IMDB website;
#exact object of this particular API is muddled and unclear
#Analyst will be treating as a call response with arbitrary data
#for testing purposes, containing some
#international shows and films from all eras 
import ast
import http.client
import pandas as pd
import random
import inspect
import wikipedia
import os
from dotenv import load_dotenv
load_dotenv()
#Utilize API to connect to the IMDB server
conn = http.client.HTTPSConnection('imdb8.p.rapidapi.com')
#Private keys
headers = {
    'x-rapidapi-host': os.environ.get("x-rapidapi-host"),
    'x-rapidapi-key': os.environ.get("x-rapidapi-key")
    }
#Get request
conn.request("GET", "/actors/get-all-filmography?nconst=nm0001667", headers=headers)
#Obtain the response raw data
res = conn.getresponse()
#Process data by passing to read function
data = res.read()
#Convert to readable form: convert bit object to string object
top = data.decode('utf-8')
#Evaluate string object: literally interpret to get dictionary
top = ast.literal_eval(top)
#Establish that the view is all columns
pd.set_option('display.max_columns', None)
#Utilized most pertinent portion of nested containers;
#established dataframe by utilizing dictionary
df = pd.DataFrame(top['filmography'])
#Update index name for tractability
df.index = df.index.rename('Original')
#Pass indexes to a to list to utilize the random.choice() function
Index_List = df.index.to_list()
#Pseudo-randomly choose index from list
rando = random.choice(Index_List)
#Use pseudo-randomly chosen index as a corresponder for "Title" series;
#Obtain pseudo-randomly chosen film from API response data
sol = df.iloc[rando]['title']
#Pass data (as an argument) to the wikipedia.page() function and .title() function
#Obtain proxy proof of existence of the film's Wikipedia page
#In the future, may scale back by a step to achieve this more concisely;
#or push forward and add if/else block 
#to create a page if there isn't one
print("The movie/show is: " + sol)
try:
    print(wikipedia.page(sol).title + " does have a Wikipedia page")
except Exception:
    print("This movie/show does not have a Wikipedia page")
input("Press enter to exit")

