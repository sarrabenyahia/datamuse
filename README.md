
# Datamuse : What to do in Paris ? 

## Table of Contents

* [About the Project](#about_the_project)
* [Problematic](#prob)
* [Console Application](#app_docker)
  * [Installation](#installation_app)
* [Web Application](#web_app)
  * [Installation](#installation_webapp)
  * [Lauching the app](#launch_app)
  * [Usage](#usage)
* [Contact](#contact)

<br>

## About the Project
The following project is realized as part of the Linux course given by the MoSEF Master at the University of Paris 1 Panthéon-Sorbonne. The main goal is to deploy an app with Docker or with a simple shell file. We have decided to backend the application with a NLP model based on TF-IDF to make recommendations from opendata.paris.fr

In this repository, you will find the following elements:
* A canva presentation 'Datamuse' to explain the purpose of our project. 
* A webapp folder and an app_docker folder

## Problematic

After spending several days in Paris or living permanently in Paris, you have already visited all the museums. What activity can I do? Less known museums, concerts, shows... Write what you want and we will advise you!

The project is built in two parts. 
<br>


<!-- Console Application -->
## app_docker:
The first part is the console version of the final application, our "beta-application" if you want. This version of the application takes into account two arguments : the data as a csv file, and the keyword that serves as your research (for example, Louvre, Opéra, or even Picasso) to let the recommendation system find the most similar events to suggest to the user.

### Installation console application:

1. Clone the repository
```sh
https://github.com/sarrabenyahia/datamuse.git
```
2. Change your current working directory
```sh
cd app_docker
```
3. Change your current working directory
```sh
source install.sh
```
3. Launch the application with the keyword of your choice (keep in mind to translate your searches in french :France: ) for example : Louvre
```sh
bash launch.sh [keyword]
```


<!-- WEB APP -->
## web_app
Our Webapp allows users to receive recommendations using NLP and similarity computing with the TF-IDF cosine similarity matrix.
The app is hosted on the local machine at http://localhost:8000/.

The main page, or "Home", is just a simple user guide for the app!
After mastering the console application and having dockerized it, we challenged ourselves by creating a web application using the django package.

- Created Django form with the research key-word to be entered
- Created views for index page and prediction page. The predict view inputs the key-word as values to the NLP model. (File: webapp/linux_app/views.py)
- The model outputs the label index of the recommended cultural events. The title and other information of the events recommended are fetched from the api downloaded file of https://opendata.paris.fr/ (File: data.csv).
- An HTML page is rendered with that serves as a home page to explain the purpose of the project to the user (File: webapp/linux_app/templates/result.html)
- An HTML page is rendered with the form and the recommended events. (File: webapp/linux_app/templates/result.html)



### Installation
In order to run the code, you will need to create API access for Spotify and Lastfm. It's free so don't hesitate to make it! (https://developer.spotify.com/dashboard/ and https://www.last.fm/api/account/create)
1. Clone the repository
```sh
https://github.com/sarrabenyahia/datamuse.git
```
2. Change your current working directory
```sh
cd webapp
```



4. Launch shell script to make apps running
(Click on yes for csv options if you have csv and need it to avoid long requests..)
```sh
bash launch.sh
```
If errors, check docker df, group, and eventually use ```docker system prune ```
It can take 10 minutes for mysql database launching as it depends on request app service. Same for dash app which depends on mysql.. Containers that could be affected by dependences have "restarted always" option so it should cause problem.

Remark: Don't push Image on Dockerhub because secrets issue is not resolved
### Access to our app:

* Django Web App: http://localhost:8000


## Contact

* [Sarra Ben Yahia 👩🏻‍💻](https://github.com/sarrabenyahia) - Sarra.benyahia@etu.univ-paris1.fr
* [José Ángel García Sánchez 👨🏻‍💻](https://github.com/Pse1234) - jose-angel.garcia-sanchez@etu.univ-paris1.fr
