Instructions for Running the Django Project
Ensure Docker and Docker Compose are Installed: Make sure Docker and Docker Compose are installed on your system. You can check their installation with:


********************************************************
docker --version
docker-compose --version
Navigate to the Project Directory: Open your terminal and navigate to the directory containing your docker-compose.yml file.


********************************************************
cd /path/to/your/project
Build and Start the Containers: Build and start your Docker containers using Docker Compose:



1. Check Docker Service Status
Ensure that the Docker service is running. You can start Docker with the following command:

**********************************************************************************************
sudo systemctl start docker



2. Add User to Docker Group
The error may occur if your user is not part of the Docker group, which is required to access Docker without sudo. Add your user to the Docker group with:

**********************************************************************************************
sudo usermod -aG docker $USER


3. Check Docker Socket Permissions
Ensure the Docker socket file has the correct permissions:

**********************************************************************************************
ls -l /var/run/docker.sock


If it does not, you may need to adjust the permissions or restart Docker:

**********************************************************************************************
sudo chmod 660 /var/run/docker.sock
sudo systemctl restart docker




The errors you're seeing are related to permission issues when Docker Compose tries to connect to the Docker daemon. Here’s a step-by-step guide to help resolve these issues:

1. Verify Docker Daemon is Running
Make sure the Docker daemon is running. You can start it with:

**********************************************************************************************
sudo systemctl start docker
And check its status with:

**********************************************************************************************
sudo systemctl status docker
2. Check Docker Socket Permissions
The Docker socket file should be accessible. Check its permissions with:

**********************************************************************************************
ls -l /var/run/docker.sock
It should look something like this:

**********************************************************************************************
srw-rw---- 1 root docker 0 Sep 12 09:00 /var/run/docker.sock
If the permissions are incorrect, adjust them:

**********************************************************************************************
sudo chmod 660 /var/run/docker.sock
3. Add User to Docker Group
Ensure your user is part of the Docker group. This allows non-root users to access Docker. Add your user to the Docker group with:

**********************************************************************************************
sudo usermod -aG docker $USER


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