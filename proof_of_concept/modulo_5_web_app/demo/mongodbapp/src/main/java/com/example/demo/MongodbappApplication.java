package com.example.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import com.google.gson.*;

import java.util.List;

@SpringBootApplication
public class MongodbappApplication implements CommandLineRunner {

    @Autowired
    private coordinateRepository coordinaterepository;


    public static void main(String[] args) {
        SpringApplication.run(MongodbappApplication.class, args);

    }

    @Override
    public void run(String... args) throws Exception {

    }

}
