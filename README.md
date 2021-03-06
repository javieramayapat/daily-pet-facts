<h1 align="center" id="title">πΈ Daily Pet Facts πΆ</h1>

Public API to have fun and share knowledge about our domestic pets. πΈπ€πΆ

## πTable of Contents
- [οΏ½Table of Contents](#table-of-contents)
- [π Demo](#-demo)
- [π‘Features](#features)
- [π§βπ» Installation Steps](#-installation-steps)
- [The process](#the-process)
  - [ποΈ Build with](#οΈ-build-with)
- [Licence](#licence)
- [Author](#author)

## π Demo
![Daily Pet Facts](docs/images/pet-facts-api-documentation.png)

## π‘Features
Here're some of the projects's best features:
- Get a list of facts about our favorite pets. [π₯,π₯,π₯]
- Get the detail of a fact in specific. π₯
- List a list with our best pest registered [π€,πΈ,πΆ]
- Get a pet detail πΈ

## π§βπ» Installation Steps
1. Clone the repository
2. Create your virtual enviromen with the command `py -m venv venv`
3. Install requirements in your virtual enviroment `pip install -r requirements.txt`
4. Create the env file in the root of the project `.env` and copy the content of the `.env.example` to configurate environment variables.

5. You can run the following command to buil the image. `$ docker-compose build`

6. Once the image is built, run the container: `$ docker-compose up -d`

7. If you want to be faster in launching the project you can use the following command to perform the above two steps in one. `$ docker-compose up --build`
8. Now go to http://127.0.0.1:8000/docs and enjoy the app.
##  The process
### ποΈ Build with
Technologies used in this project:

- [Docker](https://www.docker.com/) π
- [Python](https://www.python.org/) π
- [FastAPI](https://fastapi.tiangolo.com/) π
- [Pydantic ](https://pydantic-docs.helpmanual.io/) π―
- [PostgreSQL](https://www.postgresql.org/) π
- [SQLAlchemy](https://www.sqlalchemy.org/) βοΈ

To get started you just need to download docker on your machine, I leave the link right here. β‘οΈ [Docker](https://www.docker.com/get-started "Docker").


## Licence
> This project is licensed under the MIT License

## Author
Made with π by [javieramayapat](https://www.linkedin.com/in/javieramayapat/)