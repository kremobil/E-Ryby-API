#Ryby.pl - REST API
This is an API with data for Ryby.pl site.

##Informations
###Idea
the idea to create this API was born when i created the website about fishes with my friend Paweł gołata
###Tables
This site contains information about fishes sorted in table called fishes.
and admin users. stored in table called users.
####Users table contains
    id      username        password

    int     text            text
####Users table contains
    id      name        latinName       bait        protected       attitude

    int     text        text            text        boolean         text
###Security
This API use Flask-JWT to authenticate users. only authenticated users can
access the POST, PUT and DELETE methods.
###Author
Wiktor Fajkowski 30.08.2022
##Installation
###Python

First you must install python from this link: 
[Python Download](https://www.python.org/downloads/)
###Libraries Installation
to install the libraries you must use pip comand inside your terminal
down below i write all needed libraries
```
pip install Flask
pip install Flask-RESTful
pip install Flask-JWT
pip install Flask-SQLAlchemy
pip install Flask
pip install Flask-Cors
```
##Deployment
This app is deployed on heroku and can be access from this [link](google.com)