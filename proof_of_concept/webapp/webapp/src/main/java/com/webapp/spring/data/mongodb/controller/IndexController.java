/*
  Project Name: GDP- Gathering Detection Platform
  File Name: IndexController.java
  Author: Emma Roveroni
  Creation Date: 2021-03-07
  Summary: the file containes all the http request
  Last change date: 2021-05-12
*/
package com.webapp.spring.data.mongodb.controller;

import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.webapp.spring.data.mongodb.model.Detection;
import com.webapp.spring.data.mongodb.customRepository.DetectionCustomRepository;

@CrossOrigin(origins = "http://localhost:8081")
@RestController
@RequestMapping("/api")
@Service
public class IndexController {

    private DetectionCustomRepository detectionCustomRepository;

    @Autowired
    public IndexController(DetectionCustomRepository detectionCustomRepository) {
        this.detectionCustomRepository = detectionCustomRepository;
    }

    @GetMapping("/city")
    public ResponseEntity<List<String>> fetchCity() {
        return new ResponseEntity<>(detectionCustomRepository.getCities(), HttpStatus.OK);
    }

    @GetMapping("/coo/{city}")
    public ResponseEntity<List<List<Double>>> fetchCoo(@PathVariable("city") String city) {
        return new ResponseEntity<>(detectionCustomRepository.getLatLngs(city), HttpStatus.OK);
    }

    @GetMapping("/RT/{city}/{date}")
    public ResponseEntity<List<Detection>> fetchDataRT(@PathVariable("city") String city,
            @PathVariable("date") String date) throws Exception {
        return new ResponseEntity<>(detectionCustomRepository.getDataRT(city, date), HttpStatus.OK);
    }

    @GetMapping("/LV/{city}")
    public ResponseEntity<Detection> fetchLastValue(@PathVariable("city") String city) throws Exception {
        return new ResponseEntity<>(detectionCustomRepository.getLastValue(city), HttpStatus.OK);
    }

    @GetMapping("/CityById/{id}")
    public ResponseEntity<List<String>> fetchCityById(@PathVariable("id") String id) throws Exception {
        return new ResponseEntity<>(detectionCustomRepository.getCityById(id), HttpStatus.OK);
    }

    @GetMapping("/AllValue/{city}")
    public ResponseEntity<List<Detection>> fetchAllValue(@PathVariable("city") String city) throws Exception {
        return new ResponseEntity<>(detectionCustomRepository.getAllValue(city), HttpStatus.OK);
    }
}
