import http from "../http-common";

class Elements {
    getCoordinate() {
        return http.get("/coordinate");
    }
    getCities() {
        return http.get('/testCity');
    }
}

export default new Elements();