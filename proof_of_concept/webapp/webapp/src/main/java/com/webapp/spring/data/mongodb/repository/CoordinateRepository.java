package com.webapp.spring.data.mongodb.repository;

import java.util.List;

import org.springframework.data.mongodb.repository.MongoRepository;

import com.webapp.spring.data.mongodb.model.Detection;

public interface CoordinateRepository extends MongoRepository<Detection, String>{
	List<Detection> findByIdContaining(String id);
}
