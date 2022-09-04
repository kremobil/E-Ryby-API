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
This app is deployed on heroku and can be access from this [link](https://ryby-api.herokuapp.com)
##Endpoints
###/fishes
####Get method
this endpoint will return a list of all fishes in json format.
#####example:
[https://ryby-api.herokuapp.com/fishes](https://ryby-api.herokuapp.com/fishes)
###/fish/name
#### Get method
this endpoint will a single record which contains the fish and return it in json format.
###### example: [https://ryby-api.herokuapp.com/fish/sum](https://ryby-api.herokuapp.com/fish/sum)

#### Post method - JWT token required
this endpoint allow you to add informations about fish to database.
you must add data in json format. here is example of json file with information nedded to complete the request.

```
{
    "latin_name": "lorem ipSUM",
    "description": "test",
    "bait": "robaki i ryby",
    "protected": true,
}
```

in this request we can give values:
######"latin_name" - type:string, required: yes, here you must add the fish name in latin.
######"description" - type:string, required: yes, here you must write the description about fish.
######"bait" - type:string, required: no, you must give this value only if fish is not under the protection. just write what bait is needed to catch this fish.
######"protected" - type:boolean, required: no, default:false ,set to True if fish is protected.
######"attitude" - type:boolean, required: no, default:"Żeru spokojnego" ,if fish is aggressive set value to "Drapieżna"


###### example: https://ryby-api.herokuapp.com/fish/sum
#### Put method - JWT token required
this endpoint allow you to add or update information about fish to database.
you must add data in json format. here is example of json file with information nedded to complete the request.

```
{
    "latin_name": "lorem ipSUM",
    "description": "test",
    "bait": "robaki i ryby",
    "protected": true,
}
```

in this request we can give values:
######"latin_name" - type:string, required: yes, here you must add the fish name in latin.
######"description" - type:string, required: yes, here you must write the description about fish.
######"bait" - type:string, required: no, you must give this value only if fish is not under the protection. just write what bait is needed to catch this fish.
######"protected" - type:boolean, required: no, default:false ,set to True if fish is protected.
######"attitude" - type:boolean, required: no, default:"Żeru spokojnego" ,if fish is aggressive set value to "Drapieżna"


###### example: https://ryby-api.herokuapp.com/fish/sum

#### Delete method - JWT token required
with this endpoint you can delete a record with fish from the database.
###### example: [https://ryby-api.herokuapp.com/fish/sum](https://ryby-api.herokuapp.com/fish/sum)