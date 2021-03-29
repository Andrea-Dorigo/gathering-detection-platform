package com.webapp.spring.data.mongodb.customRepository;
import java.util.List;

public interface DetectionCustomRepository {
	public List<String> getCities();
	public List<String> getLatLngs(String city);
}
