FROM mageai/mageai:0.8.41

RUN apt-get -y update

COPY ./airbnb/ /home/src/airbnb
COPY ./run_app.sh /home/src/run_app.sh
COPY ./sourceme.sh /home/src/sourceme.sh
COPY ./data-source /home/src/data-source

RUN pip install -r airbnb/requirements.txt
