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
import org.springframework.data.domain.Sort.Direction;
import org.springframework.data.domain.Sort.Order;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import java.text.DateFormat;
import java.text.SimpleDateFormat;

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
    public List<Detection> getDataRT(String city, String startDate) throws Exception {
        Query query = new Query();
        DateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd'T'HH");
        query.addCriteria(Criteria.where("date").lte(dateFormat.parseObject(startDate)));
        query.addCriteria(Criteria.where("city").is(city));
        query.with(Sort.by("time").descending());
        query.limit(1);
        List<Detection> numPeople = mongoTemplate.find(query, Detection.class, "detection");
        return numPeople;
    }

    public List<Detection> getLastValue(String city) throws Exception {
        Query query = new Query();
        query.limit(1);
        query.with(Sort.by("time").descending());
        List<Detection> LastValue = mongoTemplate.find(query, Detection.class, "detection");
        System.out.println("ultimo valore");
        System.out.println(LastValue);
        return LastValue;
    }

    public List<Integer> getNumPeopleToday(String city, String startDate) throws Exception {
        DateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd'T'HH");
        Query query = new Query();
        query.addCriteria(Criteria.where("date").gte(dateFormat.parseObject(startDate)));
        query.addCriteria(Criteria.where("city").is(city));
        List<Detection> detections = mongoTemplate.find(query, Detection.class, "detection");
        List<Integer> numPeople = new ArrayList<Integer>();
        for(int i=0;i<detections.size();i++) {
          numPeople.add(detections.get(i).getNumPeople());
        }
        return numPeople;
    }
}
