package com.webapp.spring.data.mongodb.repository;

import java.util.List;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

import com.webapp.spring.data.mongodb.customRepository.DetectionCustomRepository;
import com.webapp.spring.data.mongodb.model.Detection;

public interface CoordinateRepository extends MongoRepository<Detection, String>, DetectionCustomRepository{
	List<Detection> findByIdContaining(String id);
	/*@Query(value="{}", fields="{_id : 0, id_webcam : 0, city : 1,location : 0, latitude : 0, longitude : 0, numPeople : 0, date : 0, time : 0, type : 0, weather_description : 0, temperature : 0, day_of_week : 0}")
	List<Detection> findCities();*/
}
