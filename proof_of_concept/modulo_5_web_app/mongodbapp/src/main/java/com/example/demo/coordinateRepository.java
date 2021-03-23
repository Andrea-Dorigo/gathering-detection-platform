package com.example.demo;

import org.springframework.data.mongodb.repository.MongoRepository;

import com.example.demo.Detection;

public interface coordinateRepository extends MongoRepository<Detection, String>{
	Detection findFirstById(String id);
}
