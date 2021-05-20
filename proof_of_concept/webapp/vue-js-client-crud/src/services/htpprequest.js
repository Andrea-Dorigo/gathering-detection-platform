/*jshint esversion: 6 */
import http from "../http-common";

class Elements {
  getCities() {
    return http.get("/city");
  }
  getCoo(city) {
    return http.get(`/coo/${city}`);
  }
  getDataRT(city, date) {
    return http.get(`/RT/${city}/${date}`);
  }
  getLastValue(city) {
    return http.get(`/LV/${city}`);
  }
  getCityById(id) {
    return http.get(`/CityById/${id}`);
  }
  getAllValue(city){
    return http.get(`/AllValue/${city}`)
  }
}

export default new Elements();
