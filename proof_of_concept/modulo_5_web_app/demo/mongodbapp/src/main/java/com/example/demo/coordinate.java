package com.example.demo;
import org.springframework.data.annotation.Id;

public class coordinate {

	    @Id
	    private String id;
		public String place;
		public float lat;
		public float lon;
		public int people;
		
		public coordinate(String id, String place, float lat, float lon, int people) {
			super();
			this.id = id;
			this.place = place;
			this.lat = lat;
			this.lon = lon;
			this.people = people;
		}
		public String getId() {
			return id;
		}
		public void setId(String id) {
			this.id = id;
		}
		public String getPlace() {
			return place;
		}
		public void setPlace(String place) {
			this.place = place;
		}
		public float getLat() {
			return lat;
		}
		public void setLat(float lat) {
			this.lat = lat;
		}
		public float getLon() {
			return lon;
		}
		public void setLon(float lon) {
			this.lon = lon;
		}
		public int getPeople() {
			return people;
		}
		public void setPeople(int people) {
			this.people = people;
		}
		@Override
		public String toString() {
			return "coordinate [id=" + id + ", place=" + place + ", lat=" + String.valueOf(lat) + ", lon=" + String.valueOf(lon) + ", people=" + people
					+ "]";
		}
}
	
