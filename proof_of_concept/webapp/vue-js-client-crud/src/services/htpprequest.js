import http from "../http-common";

class Elements {
    getCoordinate() {
        return http.get("/coordinate");
    }
    getCities() {
        return http.get('/city');
    }
    getCoo() {
        return http.get("/coo");
    }
}

export default new Elements();
