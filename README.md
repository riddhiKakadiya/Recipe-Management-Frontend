# f19-t2-webapp-frontend

# CSYE 7374 - Fall 2019

## Team Information

| Name | NEU ID | Email Address |
| --- | --- | --- |
| Jai Soni| 001822913|soni.j@husky.neu.edu |
| Riddhi Kakadiya| 001811354 | kamlesh.r@husky.neu.edu |
| Sreerag Mandakathil Sreenath| 001838559| mandakathil.s@husky.neu.edu|
| Vivek Dalal| 001430934 | dalal.vi@husky.neu.edu |



## Circle CI setup
### Required Environment variables
```bash
DOCKERHUB_USERNAME = <DOCKERHUB_USERNAME>
DOCKERHUB_PASS = <DOCKERHUB_PASS>
DOCKERHUB_IMAGE_NAME = <DOCKERHUB_USERNAME/TAG> 
```
DOCKERHUB_IMAGE_NAME eg. sreeragsreenath/f19-t2-webapp-frontend


## Docker Commands

### Docker local build command
```bash
docker build -t <USER_NAME>/f19-t2-webapp-frontend:latest .
```

### Docker run command
```bash
docker run -ti -e BACKEND_HOST=localhost -e BACKEND_PORT=8000 -p 8001:8000 <USER_NAME>/f19-t2-webapp-frontend:latest
```

### Docker push command
```bash
docker push <USER_NAME>/f19-t2-webapp-frontend:latest
```

## Instructions to set up and run the application application 'f19-t2-webapp-frontend' locally

## Install Dependencies
```bash
sudo dnf update -y
python3 -m pip install --user --upgrade pip
python3 -m pip install --user virtualenv
```

## ENV File Example
```bash
export DJANGO_PROFILE=local
export MARIADB_USERNAME=root
export MARIADB_PASSWORD=<Password>
export MARIADB_DATABASE=<Database>
export BACKEND_API=/v1/allrecipes
export BACKEND_HOST=localhost
export BACKEND_PORT=8001
echo "Local profile set"
```

```bash
source ~/.django/.local_env
```

## Run command:
```bash
cd djangoEnv/ && source bin/activate 
python3 manage.py runserver
```

```bash
use your local host to run the application
```