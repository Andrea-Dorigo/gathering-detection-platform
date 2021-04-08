/*
  Project Name: GDP- Gathering Detection Platform
  File Name: WebappApplicationTests.java
  Author: Andrea Cecchin
  Creation Date: 2021-03-26
  Summary: the file is the repository that extends MongoRepository 
  Last change date: 2021-03-26
*/
package com.webapp.spring.data.mongodb.customRepository;
import java.util.List;

public interface DetectionCustomRepository {
    public List<String> getCities();
    public List<List<Double>> getLatLngs(String city);
    public List<Detection> getDataRT(String city, String date);
}
