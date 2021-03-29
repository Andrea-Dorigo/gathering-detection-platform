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

	public List<String> getLatLngs(String city){
		Criteria criteria = new Criteria();
		criteria.where("city").is(city);
		Query query = new Query();
        query.addCriteria(criteria);
		query.fields().include("latitude", "longitude").exclude("id", "id_webcam", "city");
        return mongoTemplate.findDistinct(query, ("latitude", "longitude"), Detection.class, String.class);
	}
	
	

}
