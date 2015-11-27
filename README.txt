This project is for Data Structures (except I decided to take this project to the next level). 
This project implements the following technologies: 
Front-end: 
React
D3.js (Data Visualization library) 

Back-end: 
Django 
Self-made unofficial Buzzfeed API (created via data scraping) 
Indico API 

The data structures used are: 
-Linked List
-Hashmap

Abstract & Importa

Goalsf or today: 
-Get the JSON from the back-end in a parseable way for the d3.js ,and then go back to the backend for getting teh text form Buzzfeed, and the indico stuff. 



As the world become increasingly uploaded into the web, it is important to 
extract data from various online resources to study political and socioeconomic trends. Empirical data, especially regarding the opinions of a population between the ages of 12 and 30, can be collected from the web from sources such as Facebook and Youtube. For example, the question: “To what extent has Islamaphobia spread throughout social media in youth?” could target Twitter tweets with the word “Islam,” returning the comments as a JSON. Twitter’s very detailed API enables social researchers to download the data set instead of having to go on Twitter, type in “Islam,” and copy paste the first n or so tweets. Buzzfeed, as one of the world’s leading entertainment and media companies, reflect the ideologies of its target customer, young adults between 13-23, in areas from fashion to world politics to social activism. However, as of now, there is no API to make use of Buzzfeed’s dataset (and very little on github). 

I will not only create an unofficial Buzzfeed API (of GET requests, with the following endpoints):
GET: /search
GET: /<post>/comments

I will also utilize the API to create a website where users can input in a word and that word would be searched in the Buzzfeed API. The comments of each blog post that is extracted using the GET /search would then be parsed through the Indico API to get its sentiment and the words with the highest frequency in the comments of those posts. 

I will then visually display that using D3.js to the users.