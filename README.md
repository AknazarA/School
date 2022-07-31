# School

### Website for automation school processes

## Prerequisites

## Install
- Python: 3.9.1
- Docker Desktop - [Download](https://docs.docker.com/get-docker/)

## Steps

- Clone the current github folder
- Create a virtual environment (Do not forget to activate it)
- Go to the directory with "docker-compose.yml" file
- Open a command line there and run `docker-compose up`
	* if it will show some errors (like "Is the server running on that host and accepting TCP/IP connections?") and does nothing. Press “CTRL + C” and type again `docker-compose up`. It happens because school_web starts before database is fully finished.
- When it runs, go to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and log in with these credentials:
	* Phone: 123456789
	* Password: 123456789
- Create a School, Class, Subject(optional) instances
- Then you can go to [http://127.0.0.1:8000/student/](http://127.0.0.1:8000/student/) and check the website
- URLS:
	* [http://127.0.0.1:8000/register/](http://127.0.0.1:8000/register/) - Register a teacher
	* [http://127.0.0.1:8000/login/](http://127.0.0.1:8000/login/) - Authorize a teacher
	* [http://127.0.0.1:8000/mailing/](http://127.0.0.1:8000/mailing/) - Send mass mail to teachers's classes
	* [http://127.0.0.1:8000/student/](http://127.0.0.1:8000/student/) - CRUD student