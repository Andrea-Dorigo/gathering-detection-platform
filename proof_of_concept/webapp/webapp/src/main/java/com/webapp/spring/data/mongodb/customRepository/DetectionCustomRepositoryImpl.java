package com.webapp.spring.data.mongodb.customRepository;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;

import com.webapp.spring.data.mongodb.model.Detection;

public class DetectionCustomRepositoryImpl implements DetectionCustomRepository {
	@Autowired
	MongoTemplate mongoTemplate;

	public List<String> getCities() {

		return mongoTemplate.findDistinct("city", Detection.class, String.class);
	}

	public List<Double> getLatLngs(String city) {
		Query query = new Query(Criteria.where("city").is("Krk"));
		System.out.println(mongoTemplate.findDistinct(query, "latitude", Detection.class, Double.class));
		return mongoTemplate.findDistinct(query, "latitude", Detection.class, Double.class);

	}



}
