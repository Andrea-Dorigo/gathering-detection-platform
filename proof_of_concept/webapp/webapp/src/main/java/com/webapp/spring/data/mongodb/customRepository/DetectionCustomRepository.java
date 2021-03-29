package com.webapp.spring.data.mongodb.customRepository;
import java.util.List;

public interface DetectionCustomRepository {
	public List<String> getCities();
	public List<List<Double>> getLatLngs(String city);
}
