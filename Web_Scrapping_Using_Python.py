#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Web Scraping Job Vacancies


# In[ ]:


## Introduction

In this project, I'vel built a web scraper to extract job listings from a Fake Python Jobs search platform https://realpython.github.io/fake-jobs/. It’s an example site with fake job postings that we can freely scrape to train our skills. This web scraper will parse the HTML on the site to pick out the relevant information and filter that content for specific words.

We'll extract job titles, companies, and locations.

Here are the main steps we'll follow in this project:

1. Setup our development environment
    -- To complete this project, I've used Jupyter Notebook on Coursera's cloud workspace.

2. Understand the basics of web scraping

3. Analyze the website structure of our job search platform
4. Write the Python code to extract job data from our job search platform
5. Save the data to a CSV file
6. Test our web scraper and refine our code as needed


##


# In[ ]:


# Task 1 – Import required libraries

import csv
import datetime
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import csv 


# In[ ]:


# Task 2 – Generating a URL

URL = 'https://realpython.github.io/fake-jobs/'


# Set the headers for the HTTP request.

HEADERS = ({"userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36", 'Accept-Language': 'en=US,en;q=0.5'})


# Send an HTTP request to the URL and retrieve the HTML code of the search results page

page = requests.get(URL, headers=HEADERS)

time.sleep(5)
if page.status_code != 200:
    print("Error page")

page.status_code


# In[ ]:


# Task 3 – Parse the HTML code using BeautifulSoup

soup = BeautifulSoup(page.content, "html.parser")
soup


# select the HTML elements that contain the job postings

jobs = soup.find_all('section', class_='section')

jobs


# In[ ]:


# Task 4 - For each posting, extract the job posting information

jobs_data = []

for job in jobs:
    title = job.find("h2", class_="title").text.strip() 
    company = job.find("h3", class_="company").text.strip()
    location = job.find("p", class_="location").text.strip()
    
    print(title)
    print(company)
    print(location)
    
    print()

    job_data = [title, company, location]
    jobs_data.append(job_data)


# In[ ]:


# Task 5 - Write the job posting information to a CSV file

with open('jobs.csv', 'w', newline='') as file:
  writer = csv.writer(file)
  writer.writerow(['Title', 'Company', 'Location']) # write header
  writer.writerows(jobs_data)

df = pd.read_csv('jobs.csv')
print(df)
print('Data extracted successfully!')


# In[ ]:


# To filter for only specific jobs - Passing the function to a Beautiful Soup Method

python_jobs = soup.find_all("h2", string=lambda text: "python" in text.lower())

python_jobs


# In[ ]:


# To extract links to apply for a job

for job in python_jobs:
     # -- snip --
    links = soup.find_all("a")
    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}\n")


# In[ ]:


# To fetch the URL of just the second link for each job card

for job in python_jobs:
     # -- snip --
    link_url = soup.find_all("a")[1]["href"]
    print(f"Apply here: {link_url}\n")

