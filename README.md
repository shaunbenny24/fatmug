Instructions for Running the Django Project
Ensure Docker and Docker Compose are Installed: Make sure Docker and Docker Compose are installed on your system. You can check their installation with:


********************************************************
docker --version
docker-compose --version
Navigate to the Project Directory: Open your terminal and navigate to the directory containing your docker-compose.yml file.


********************************************************
cd /path/to/your/project
Build and Start the Containers: Build and start your Docker containers using Docker Compose:


********************************************************

Run Database Migrations: If you haven't already run migrations, do so with:
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate



This command will build the images defined in your Dockerfile and start the containers as specified in your docker-compose.yml file.


docker-compose up --build

********************************************************

This command will apply any pending migrations to your database.

Create a Superuser (Optional): If you need a superuser to access the Django admin interface, create one with:


********************************************************
docker-compose run web python manage.py createsuperuser
Follow the prompts to enter the superuser credentials.