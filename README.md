# low-setup-tutorial
Use this repository to get started with bitswan and write your first pump!

## Prerequisites

- bspump library
- docker and docker-compose
- git


# Getting started

## Step 1: Clone this repository

```bash
git clone https://github.com/bitswan-space/low-setup-tutorial.git
```

## Step 2: Run your first pump with kafka locally using docker-compose
Todo

## Step 3: Install bitswan

If you want to install bitswan, you can do so by running the following command:


## Step 4: Run your first pump with bitswan locally

head over to the `sample_kafka_pump` folder in your terminal and run:
```bash
python3 kafkapump_app.py
```

you should see output similar to this:
```bash
{'data': 5, 'timestamp': '2023-09-27 16:43:33.668252'}
{'data': 63, 'timestamp': '2023-09-27 16:43:34.669802'}
{'data': 29, 'timestamp': '2023-09-27 16:43:35.671566'}
{'data': 8, 'timestamp': '2023-09-27 16:43:36.673247'}
{'data': 60, 'timestamp': '2023-09-27 16:43:37.674116'}
```
## Step 5: Pummp data to kafka topic

Firstly, you have to start local kafka instance. go to root directory of this repository and enter ```bash
docker-compose up -d
```
kafka, zookeeper, and kafdrop should have been started. Now test your kafka by going to ``


This pump is responsible for pumping data to kafka, but when you firstly run it, it was configured to just dump the events. You can change behaviour of pumps in `pipline.py`.

Go to `sample_kafka_pump/tutorialpump/pipeline.py` and change the pump sink based on instructions in the file. You can also change the pump source, but it is not necessary for this tutorial.

You can check if your pump is working by running the following command in your terminal:
```bash
python3 kafkapump_app.py -c sample_kafka_pump/config.conf
```

If you have connection error make sure you have kafka running locally via docker-compose.

as you can see now you newly use configuration file, where we specify the connection to kafka. You can also specify the connection to kafka in the code, but it is not recommended. Don't worry about how configuration file works, we will cover it in the next tutorial.

