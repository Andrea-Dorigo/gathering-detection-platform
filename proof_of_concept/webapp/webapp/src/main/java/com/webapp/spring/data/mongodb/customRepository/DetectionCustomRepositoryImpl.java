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
	 
	public List<String> getAllCity() {
		Criteria criteria = new Criteria();
		criteria.where("id").is("1");
		Query query = new Query();
		query.addCriteria(criteria);
		System.out.println(mongoTemplate.findDistinct("city", Detection.class, String.class));
		
		return mongoTemplate.findDistinct(query, "city", Detection.class, String.class);
	}

}
