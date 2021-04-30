/*
  Project Name: GDP- Gathering Detection Platform
  File Name: WebappApplicationTests.java
  Author: Emma Roveroni
  Creation Date: 2021-04-12
  Summary: the file is the repository that extends MongoRepository 
  Last change date: 2021-04-13
*/

package com.webapp.data.mongodb.DetectionCustomRepositoryImplTest;

import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.List;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.Mockito;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.data.domain.Sort;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;

import com.webapp.spring.data.mongodb.customRepository.DetectionCustomRepositoryImpl;
import com.webapp.spring.data.mongodb.model.Detection;

@ExtendWith(MockitoExtension.class)
public class DetectionCustomRepositoryImplTest {

  private DetectionCustomRepositoryImpl underTest;
  private @Mock MongoTemplate mongoTemplate;
  
  @BeforeEach
  public void setup() {
	  underTest = new DetectionCustomRepositoryImpl(mongoTemplate);
  }
  
  @AfterEach
  public void reset() {
	  Mockito.reset(mongoTemplate);
  }

  @Test
  public void getCitiesTest() {
    List<String> cities = new ArrayList<>();
    cities.add("Fake1");
    cities.add("Fake2");
    when(mongoTemplate.findDistinct("city", Detection.class, String.class)).thenReturn(cities);
    underTest.getCities();
    verify(mongoTemplate).findDistinct("city", Detection.class, String.class);
  }
  
  @Test
  public void getLastValueTest() throws Exception {
    String city = "Fake1";
	Query query = new Query();
	query.addCriteria(Criteria.where("city").is(city));
    query.limit(1);
    query.with(Sort.by("time").descending());
	List<Detection> lastValue = new ArrayList<>();
	lastValue.add(new Detection());
	when(mongoTemplate.find(query, Detection.class, "detection")).thenReturn(lastValue);
	underTest.getLastValue(city);
	verify(mongoTemplate).find(query, Detection.class, "detection");
  }
  
  @Test
  public void getDataRTTest() throws Exception {
	  String date = "2021-04-16T10";
	  String city = "Fake1";
	  String temptime = date.substring(date.length() - 2);
      String tempDate = date.substring(0, date.length() - 2);
      int temp = Integer.valueOf(temptime);
      temp = temp - 1;
      String t;
      if (temp < 10) {
          t = "0" + temp;
      } else {
          t = Integer.toString(temp);
      }
      tempDate = tempDate + t;
      Query query = new Query();
      DateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd'T'HH");
      query.addCriteria(Criteria.where("date").lte(dateFormat.parseObject(date)));
      query.addCriteria(Criteria.where("time").gte(dateFormat.parseObject(tempDate)));
      query.addCriteria(Criteria.where("city").is(city));
      query.addCriteria(Criteria.where("type").is(0));
      query.with(Sort.by("time").descending());
      query.limit(1);
      List<Detection> numPeople = new ArrayList<>();
  	  when(mongoTemplate.find(query, Detection.class, "detection")).thenReturn(numPeople);
  	  underTest.getDataRT(city , date);
  	  verify(mongoTemplate).find(query, Detection.class, "detection");
  }
  
  
  @Test
  public void getLatLngsTest() {
	  String city = "Fake1";
	  Query query = new Query(Criteria.where("city").is(city));
	  List<Double> lat = new ArrayList<>();
	  when(mongoTemplate.findDistinct(query, "latitude", Detection.class, Double.class)).thenReturn(lat);
  	  underTest.getLatLngs(city);
  	  verify(mongoTemplate).findDistinct(query, "latitude", Detection.class, Double.class);
      
  }
}