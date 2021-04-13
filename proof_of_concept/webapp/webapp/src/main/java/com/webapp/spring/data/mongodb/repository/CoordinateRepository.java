/*
  Project Name: GDP- Gathering Detection Platform
  File Name: CoordinateRepository.java
  Author: Margherita Mitillo
  Creation Date: 2021-03-24
  Summary: the file is the repository that extends MongoRepository 
  Last change date: 2021-04-01
*/
package com.webapp.spring.data.mongodb.repository;

import java.util.List;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

import com.webapp.spring.data.mongodb.customRepository.DetectionCustomRepository;
import com.webapp.spring.data.mongodb.model.Detection;

public interface CoordinateRepository extends MongoRepository<Detection, String>, DetectionCustomRepository {
  List<Detection> findByIdContaining(String id);
}