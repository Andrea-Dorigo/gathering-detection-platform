package com.example.demo;

import org.springframework.data.mongodb.repository.MongoRepository;

public interface coordinateRepository extends MongoRepository<coordinate, String>{
	coordinate findFirstById(String id);
}
