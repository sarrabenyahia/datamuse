
# Datamuse : What to do in Paris ? 

## Table of Contents

* [About the Project](#about_the_project)
* [Problematic](#prob)
* [Web Application](#web_app)
  * [Installation](#installation)
  * [Lauching the app](#launch_app)
  * [Usage](#usage)
* [Contact](#contact)

<br>

## About the Project
The following project is realized as part of the Linux course given by the MoSEF Master at the University of Paris 1 Panthéon-Sorbonne. The main goal is to deploy an app with Docker or with a simple shell file. We have decided to make an NLP model based on TF-IDF to make recommendations from opendata.paris.fr



In this repository, you will find the following elements:
* A canva presentation 'Datamuse' to explain the purpose of our project. 
* A Docker-compose.yml which orchestrates the containers.
* Some Docker Images each folder corresponds to an Image to build (with Python)):
    * collect_from_spotify_api : Request data from Spotify with Python (with Spotipy package)
    * dash_app_analytics : Create a user web-app on local host with Dash



## Problematic

After spending several days in Paris or living permanently in Paris, you have already visited all the museums. What activity can I do? Less known museums, concerts, shows... Write what you want and we will advise you!

The project is built around 4 containers (available on the docker-compose): the data collection (+ sending to MySQL)
the SQL database, the SQL database viewer and the web-app.
<br>

## MySQL app:
 This container is just as important, if not more so, for people who do/want to do data science. We particularly wanted to make a MySQL database because it allows us to store data in a structured way that can easily be used in languages other than Python.
The database consists of a table for artists and another for songs. In the latter, users can find features about the song (such as its acousticness, danceability score, etc. - see Spotify documentation at https://developer.spotify.com/discover/#audio-features-analysis).
To populate this database, we use the collect_from_spotify_api container, which uses the Python Spotipy package to request data. I encourage you to check out the documentation for more information.
Note: It is necessary to have Spotify access to build this database.
The visual SQL interface is available at http://localhost:8080/.


<!-- WEB APP -->
## Web Application
Our Dash web app allows users to view information about a selected artist() and receive song recommendations using ML. The app is hosted on the local machine at http://localhost:8000/.

The main page, or "Home", is just a simple user guide for the app!

The first tab is an overview of the artist of the user's choice. It provides statistical information such as the popularity score and the top 10 songs, as well as star graphs that allow the comparison of different artists or songs. In addition to being fun, this format allows for an easy understanding of the artist's characteristics.

The second tab is a simple recommendation system. The project is not focused on using machine learning, so we used a simple K-means model on the artists and songs. By forming clusters (determined using traditional methods), we have groups of similar artists/songs. Based on the user's desire for an artist or song suggestion, we provide content. 


### Installation
In order to run the code, you will need to create API access for Spotify and Lastfm. It's free so don't hesitate to make it! (https://developer.spotify.com/dashboard/ and https://www.last.fm/api/account/create)
1. Clone the repository
```sh
git clone https://github.com/luciegaba/spotify_app
```
2. Change your current working directory
```sh
cd spotify_app
```
3. Create a .env file like the following one:
```sh
# In dashboard 
SPOTIPY_CLIENT_ID="spotify_client_id"
SPOTIPY_CLIENT_SECRET="spotify_client_secret"


LASTFM_API_KEY="lastfm key"
LASTFM_API_SECRET="lastfm secret"

#You can leave it like that it's not necessary secrets
CREDS_MYSQL_RAP_USERNAME="root"
CREDS_MYSQL_RAP_PASSWORD="frenchrap2022"
CREDS_MYSQL_RAP_HOST="mysqldb"
CREDS_MYSQL_RAP_DB="mysqldb"
SQL_REQUEST_ARTISTS="SELECT * FROM artists;"
SQL_REQUEST_TRACKS="SELECT * FROM tracks;"

```

4. Launch shell script to make apps running
(Click on yes for csv options if you have csv and need it to avoid long requests..)
```sh
bash launch.sh
```
If errors, check docker df, group, and eventually use ```docker system prune ```
It can take 10 minutes for mysql database launching as it depends on request app service. Same for dash app which depends on mysql.. Containers that could be affected by dependences have "restarted always" option so it should cause problem.

Remark: Don't push Image on Dockerhub because secrets issue is not resolved
### Access to our apps:

* MySQL:  http://localhost:8080
* Dash App: http://localhost:8000



## Contact

* [Sarra ben Yahia👸](https://github.com/luciegaba) - Sarra.benyahia@etu.univ-paris1.fr
* [José Ángel García Sánchez👨‍🎓](https://github.com/Yanisreh) - jose-angel.garcia-sanchez@etu.univ-paris1.fr
