package com.example.demo;
import org.springframework.data.annotation.Id;

public class Detection {

	    @Id
	    private String id;
	    private int id_webcam;
	    public String luogo;
		public float latitude;
		public float longitude;
		public int numPeople;
		public String date;
		public String time;
		
		public Detection(String id, int id_webcam, String luogo, float latitude, float longitude, int numPeople, String date, String time) {
			super();
			this.id = id;
			this.id_webcam = id_webcam;
			this.luogo = luogo;
			this.latitude = latitude;
			this.longitude = longitude;
			this.numPeople = numPeople;
			this.date = date;
			this.time = time;
		}
		public float getId() {
			return id_webcam;
		}
		public void setId(int id_webcam) {
			this.id_webcam = id_webcam;
		}
		public String getPlace() {
			return luogo;
		}
		public void setPlace(String luogo) {
			this.luogo = luogo;
		}
		public float getlatitude() {
			return latitude;
		}
		public void setlatitude(float latitude) {
			this.latitude = latitude;
		}
		public float getlongitude() {
			return longitude;
		}
		public void setlongitude(float longitude) {
			this.longitude = longitude;
		}
		public int getnumPeople() {
			return numPeople;
		}
		public void setnumPeople(int numPeople) {
			this.numPeople = numPeople;
		}
		public void getDate(String date) {
			this.date = date;
		}
		public void setDate(String date) {
			this.date = date;
		}
		public void getTime(String time) {
			this.time = time;
		}
		public void setTime(String time) {
			this.time = time;
		}
		@Override
		public String toString() {
			return "coordinate [id = "+ id +", id_webcam=" + String.valueOf(id_webcam) + ", luogo=" + luogo + ", latitude=" + String.valueOf(latitude) + ", longitude=" + String.valueOf(longitude) + ", numPeople=" + numPeople
					+  ", date=" + date + ",  time=" + time + "]";
		}
}
	
