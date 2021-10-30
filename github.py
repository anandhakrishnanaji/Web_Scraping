from bs4 import BeautifulSoup
import requests
import pandas as pd

keyword = 'hacktoberfest'
language = "Python"

BASE_URL = 'https://github.com/search?o=desc&q={}+language%3A{}&s=&type=Repositories'.format(keyword,language)

r = requests.get(BASE_URL)
soup =  BeautifulSoup(r.text, 'html.parser')
table = soup.find_all('li', class_='repo-list-item hx_hit-repo d-flex flex-justify-start py-4 public source')

# description
#print(table[0].find('p', class_='mb-1').text)

#tags
#print('https://www.github.com' + table[0].find_all('a', attrs={'data-ga-click':'Topic, search results'}, href=True)[1]['href'])

#stars
#print(table[0].find('a', class_='Link--muted', recursive="False").text.strip())

#Author and repo name
#title = table[0].find('a', class_='v-align-middle').text
#Author = title.split('/')[0]
#Repo = title.split('/')[1]

#print(len(table))

description = []
tags = []
starts = []
author = []
repo = []

for row in table:
    description.append(row.find('p', class_='mb-1').text)
    title = row.find('a', class_='v-align-middle').text
    author.append(title.split('/')[0])
    repo.append(title.split('/')[1])
    starts.append(row.find('a', class_='Link--muted', recursive="False").text.strip())
    table_tags = table[0].find_all('a', attrs={'data-ga-click':'Topic, search results'}, href=True)
    tags_list =[]
    for tag in table_tags:
        tags_list.append(tag['href'])
    tags.append([i.replace('/topics/', '') for i in tags_list])

df = pd.DataFrame({
    'author':author,
    'repo':repo,
    'description':description,
    'tags':tags,
    'starts':starts
})

print(df)
df.to_csv('{}_github_repo_data.csv'.format(keyword), index=False)

#https://github.com/search?o=desc&q=hacktoberfest+%22scraping%22+language%3APython&s=&type=Repositories