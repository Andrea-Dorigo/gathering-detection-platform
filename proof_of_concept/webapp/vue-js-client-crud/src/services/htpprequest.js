import http from "../http-common";

class Elements {
    getCoordinate() {
        return http.get("/coordinate");
    }
    getCities() {
        return http.get('/city');
    }
}

export default new Elements();