package model;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "detections")
public class detection {

	    @Id
	    private String id;
	    private int id_webcam;
		private String city;
	    public String location;
		public float latitude;
		public float longitude;
		public int numPeople;
		public String date;
		public String time;
		public int type;
		public String weather_description;
		public float temperature;
		public int day_of_week;
		
		public detection(String id, int id_webcam, String city, String location, float latitude, float longitude,
            int numPeople, String date, String time, int type, String weather_description, float temperature,
            int day_of_week) {
       		super();
			this.id = id;
			this.id_webcam = id_webcam;
			this.city = city;
			this.location = location;
			this.latitude = latitude;
			this.longitude = longitude;
			this.numPeople = numPeople;
			this.date = date;
			this.time = time;
			this.type = type;
			this.weather_description = weather_description;
			this.temperature = temperature;
			this.day_of_week = day_of_week;
    	}

		public String getId() {
			return id;
		}
		public void setId(String id) {
			this.id = id;
		}
		public int getId_webcam() {
			return id_webcam;
		}
		public void setId_webcam(int id_webcam) {
			this.id_webcam = id_webcam;
		}
		public String getCity() {
			return city;
		}
		public void setCity(String city) {
			this.city = city;
		}
		public String getLocation() {
			return location;
		}
		public void setLocation(String location) {
			this.location = location;
		}
		public float getLatitude() {
			return latitude;
		}
		public void setLatitude(float latitude) {
			this.latitude = latitude;
		}
		public float getLongitude() {
			return longitude;
		}
		public void setLongitude(float longitude) {
			this.longitude = longitude;
		}
		public int getNumPeople() {
			return numPeople;
		}
		public void setNumPeople(int numPeople) {
			this.numPeople = numPeople;
		}
		public String getDate() {
			return date;
		}
		public void setDate(String date) {
			this.date = date;
		}
		public String getTime() {
			return time;
		}
		public void setTime(String time) {
			this.time = time;
		}
		public int getType() {
			return type;
		}
		public void setType(int type) {
			this.type = type;
		}
		public String getWeather_description() {
			return weather_description;
		}
		public void setWeather_description(String weather_description) {
			this.weather_description = weather_description;
		}
		public float getTemperature() {
			return temperature;
		}
		public void setTemperature(float temperature) {
			this.temperature = temperature;
		}
		public int getDay_of_week() {
			return day_of_week;
		}
		public void setDay_of_week(int day_of_week) {
			this.day_of_week = day_of_week;
		}
		
		@Override
   		public String toString() {
        return "detection [id=" + id + ", id_webcam=" + id_webcam + ", city=" + city + ", location=" + location
                + ", latitude=" + latitude + ", longitude=" + longitude + ", numPeople=" + numPeople + ", date=" + date
                + ", time=" + time + ", type=" + type + ", weather_description=" + weather_description
                + ", temperature=" + temperature + ", day_of_week=" + day_of_week + "]";
    }
}
	
