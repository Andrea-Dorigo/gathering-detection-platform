/*
  Project Name: GDP- Gathering Detection Platform
  File Name: WebappApplicationTests.java
  Author: Emma Roveroni
  Creation Date: 2021-04-12
  Summary: the file is the repository that extends MongoRepository 
  Last change date: 2021-04-13
*/

package com.webapp.data.mongodb.modelTest;

import java.util.List;

import com.webapp.spring.data.mongodb.model.Detection;

import java.util.ArrayList;
import java.time.LocalTime;
import static org.junit.Assert.assertEquals;
import org.junit.Test;

import jdk.jfr.Timestamp;

import org.junit.Before;
import org.junit.After;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

public class DetectionTest {

    Detection d;
    String id;
    int id_webcam;
    String city;
    String location;
    float latitude;
    float longitude;
    int numPeople;
    String date;
    String time;
    int type;
    String weather_description;
    float temperature;
    int day_of_week;

    @Before
    public void setup() {
        id = "605afa3c1444b4c212abb28b";
        id_webcam = 1;
        city = "Roma";
        location = "PiazzaNavona";
        latitude = 41.899139f;
        longitude = 12.473311f;
        numPeople = 9;
        date = "2021-03-24T09:36:55.182+00:00";
        time = "2021-03-24T09:36:55.182+00:00";
        type = 0;
        weather_description = "clear sky";
        temperature = 8.74f;
        day_of_week = 2;
        d = new Detection(id, id_webcam, city, location, latitude, longitude, numPeople, date, time, type,
                weather_description, temperature, day_of_week);
    }

    @Test
    public void getIdTest() {
        assertEquals(id, d.getId());
    }

    @Test
    public void getId_webcamTest() {
        assertEquals(id_webcam, d.getId_webcam());
    }

    @Test
    public void getCityTest() {
        assertEquals(city, d.getCity());
    }

    @Test
    public void getLocationTest() {
        assertEquals(location, d.getLocation());
    }

    @Test
    public void getLatitudeTest() {
        assertEquals(latitude, d.getLatitude(), 0.0f);
    }

    @Test
    public void getLongitudeTest() {
        assertEquals(longitude, d.getLongitude(), 0.0f);
    }

    @Test
    public void getNumPeople() {
        assertEquals(numPeople, d.getNumPeople());
    }

    @Test
    public void getDateTest() {
        assertEquals(date, d.getDate());
    }

    @Test
    public void getTimeTest() {
        assertEquals(time, d.getTime());
    }

    @Test
    public void getTypeTest() {
        assertEquals(type, d.getType());
    }

    @Test
    public void getWeather_descriptionTest() {
        assertEquals(weather_description, d.getWeather_description());
    }

    @Test
    public void getTemperatureTest() {
        assertEquals(temperature, d.getTemperature(), 0.0f);
    }

    @Test
    public void getDay_of_weekTest() {
        assertEquals(day_of_week, d.getDay_of_week());
    }
}