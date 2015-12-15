This project is for Data Structures (except I decided to take this project to the next level). 
This project implements the following technologies: 
Front-end: 
React
D3.js (Data Visualization library) 

Back-end: 
Django 
Self-made unofficial Buzzfeed API (created via data scraping) 
Indico API 
Joblib for Parallelization 

The data structures used are: 
-Linked List
-Hashmap

Abstract & Imports:

As the world become increasingly uploaded into the web, it is important to 
extract data from various online resources to study political and socioeconomic trends. Empirical data, especially regarding the opinions of a population between the ages of 12 and 30, can be collected from the web from sources such as Facebook and Youtube. For example, the question: “To what extent has Islamaphobia spread throughout social media in youth?” could target Twitter tweets with the word “Islam,” returning the comments as a JSON. Twitter’s very detailed API enables social researchers to download the data set instead of having to go on Twitter, type in “Islam,” and copy paste the first n or so tweets. Buzzfeed, as one of the world’s leading entertainment and media companies, reflect the ideologies of its target customer, young adults between 13-23, in areas from fashion to world politics to social activism. However, as of now, there is no API to make use of Buzzfeed’s dataset (and very little on github). 

The unofficial Buzzfeed API has the following endpoints:
GET: /search
GET: /<post>/comments

I used the API to create a website where users can input in a word and that word would be searched in the Buzzfeed API. The comments of each blog post that is extracted using the GET /search would then be parsed through the Indico API to get its sentiment and the words with the highest frequency in the comments of those posts. 

Run the website by cding into the directory and then running "python manage.py runserver", and then go to 127.0.0.1:8000/ to start. Then, you can query a word and see how that word is portrayed in buzzfeed, as well as the key words associated with that query word. 

What to do: 
-Modularize data scraping. 