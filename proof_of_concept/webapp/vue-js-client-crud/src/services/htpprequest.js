import http from "../http-common";

class Elements {
    getCoordinate() {
        return http.get("/coordinate");
    }
    getCities() {
        return http.get("/city");
    }
    getCoo(city) {
        return http.get(`/coo/${city}`);
    }
    getDataRT(city, date) {
        return http.get(`/RT/${city}/${date}`);
    }
}

export default new Elements();