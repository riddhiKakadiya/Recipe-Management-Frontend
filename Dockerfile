# Here the FROM clause states which base image we are intending to work with. If the image does not exist, locally, Docker automatically fetches it from Dockerhub. If you supplied a URI for the image, Docker will download it from there too.
FROM python:3
ENV PYTHONUNBUFFERED 1


RUN mkdir /FrontEndProject

# Tells Docker to create a working directory that the container will by default use for your project. When you docker -ti <image> it will check into this folder first
WORKDIR /FrontEndProject

# This command tells Docker to copy files from our local machine, into the container that is being built. In some cases we can choose to download our code from Github or any other source, for our case it is simple enough to just COPY the welcome-app to Docker. and place it in the WORKDIR mentioned earlier.
COPY webapp/FrontEndProject/requirements.txt /FrontEndProject

RUN pip install -r requirements.txt

COPY webapp/FrontEndProject/. /FrontEndProject

EXPOSE 8000

CMD ["./start.sh"]