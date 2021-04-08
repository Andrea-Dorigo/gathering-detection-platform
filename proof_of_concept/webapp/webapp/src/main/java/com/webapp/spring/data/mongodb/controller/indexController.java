/*
  Project Name: GDP- Gathering Detection Platform
  File Name: indexController.java
  Author: Emma Roveroni
  Creation Date: 2021-03-07
  Summary: the file containes the methods ?? 
  Last change date: 2021-04-01
*/
package com.webapp.spring.data.mongodb.controller;

import com.google.gson.Gson;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.webapp.spring.data.mongodb.model.Detection;
import com.webapp.spring.data.mongodb.repository.CoordinateRepository;

@CrossOrigin(origins = "http://localhost:8081")
@RestController
@RequestMapping("/api")
@Service
public class indexController {

    @Autowired
    CoordinateRepository coordinateRepository;

    @GetMapping("/coordinate")
    public ResponseEntity<List<Detection>>getAllDetection(@RequestParam(required = false) String id) {
        try {
            List<Detection> detec = new ArrayList<Detection>();
            if (id == null) { 
                coordinateRepository.findAll().forEach(detec::add);
            }
            else {
                coordinateRepository.findByIdContaining(id).forEach(detec::add);
            }
            if (detec.isEmpty()) {
                return new ResponseEntity<>(HttpStatus.NO_CONTENT);
            }
            String json = new Gson().toJson(detec);
            return new ResponseEntity<>(detec, HttpStatus.OK);
        }
        catch (Exception e) {
            return new ResponseEntity<>(null, HttpStatus.INTERNAL_SERVER_ERROR);
    }
}

@GetMapping("/city")
    public ResponseEntity<List<String>> fetchCity() {
        return new ResponseEntity<>(coordinateRepository.getCities(),HttpStatus.OK);
 }

@GetMapping("/coo/{city}")
    public ResponseEntity<List<List<Double>>> fetchCoo(@PathVariable("city") String city) {
        return new ResponseEntity<>(coordinateRepository.getLatLngs(city),HttpStatus.OK);
 }
@GetMapping("/RT/{city}/{date}")
public ResponseEntity<List<Detection>> fetchDataRT(@PathVariable("city") String city,@PathVariable("date") String date ) {
    return new ResponseEntity<>(coordinateRepository.getDataRT(city,date),HttpStatus.OK);
 }
}
