# Chat Application

This is a project for the HackUSU 2023 Hackathon. Our goal for this project is to create an
implementation for Kafka and Elasticsearch. We probably wouldn't do this in a real chat  app designed
for such a small scale, but we wanted to learn more about these tools and this seemed like a good
way to do it.

## Setup

1. Download and install [Docker](https://www.docker.com/products/docker-desktop/)

    Kafka, Elasticsearch, and Kibana can all run in Docker containers. This is an easy way to get
    them up and running.

2. Start the containers

    ```bash
    docker-compose up -d
    ```

    This will start Kafka and an Elasticsearch node.

3. Setup Kafka topics

    ```bash
    docker-compose exec kafka kafka-topics --create --bootstrap-server \
    localhost:9092 --replication-factor 1 --partitions 1 --topic chat-message
    ```

4. Finish ElasticSearch setup

    Follow the instructions [here](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html),
    starting at step 3. You will probably have to reset the password for the elastic user because of
    how it starts in docker-compose:

    ```bash
    docker exec -it elasticsearch /usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic
    ```

5. Install Python dependencies (preferably in a virtual environment)

    ```bash
    pip install -r requirements.txt
    ```

6. Setup frontend

    ```bash
    cd frontend/chat-app
    yarn
    ```

7. Start the backend server by running the following command inside the `chatapp` sub-directory

    ```bash
    endpoints --prefix=controllers
    ```

8. Start the consumer by running the following command inside the `chatapp` sub-directory

    ```bash
    python consumer.py
    ```

9. Start the frontend by running the following command inside the `frontend/chat-app` sub-directory

    ```bash
    yarn dev
    ```

## Tools

- Python 3

- Kafka

- Elasticsearch

- Kibana

- [Docker](https://www.docker.com/products/docker-desktop/)

- [Endpoints](https://github.com/Jaymon/testdata)

- [DataTypes](https://github.com/jaymon/datatypes)

- React

- Firebase
