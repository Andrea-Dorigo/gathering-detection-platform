package com.example.demo;


import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
//import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import com.google.gson.Gson;

@Controller
public class indexController {

	@Autowired
	private coordinateRepository coordinaterepository;
	
	@RequestMapping("index")
	public String index() {
		return "index.jsp";
	}
	
	@RequestMapping(value = "/coordinate",method = RequestMethod.GET)
	public @ResponseBody String jsonRetr() throws Exception {
		
		List<coordinate> coordinate = coordinaterepository.findAll();
		Gson gson = new Gson();
		String jsonString = gson.toJson(coordinate);
        return jsonString;
    }
	
}

