/*
  Project Name: GDP- Gathering Detection Platform
  File Name: CoordinateRepository.java
  Author: Margherita Mitillo
  Creation Date: 2021-03-23
  Summary: the file is the class that represents the type of data saved in the collection detection
  Last change date: 2021-04-01
*/
package com.webapp.spring.data.mongodb.model;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "detection")
public class Detection {

    @Id
    private String id;
    private int id_webcam;
    private String city;
    public String location;
    public float latitude;
    public float longitude;
    public int numPeople;
    public String date;
    public String time;
    public int type;
    public String weather_description;
    public float temperature;
    public int day_of_week;

    public Detection() {
    }

    public Detection(String id, int id_webcam, String city, String location, float latitude, float longitude,
            int numPeople, String date, String time, int type, String weather_description, float temperature,
            int day_of_week) {
        this.id = id;
        this.id_webcam = id_webcam;
        this.city = city;
        this.location = location;
        this.latitude = latitude;
        this.longitude = longitude;
        this.numPeople = numPeople;
        this.date = date;
        this.time = time;
        this.type = type;
        this.weather_description = weather_description;
        this.temperature = temperature;
        this.day_of_week = day_of_week;
    }

    @Override
    public String toString() {
        return "Detection [id=" + id + ", id_webcam=" + id_webcam + ", city=" + city + ", location=" + location
                + ", latitude=" + latitude + ", longitude=" + longitude + ", numPeople=" + numPeople + ", date=" + date
                + ", time=" + time + ", type=" + type + ", weather_description=" + weather_description
                + ", temperature=" + temperature + ", day_of_week=" + day_of_week + "]";
    }
}