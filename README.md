Introduction
This project is a simple note-taking application's backend, built with Python, Docker and MySQL. It provides a RESTful API that allows users to create, read, update, and delete notes. This guide will help you understand the structure of the project, the purpose of each part, and how to get everything up and running.

Project Structure
api/server.py: The heart of our application. This Python script uses the built-in http.server module to listen for HTTP requests and respond to them. It can handle requests to view, add, edit, or delete notes.
api/database_handler.py: This script manages all interactions with the MySQL database. It executes SQL queries to retrieve, insert, update, or delete notes from the database.
db/init.sql: A SQL script that sets up the initial structure of the database. It creates the necessary tables and schemas for storing notes.
docker-compose.yml: A Docker Compose file that defines how to run our application and its database in containers. It makes setting up and running our environment easy.
Dockerfile: Instructions for Docker on how to build the image for our API server. It specifies the environment, dependencies, and what command to run.
.gitignore: A file that tells Git which files or directories to ignore in version control. This helps prevent unnecessary files from being added to our repository.
tests/test_requests.sh: A simple script with curl commands to test the API endpoints. It's used to manually verify that our API is working as expected.

Running the Project
To run this project, you'll need Docker installed on your computer. Once installed, follow these steps:

Open a terminal and navigate to the project directory.
Run docker-compose up --build to build and start the containers for both the API server and the MySQL database.
The API will be accessible at http://localhost:8080. You can use tools like Postman or the provided test_requests.sh script to test the API endpoints.
Testing the API
After starting the API, you can test it by sending HTTP requests to create, read, update, or delete notes. The tests/test_requests.sh script provides examples of how to use curl to make these requests. Alternatively, you can use Postman to send requests and view responses.

Also, To test your API with curl, you can also execute commands in your terminal. Here are examples for each type of request:
GET request to retrieve notes:
curl http://localhost:8080/notes
POST request to create a new note:
curl -X POST http://localhost:8080/notes -H "Content-Type: application/json" -d '{"title": "New Note", "content": "This is a new note."}'
PUT request to update an existing note (replace 1 with the actual note ID):
curl -X PUT http://localhost:8080/notes/1 -H "Content-Type: application/json" -d '{"title": "Updated Note", "content": "This note has been updated."}'
DELETE request to delete an existing note (replace 1 with the actual note ID):
curl -X DELETE http://localhost:8080/notes/1

When you're done testing, you can stop the Docker containers by pressing Ctrl+C in the terminal where Docker Compose is running. To remove the containers completely, use the following command:

docker-compose down

Conclusion
This project demonstrates a simple yet functional backend for a note-taking application. By following the instructions above, you can get the application running and test the API endpoints.
