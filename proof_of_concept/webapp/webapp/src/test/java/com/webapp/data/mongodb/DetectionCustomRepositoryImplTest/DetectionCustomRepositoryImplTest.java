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
    Query query = new Query();
    query.limit(1);
    query.with(Sort.by("time").descending());
	List<Detection> lastValue = new ArrayList<>();
	when(mongoTemplate.find(query, Detection.class, "detection")).thenReturn(lastValue);
	underTest.getLastValue("Fake1");
	verify(mongoTemplate).find(query, Detection.class, "detection");
  }
  
}