# Pydict Weather

This is a web application that implements a previous python application of my own. Instead of using a GUI, I used the framework [Flask](https://flask.palletsprojects.com/en/1.1.x/) to build a simple web application.

It uses web scraping to collect weather data and it has two end points:

/home ( The home page that asks the user for a city )

/predict ( The page that displays the weather forecast )

## Requirements
Flask == 1.1.2

bs4 == 0.0.1

requests == 2.24.0

## Build a Docker Image
* Change directory into the folder that the project exists, e.g.
```
cd C:\Users\myUser\projects\pydict_weather_web
```
* Run the following command to build an image with the name webflask
```
docker build -t webflask:latest .
```
* Create a container with the following command 
```
docker run -d -p 5001:5000 webflask:latest
```
* Access the web application by typing [http://localhost:5001/home/](http://localhost:5001/home/)

## Run it as a python application
* Create a virtual environment (Windows)
```
python -m venv venv
```
* Activate it
```
venv\Scripts\activate.bat
```
* Install the requirements
```
pip install -r requirements.txt
```
* Run the app
```
python app.py
```
* Access the web application by typing [http://localhost:5000/home/](http://localhost:5001/home/)

### Disclaimer

This project is made for fun and to learn more about the framework [Flask](https://flask.palletsprojects.com/en/1.1.x/).
I do not own the data that I am scraping.