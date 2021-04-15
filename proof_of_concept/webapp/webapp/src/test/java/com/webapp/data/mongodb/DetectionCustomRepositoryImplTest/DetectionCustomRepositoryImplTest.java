/*
  Project Name: GDP- Gathering Detection Platform
  File Name: WebappApplicationTests.java
  Author: Emma Roveroni
  Creation Date: 2021-04-12
  Summary: the file is the repository that extends MongoRepository 
  Last change date: 2021-04-13
*/

package com.webapp.data.mongodb.DetectionCustomRepositoryImplTest;

import static org.mockito.ArgumentMatchers.anyList;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.Mockito;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.data.mongodb.core.MongoTemplate;

import com.webapp.spring.data.mongodb.customRepository.DetectionCustomRepositoryImpl;
import com.webapp.spring.data.mongodb.model.Detection;

@ExtendWith(MockitoExtension.class)
public class DetectionCustomRepositoryImplTest {

  private DetectionCustomRepositoryImpl dcri;
  private @Mock MongoTemplate mongoTemplate;
  
  @BeforeEach
  public void setup() {
    dcri = new DetectionCustomRepositoryImpl();
  }
  
  @AfterEach
  public void reset() {
	  Mockito.reset(dcri, mongoTemplate);
  }

  @Test
  public void getCitiesTest() {
    when(mongoTemplate.findDistinct("city", Detection.class, String.class)).thenReturn(anyList());
    dcri.getCities();
    verify(mongoTemplate).findDistinct("city", Detection.class, String.class);
  }
}