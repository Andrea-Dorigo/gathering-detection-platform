package controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
//import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import com.google.gson.Gson;

import model.detection;
import repository.CoordinateRepository;

@CrossOrigin(origins = "http://localhost:8080")
@RestController
@RequestMapping("/api")
public class indexController {

	@Autowired
	private CoordinateRepository coordinaterepository;

	@RequestMapping("index")
	public String index() {
		return "index.jsp";
	}

	@RequestMapping(value = "/coordinate", method = RequestMethod.GET)
	public @ResponseBody String jsonRetr() throws Exception {

		System.out.println(1);
		List<detection> coordinate = coordinaterepository.findAll();
		System.out.println(2);
		Gson gson = new Gson();
		System.out.println(3);
		String jsonString = gson.toJson(coordinate);
		System.out.println(jsonString);
		return jsonString;
	}

}
