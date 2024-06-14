Do the following commands:

docker compose build 

docker-compose up


For making superuser: docker exec -it api python manage.py createsuperuser   


make a .env file that has something like these, you can pass whatever db you wish to connect to, I made a db called movies and connected to it. 
SECRET_KEY=
DB_NAME=movies
DB_USER=postgres
DB_PASSWORD=password
DB_HOST=host.docker.internal
DB_PORT=5432
