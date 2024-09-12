Ensure Docker and Docker Compose are Installed: Make sure Docker and Docker Compose are installed on your system. You can check their installation with:

******************************************************
docker --version
docker-compose --version
Navigate to the Project Directory: Open your terminal and navigate to the directory containing your docker-compose.yml file:

******************************************************
cd /path/to/your/project
Build and Start the Containers: Build and start your Docker containers using Docker Compose:

******************************************************
sudo docker-compose up --build
Verify Docker Daemon is Running: Make sure the Docker daemon is running. You can start it with:

******************************************************
sudo systemctl start docker
Check the status with:

******************************************************
sudo systemctl status docker
Check Docker Socket Permissions: Ensure the Docker socket file has the correct permissions:

******************************************************
ls -l /var/run/docker.sock
It should look like this:

******************************************************
srw-rw---- 1 root docker 0 Sep 12 09:00 /var/run/docker.sock
If the permissions are incorrect, adjust them:

******************************************************
sudo chmod 660 /var/run/docker.sock
sudo systemctl restart docker
Add User to Docker Group: The error may occur if your user is not part of the Docker group. Add your user to the Docker group with:

******************************************************
sudo usermod -aG docker $USER
Then adjust the socket ownership and permissions:

******************************************************
sudo chown root:docker /var/run/docker.sock
sudo chmod 660 /var/run/docker.sock
Note: You may need to log out and log back in for group membership changes to take effect.

Run Database Migrations: If you haven’t already run migrations, do so with:

******************************************************
sudo docker-compose run web python manage.py makemigrations
sudo docker-compose run web python manage.py migrate
This command will apply any pending migrations to your database.

Create a Superuser (Optional): If you need a superuser to access the Django admin interface, create one with:

******************************************************
sudo docker-compose run web python manage.py createsuperuser
Follow the prompts to enter the superuser credentials.