from time import sleep
from json import dumps
from kafka import KafkaProducer
from datetime import datetime,timedelta
#descrizione codice
#KafkaProducer = è il metodo per generare il client per pubblicare i record sul cluster Kafka
#Attributi di KafkaProducer:
#bootstrap_server = host:porta di base è localhost:9092
#client_id = un nome per il client
#key_serializer = converte le chiavi dello user in bytes
#value_serializer = usato per convertire il messaggio dello user in bytes
#acks = può essere 0,1,'all' , numero di acknwoledgments che il producer deve ricevere per considerare una richiesta completata 
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8')
                         )



#generate an object datetime from string
date_time_str = '2018-06-29 08:15:27.243860'
date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')


current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
print(current_time)
current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

  
for e in range(1000):
    #data = {'number' : e}
    data = { 'id_webcam': 1, 'city': "Roma", 'location': "Piazza Navona", 'longitude': 41.899139, 'latitude': 12.473311, 'numPeople': e, 'date': current_date, 'time': current_time, 'type': 0, 'weather_condition': "sunny",  'temperature': 12.4, 'day_of_week': 3}
    producer.send('numtest', value=data)
    sleep(5)
