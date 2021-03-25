package controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import com.google.gson.Gson;

import model.detection;
import repository.CoordinateRepository;

@CrossOrigin(origins = "*")
@RestController
@RequestMapping("/api")
public class indexController {

	@Autowired
	private CoordinateRepository coordinaterepository;

	@GetMapping("/coordinate")
	public @ResponseBody String jsonRetr() throws Exception {
		List<detection> coordinate = coordinaterepository.findAll();
		Gson gson = new Gson();
		String jsonString = gson.toJson(coordinate);
		return jsonString;
	}

}
