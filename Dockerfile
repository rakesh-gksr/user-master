FROM python:3.6.1

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add requirements (to leverage Docker cache)
ADD ./requirements.txt /usr/src/app/requirements.txt

# install requirements
RUN pip install -r requirements.txt

# add app
ADD . /usr/src/app

# unblock port 4000 for the Flask app to run on
EXPOSE 4000

# run server
CMD python manage.py runserver -h 0.0.0.0 -p 4000
