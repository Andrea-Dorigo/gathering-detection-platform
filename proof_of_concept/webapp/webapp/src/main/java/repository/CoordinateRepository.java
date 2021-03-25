package repository;

import org.springframework.data.mongodb.repository.MongoRepository;

import model.detection;

public interface CoordinateRepository extends MongoRepository<detection, String>{
	public detection findFirstById(String id);
}
