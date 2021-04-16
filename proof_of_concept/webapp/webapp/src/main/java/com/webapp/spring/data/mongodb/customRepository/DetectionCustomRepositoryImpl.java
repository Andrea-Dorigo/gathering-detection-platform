/*
  Project Name: GDP- Gathering Detection Platform
  File Name: WebappApplicationTests.java
  Author: Andrea Cecchin
  Creation Date: 2021-03-26
  Summary: the file is the repository that extends MongoRepository
  Last change date: 2021-03-26
*/
package com.webapp.spring.data.mongodb.customRepository;

import java.util.List;
import java.util.ArrayList;

import org.springframework.data.domain.Sort;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.stereotype.Repository;

import java.text.DateFormat;
import java.text.SimpleDateFormat;

import com.webapp.spring.data.mongodb.model.Detection;

@Repository
public class DetectionCustomRepositoryImpl implements DetectionCustomRepository {
    
    private MongoTemplate mongoTemplate;
    
    @Autowired
    public DetectionCustomRepositoryImpl(MongoTemplate mongoTemplate) {
    	this.mongoTemplate = mongoTemplate;
    }

    public List<String> getCities() {
        return mongoTemplate.findDistinct("city", Detection.class, String.class);
    }

    public List<List<Double>> getLatLngs(String city) {
        Query query = new Query(Criteria.where("city").is(city));
        List<Double> lat = mongoTemplate.findDistinct(query, "latitude", Detection.class, Double.class);
        List<Double> lon = mongoTemplate.findDistinct(query, "longitude", Detection.class, Double.class);
        List<List<Double>> cooList = new ArrayList<List<Double>>();
        for (int i = 0; i < lat.size(); i++) {
            List<Double> coo = new ArrayList<Double>();
            coo.add(lat.get(i));
            coo.add(lon.get(i));
            cooList.add(coo);
        }
        return cooList;
    }

    public List<Detection> getDataRT(String city, String startDate) throws Exception {
        String temptime = startDate.substring(startDate.length() - 2);
        String tempDate = startDate.substring(0, startDate.length() - 2);
        int temp = Integer.valueOf(temptime);
        temp = temp - 1;
        String t;
        if (temp < 10) {
            t = "0" + temp;
        } else {
            t = Integer.toString(temp);
        }
        tempDate = tempDate + t;
       
        Query query = new Query();
        DateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd'T'HH");
        query.addCriteria(Criteria.where("date").lte(dateFormat.parseObject(startDate)));
        query.addCriteria(Criteria.where("time").gte(dateFormat.parseObject(tempDate)));
        query.addCriteria(Criteria.where("city").is(city));
        query.addCriteria(Criteria.where("type").is(0));
        query.with(Sort.by("time").descending());
        query.limit(1);
        List<Detection> numPeople = mongoTemplate.find(query, Detection.class, "detection");
        if (numPeople.isEmpty()) {
            Query query1 = new Query();
            query1.addCriteria(Criteria.where("date").lte(dateFormat.parseObject(startDate)));
            query1.addCriteria(Criteria.where("time").gte(dateFormat.parseObject(tempDate)));
            query1.addCriteria(Criteria.where("city").is(city));
            query1.addCriteria(Criteria.where("type").is(1));
            query1.with(Sort.by("time").descending());
            query1.limit(1);
            numPeople = mongoTemplate.find(query1, Detection.class, "detection");
        }
        return numPeople;
    }

    public Detection getLastValue(String city) throws Exception {
        Query query = new Query();
        query.addCriteria(Criteria.where("city").is(city));
        query.limit(1);
        query.with(Sort.by("time").descending());
        Detection LastValue = mongoTemplate.find(query, Detection.class, "detection").get(0);
        return LastValue;
    }
}
