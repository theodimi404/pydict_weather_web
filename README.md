# Pydict Weather

This is a web application that implements a previous python application of my own. Instead of using a GUI, I used the framework flask to build a simple web application. 

## Build a Docker Image
* Change directory into the folder that the project exists
* Run the following command to build an image with the name webflask
```
docker build -t webflask:latest .
```
* Create a container with the following command 
```
docker run -d -p 5001:5000 webflask:latest
```
* Access the web application by [typing](http://localhost:5001/home/)