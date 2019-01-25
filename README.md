
run docker image on mac

docker run -p 5000:4000 --volume=/Users/admin/Documents/flask_web:/appaa flaskdock:latest

1. Steps to push the docker image to docker hub:

1. docker login --username username --password password 
2. docker tag [my-image] [username/your-repo-name] 
3. docker push username/your-repo-name