/*
  Project Name: GDP- Gathering Detection Platform
  File Name: WebappApplicationTests.java
  Author: Emma Roveroni
  Creation Date: 2021-04-12
  Summary: the file containes all the unit tests.
  Last change date: 2021-05-12
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
    
  	  String startDate = "2021-04-16T10";
  	  String city = "Fake1";

  	  String temptime = startDate.substring(startDate.length() - 2);
      String tempDate = startDate.substring(0, startDate.length() - 2);
      int temp = Integer.valueOf(temptime);
      temp = temp + 1;

     

      String t;
      if (temp < 10) {
          t = "0" + temp;
      } else {
          t = Integer.toString(temp);
      }
      tempDate = tempDate + t;

      Query query = new Query();
      String testDate = startDate;
      startDate = startDate + ":00:00.000-0000";
      tempDate = tempDate + ":00:00.000-0000";

      DateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss.SSSZ");
      query.addCriteria(Criteria.where("date").lte(dateFormat.parseObject(tempDate)));
      query.addCriteria(Criteria.where("time").gte(dateFormat.parseObject(startDate)));
      query.addCriteria(Criteria.where("city").is(city));
      query.addCriteria(Criteria.where("type").is(0));
      query.with(Sort.by("time").descending());
      query.limit(1);

      List<Detection> numPeople = new ArrayList<>();
  	  when(mongoTemplate.find(query, Detection.class, "detection")).thenReturn(numPeople);
  	  underTest.getDataRT(city , testDate);
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

  @Test
  public void getCityByIdTest() {
    String i = "1";
    int x = Integer.parseInt(i);
    Query query = new Query(Criteria.where("id_webcam").is(x));
    List<String> cities = new ArrayList<>();
    when(mongoTemplate.findDistinct(query,"city", Detection.class, String.class)).thenReturn(cities);
    underTest.getCityById(i);
    verify(mongoTemplate).findDistinct(query, "city", Detection.class, String.class);
  }


  
  @Test
  public void getAllValueTest() throws Exception {
    String city = "Fake1";
    Query query = new Query();
    query.addCriteria(Criteria.where("city").is(city));
    query.with(Sort.by("time").descending());
    List<Detection> AllValue = new ArrayList<>();
    AllValue.add(new Detection());
    when(mongoTemplate.find(query, Detection.class, "detection")).thenReturn(AllValue);
    underTest.getAllValue(city);
    verify(mongoTemplate).find(query, Detection.class, "detection");
  }


}
