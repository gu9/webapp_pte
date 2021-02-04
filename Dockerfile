FROM ubuntu:16.04
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /web_app/requirements.txt

WORKDIR /web_app

RUN pip install -r requirements.txt

COPY . /web_app
EXPOSE 5000/tcp
CMD [ "flask", "run", "-h", "0.0.0.0" , "-p", "5000"]

