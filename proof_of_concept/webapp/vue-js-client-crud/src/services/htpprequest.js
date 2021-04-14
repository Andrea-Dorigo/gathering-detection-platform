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
}

export default new Elements();
