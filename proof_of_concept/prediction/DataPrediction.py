from mongoengine import *
import numpy as np
import datetime
import pandas
import matplotlib.pyplot as plt
import sklearn
import sklearn.preprocessing
import sklearn.model_selection
import sklearn.linear_model
from sklearn.ensemble import RandomForestRegressor
import tabulate
import requests, json
import time
import pickle
from datetime import date, datetime, timedelta


PATH_WEBCAM_JSON = "../acquisition/webcams.json"


connect("GDP-test", host = "localhost", port = 27017)
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

class weather_forecast(Document):
    latitude = FloatField(required=True)
    longitude = FloatField(required=True)
    datetime = DateTimeField(required=True)
    weather_description = StringField()
    temperature = FloatField()

def predict(webcam):
    print(webcam["city"])
    # vedere se posso prendere solo le città per poi fare query distinte
    table = pandas.DataFrame(Detection.objects(city=webcam['city'],type=0).as_pymongo()) #prelevo i dati di roma
    table = table.dropna()
    print(table.shape)
    most_freq = lambda x: x.value_counts(dropna=True).index[0]

    table_a = table
    table_a = table_a.drop(columns = ['_id','id_webcam','city','type','date','location','latitude','longitude'])
    table_a['time'] = pandas.to_datetime(table_a['time'])
    table_a.sort_values(by='time', inplace=True)

    tb = table_a.groupby([pandas.Grouper(key='time', freq='30T')], as_index=False).agg( time=('time', most_freq)
                                                                       , meanPeople=('numPeople', 'mean')
                                                                       , temp=('temperature','mean')
                                                                       , weather=('weather_description', most_freq )
                                                                       , day_of_week=('day_of_week', most_freq))


    tb = tb.dropna()
    tb.plot('time','meanPeople')

    forecast = pandas.DataFrame(weather_forecast.objects(latitude=webcam['latitude']).as_pymongo()) #prelevo i dati di Djakovo
    forecast = forecast.drop(columns = ['_id','latitude','longitude'])

    forecast['datetime'] = pandas.to_datetime(forecast['datetime'])
    forecast = forecast.groupby('datetime').first().reset_index()
    forecast.sort_values(by='datetime', inplace=True)


    today = datetime.today()
    tomorrow = today + timedelta(days=1)
    midnight0 = datetime.combine(today, datetime.min.time())
    midnight1 = datetime.combine(tomorrow, datetime.min.time())

    forecast = forecast.loc[(forecast['datetime'] >= midnight0)]
    forecast = forecast.loc[(forecast['datetime'] < midnight1)].reset_index()
    # print(forecast.to_markdown())


    weekday = np.full((24,1),today.weekday())
    fc = pandas.DataFrame()
    fc.insert(0,'time', np.arange(0,24))
    fc.insert(1,'temp', forecast['temperature'].iloc[0:24])
    fc.insert(2,'weather', forecast['weather_description'].iloc[0:24])
    fc.insert(3,'day_of_week', weekday[0:24])

    print(fc)

    forecast_dummies = fc['weather'].unique()
    print(forecast_dummies.shape)
    detection_dummies = tb['weather'].unique()
    print(detection_dummies.shape)
    # print(np.concatenate((forecast_dummies, detection_dummies), axis=0))
    le = sklearn.preprocessing.LabelEncoder()
    le.classes_ = np.unique(np.concatenate((forecast_dummies, detection_dummies), axis=0))

    fc['weather'] = le.transform(fc['weather'])
    tb['weather_dummy'] = le.transform(tb['weather'])

    print(fc)

    tb['time'] = tb['time'].dt.hour

    tb = tb.dropna()
    tb = tb.reset_index()

    #divide the dataframe 70-30 for train and test
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(
        tb[['time','temp','day_of_week','weather_dummy']],
        tb['meanPeople'],
        test_size = 0.33, shuffle = True, random_state= 42)


    #Modello tipo Regressione Lineare standard

    modelLReg = sklearn.linear_model.LinearRegression()
    #provo a dargli in pasto tutto
    #prima di questo ora bisogna dividere tutto il dataset in 70-30
    modelLReg.fit(x_train, y_train)


    # The coefficients
    print('Coefficients: \n', modelLReg.coef_)

    # The mean square error
    print("Residual sum of squares: %.2f" % np.mean((modelLReg.predict(x_test) - y_test) ** 2))

    # Explained variance score: 1 is perfect prediction
    print('Variance score: %.2f' % modelLReg.score(x_test, y_test))


    #Modello tipo Forest

    modelForest = RandomForestRegressor(n_estimators = 1000)

    modelForest.fit(x_train,y_train)
    pickle.dump(modelForest, open("modelForest_" + webcam['location'] + ".pkl", "wb"))


    print('Forest score : %.2f' % modelForest.score(x_test,y_test))
    forest_prediction= modelForest.predict(fc)
    plt.title("Random Forest")
    forest_prediction = np.rint(forest_prediction)
    #ATTENZIONE: CONVERTENDO IN INTERO PERDO LA PRECISIONE.
    print(forest_prediction)
    plt.plot(fc['time'],modelForest.predict(fc))




    # timePred = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days = 1)
    # timeDelta = timedelta(hours = 1)
    # xTime = []
    # xtime = np.asarray(xTime)
    # for i in range(24):
    #     xTime.append(timePred+timeDelta*i)
    dtPrediction = pandas.DataFrame()
    dtPrediction.insert(0,'id_webcam', table['id_webcam'].iloc[0:24])
    dtPrediction.insert(1,'city', table['city'].iloc[0:24])
    dtPrediction.insert(2,'location', table['location'].iloc[0:24])
    dtPrediction.insert(3,'latitude', table['latitude'].iloc[0:24])
    dtPrediction.insert(4,'longitude', table['longitude'].iloc[0:24])
    dtPrediction.insert(5,'numPeople', forest_prediction[0:24])
    dtPrediction.insert(6,'date', forecast['datetime'].iloc[0:24])
    dtPrediction.insert(7,'time',  forecast['datetime'].iloc[0:24])
    dtPrediction.insert(8,'type', int(1))
    dtPrediction.insert(9,'weather_description', forecast['weather_description'])
    dtPrediction.insert(10,'temperature', forecast['temperature'])
    dtPrediction.insert(11,'day_of_week', fc['day_of_week'])

    print(dtPrediction)
    for i in range(24):
      Detection(id_webcam = dtPrediction['id_webcam'][i], city = dtPrediction['city'][i],location = dtPrediction['location'][i],latitude = dtPrediction['latitude'][i],longitude = dtPrediction['longitude'][i],numPeople = dtPrediction['numPeople'][i],date = dtPrediction['date'][i],time = dtPrediction['time'][i],type = dtPrediction['type'][i],weather_description = dtPrediction['weather_description'][i],temperature = dtPrediction['temperature'][i],day_of_week = dtPrediction['day_of_week'][i]).save()


def main():

    # load json with webcams data
    with open(PATH_WEBCAM_JSON) as f:
      json_data = json.load(f)

    # wait until midnight
    tomorrow = datetime.today() + timedelta(days=1)
    midnight = datetime.combine(tomorrow, datetime.min.time())
    five_past_midnight = midnight + timedelta(minutes=5)

    print( "waiting until: " + str(five_past_midnight) +
           ";\ntime remaining: " + str(five_past_midnight - datetime.now()) )
    #
    time.sleep((midnight - datetime.now()).total_seconds())

    # infinite loop
    while True:

        # get next day midnight

        tomorrow = datetime.today() + timedelta(days=1)
        midnight = datetime.combine(tomorrow, datetime.min.time())
        five_past_midnight = midnight + timedelta(minutes=5)

        # loop all webcams
        for webcam in json_data["webcams"]:
            try:
                predict(webcam)
            except:
                print('EXCEPTION OCCURRED')

        # # sleep until the next midnight
        time.sleep((five_past_midnight - datetime.now()).total_seconds())


main()
