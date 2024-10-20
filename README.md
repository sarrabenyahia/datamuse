
# Datamuse : What to do in Paris ? 

<br>

## About the Project
The following project is realized as part of the Linux course given by the MoSEF Master at the University of Paris 1 Panthéon-Sorbonne. The main goal is to deploy an app with Docker or with a simple shell file. We have decided to backend the application with a NLP model based on TF-IDF to make recommendations from opendata.paris.fr

![Alt Text](https://github.com/sarrabenyahia/datamuse/blob/main/img/Capture%20d%E2%80%99%C3%A9cran%202023-06-06%20%C3%A0%2015.12.01.png)

In this repository, you will find the following elements:
* A canva presentation 'Datamuse' to explain the purpose of our project. 
* A webapp folder and an app_docker folder

## Problematic

After spending several days in Paris or living permanently in Paris, you have already visited all the museums. What activity can I do? Less known museums, concerts, shows... Write what you want and we will advise you!

The project is built in two parts. 
<br>


<!-- Console Application -->
## Console Application:
The first part is the console version of the final application, our "beta-application" if you want. This version of the application takes into account two arguments : the data as a csv file, and the keyword that serves as your research (for example, Louvre, Opéra, or even Picasso) to let the recommendation system find the most similar events to suggest to the user.

### Installation and launching of the console application:

1. Clone the repository
```sh
https://github.com/sarrabenyahia/datamuse.git
```
2. Change your current working directory
```sh
cd app_docker
```
3. Install required dependencies
```sh
source install.sh
```
3. Launch the application with the keyword of your choice (keep in mind to translate your searches in french 🇫🇷 for example : Louvre)
```sh
bash launch.sh [keyword]
```

<!-- WEB APP -->
## Web application
Our Webapp allows users to receive recommendations using NLP and similarity computing with the TF-IDF cosine similarity matrix.
The app is hosted on the local machine at http://localhost:8000/.

The main page, or "Home", is just a simple user guide for the app!
After mastering the console application and having dockerized it, we challenged ourselves by creating a web application using the django package.

- Created Django form with the research key-word to be entered
- Created views for index page and prediction page. The predict view inputs the key-word as values to the NLP model. (File: webapp/linux_app/views.py)
- The model outputs the label index of the recommended cultural events. The title and other information of the events recommended are fetched from the api downloaded file of https://opendata.paris.fr/ (File: data.csv).
- An HTML page is rendered with that serves as a home page to explain the purpose of the project to the user (File: webapp/linux_app/templates/result.html)
- An HTML page is rendered with the form and the recommended events. (File: webapp/linux_app/templates/result.html)

### Installation and launching of the django webapp

1. Clone the repository
```sh
https://github.com/sarrabenyahia/datamuse.git
```
2. Change your current working directory
```sh
cd webapp
```
3. Install required dependencies 
```sh
source install.sh
```
3. Launch the application with the keyword of your choice (keep in mind to translate your searches in french 🇫🇷 for example : Louvre)
```sh
bash launch.sh [keyword]
```

![Alt Text](https://github.com/sarrabenyahia/datamuse/blob/main/img/Capture%20d%E2%80%99%C3%A9cran%202023-06-06%20%C3%A0%2015.12.33.png)

### Access to our app:

* Django Web App: http://127.0.0.1:8000

## Note
* Our Web App is ready for deployement in a web server but a .env file with manage.py : debug and secret_key must be created to maintain a certain security level.
* Our presentation on [canva](https://www.canva.com/design/DAFVY1C0EO4/q6OMxjwykrttN0HMmBHwcA/view?utm_content=DAFVY1C0EO4&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

## Contact

* [Sarra Ben Yahia 👩🏻‍💻](https://github.com/sarrabenyahia) - Sarra.benyahia@etu.univ-paris1.fr
* [José Ángel García Sánchez 👨🏻‍💻](https://github.com/JoseAngelGarciaSanchez) - jose-angel.garcia-sanchez@etu.univ-paris1.fr

## Acknowledgments
* A special thank you to @eliamosef for introducing and teaching us the basics in his linux course!
