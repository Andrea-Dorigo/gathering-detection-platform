from kafka import KafkaConsumer
import json
from json import loads
from mongoengine import *
consumer = KafkaConsumer(
    'gdp',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))
     
class Detection(Document):
    id_webcam = IntField(required=True)
    city = StringField(required=True)
    location = StringField(required=True)
    latitude = FloatField(required=True)
    longitude = FloatField(required=True)
    numPeople = IntField(required=True)
    date = DateTimeField(required=True)
    time = DateTimeField(required=True)
    type = IntField(required=True)
    weather_description = StringField()
    temperature = FloatField()
    day_of_week = IntField()
    
connect("GDP-test", host = "localhost", port = 27017)         
for message in consumer:
    webcam = message.value
    detection = Detection(
            id_webcam = webcam["id_webcam"],
            city = webcam["city"],
            location = webcam["location"],
            latitude = webcam["latitude"],
            longitude = webcam["longitude"],
            numPeople = webcam["numPeople"],
            date = webcam["date"],
            time = webcam["time"],
            type = webcam["type"],
            weather_description = webcam["weather_description"],
            temperature = webcam["temperature"],
            day_of_week =  webcam["day_of_week"]
            ).save()

