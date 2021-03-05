from mongoengine import *
import datetime

nameDB = 'gdp_test'
hostDB = 'localhost'
portDB = 27017

db = connect(nameDB, host=hostDB, port=portDB)


class Webcam(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    dateTime = DateTimeField(required=True)


# query collection
# wCam = Webcam.objects()

 #test for insert (it works



for i in range(20):
    test = Webcam(email = "ciao"+str(i), first_name = "ciao", last_name = "ciao", dateTime = datetime.datetime.now()).save()

#print(db)

#tmp = Webcam.objects(dateTime__lt=datetime.datetime(2021, 2, 19, 15, 44, 50))

#print(tmp[1].email)

#for wc in tmp:
#    print(wc.email)
