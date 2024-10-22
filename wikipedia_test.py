import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import requests

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#THIS IS A CLOSE COPY OF THE CODE WRITTEN BY 'ALEX THE ANALYST' AND 
#FOLLOWS THE YOUTUBE TUTORIAL HERE: https://www.youtube.com/watch?v=8dTpNajxaH0
#FULL CODE CAN BE FOUND HERE https://github.com/AlexTheAnalyst/PythonYouTubeSeries
#I HAVE WRITTEN ELEMENTS OF THE CODE FOR EASE OF READING, AND ADDED ADDITIONAL COMMENTS 
#5/3/2024
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%




#Import URL
url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
#Pull HTML
page= requests.get(url)
#PARSE
soup=BeautifulSoup(page.text, 'html.parser')

#PULL ALL TABLES
all_tables = soup.find_all('table'[:])

#COUNT OUTPUTS
print('There are ', len(all_tables[1]), 'tables on this url: ', url)

#SELECT TABLE OF INTEREST.
# We have selected the second table (as Python's indexing is 0,1,2,3.....) 
#by typing all_tables[1]. The first table is actually the box that reads
# "This article needs additional citations".  To change to a different table change to 
#all_tables[n]
selected_table=all_tables[1]
print('The Table type is: ', type(selected_table))

#OBTAIN TABLE HEADERS
#See whats contained by printing the values
header_vals=selected_table.find_all('th') #th stands for 'table header' in HTML
print(header_vals)

#STRIP UNNECESSARY VALUES FROM HEADER
# This is a "Generator object" in Python, it says, 
#for each 'thing' in header_vals, that we'll call 'title', 
#remove the whitespace from title and put these new items in an array. 
#Read this for more info: https://www.programiz.com/python-programming/generator
#Have a look at what 'title for title in header_vals' looks like before and after stripping the
#whitespace
header_vals=[title.text.strip() for title in header_vals]
print(header_vals)


#FIND WHERE DATA IS STORED IN THE TABLE
#IN THIS CASE IT'S STORED IN TABLE ROW (TR)
#IT MAY ALSO BE FOUBND IN TABLE DATA (TD)
#This is telling Python to go through each table row, and strip away the
#whitespace from each row, and save the data. 
print([data.text.strip() for data in selected_table.find_all('tr')]) #tr stands for 'table row' in HTML


# SAVE INFO TO DATAFRAME
#This sets up an empty dataframe for us to populate. We initialise it with columns
#the same as the header of our table
df= pd.DataFrame(columns=header_vals)
column_data=selected_table.find_all('tr')
#ignore first row of table as it's the header

#For each row within the data, read the data, strip the whitespace, and 
#append it to the dataframe 
for row in column_data[1:]:
    row_data=row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    print(individual_row_data)
    length=len(df)
    #append rows to df with location in table matching location in df
    df.loc[length] = individual_row_data


#CHECK LENGTH OF DATAFRAME
#Is it what we expect, compared to the table online?
print('len df', len(df))

#SAVE DATAFRAME AS A CSV
df.to_csv(r'Q:\Oflog\Council Failure\Web_scraping\la-web-scraping\wikipedia_test.csv', index = False)










