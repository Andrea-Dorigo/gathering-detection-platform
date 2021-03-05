from mongoengine import *


connect("GDP-test", host="localhost", port=27017)


class Detection(Document):
    id_webcam = IntField(required=True)
    latitude = DecimalField(required=True)
    longitude = DecimalField(required=True)
    numPeople = IntField(required=True)
    date = StringField(required=True)
    time = StringField(required=True)

    def json(self):
        daily_dict = {
            "id_webcam": self.id_webcam,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "numPeople": self.numPeople,
            "date": self.date,
            "time" : self.time
        }
        return json.dumps(daily_dict) #dumps converte python to json

#arrivano i dati
arr = [1, 2, 5, 25, '05-03-2021', '11:29']
arr2 = [2, 5, 34, 5, '05-03-2021', '12:35']


#aggiungo un documento alla collection con quel dato
detection = Detection(
    id_webcam = arr[0],
    latitude = arr[1],
    longitude = arr[2],
    numPeople = arr[3],
    date = arr[4],
    time = arr[5]
).save()


for x in range(6):
    detection = Detection(
        id_webcam = arr[0],
        latitude = arr[1],
        longitude = arr[2],
        numPeople = arr[3],
        date = arr[4],
        time = arr[5]
    ).save()

for x in range(6):
    detection = Detection(
        id_webcam = arr2[0],
        latitude = arr2[1],
        longitude = arr2[2],
        numPeople = arr2[3],
        date = arr2[4],
        time = arr2[5]
    ).save()


#
# class Daily(Document):
#     webcam = StringField(required=True)
#     coordinates = ListField()
#     date = DateTimeField(required=True)
#     counting = ListField() #da vedere
#
#     def json(self):
#         daily_dict = {
#             "webcam": self.webcam,
#             "coordinates" : self.coordinates,
#             "date": self.date,
#             "counting": self.counting
#         }
#         return json.dumps(daily_dict) #dumps converte python to json


# day = Daily(
#     webcam = "webcam piazza navona" ,
#     latitude = 33,
#     longitude = 55,
#     date = "04-03-2021"
# ).save()

# day = Daily(
#     webcam = "webcam piazza navona" ,
#     latitude = 33,
#     longitude = 55,
#     date = "04-03-2021"
# )
# day.counting =[
#     ('15:30', 15),
#     ('15:40', 20),
#     ('15:50', 13),
# ]
#
# day = Daily(
#     webcam = "webcam fontana trevi" ,
#     latitude = 33,
#     longitude = 55,
#     date = "04-03-2021"
# )
# day.counting =[
#     ('15:30', 30),
#     ('15:40', 24),
#     ('15:50', 27),
# ]
# day.save()
# try:
#     day.save()
# except NotUniqueError:
#     print("solo per ricordarmi per la gestione errori")

# #Query al database
# days = Daily.objects()
#
# print(days)
#
# for day in days:
#     print(day.webcam, day.latitude, day.counting)
#
#
# #Divido i dati per webcam
# trevi_days = Daily.objects(webcam="webcam fontana trevi")
#
# for a in trevi_days:
#     print(a.webcam, a.counting)
