package com.webapp.spring.data.mongodb.customRepository;
import java.util.List;
import java.util.ArrayList;

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

	public List<List<Double>> getLatLngs(String city) {
		Query query = new Query(Criteria.where("city").is(city));
		List<Double> lat = mongoTemplate.findDistinct(query, "latitude", Detection.class, Double.class);
        List<Double> lon = mongoTemplate.findDistinct(query, "longitude", Detection.class, Double.class);
		List<List<Double>> cooList = new ArrayList<List<Double>>();
		for(int i=0;i<lat.size();i++) {
			List<Double> coo = new ArrayList<Double>();
			coo.add(lat.get(i));
			coo.add(lon.get(i));
			cooList.add(coo);
		}
        return cooList;
	}
}
