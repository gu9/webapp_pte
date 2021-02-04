FROM ubuntu:16.04
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /web_app/requirements.txt

WORKDIR /web_app

RUN pip3 install -r requirements.txt

COPY . /web_app
RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
EXPOSE 8081

