import http from "../http-common";

class Elements {
    getCoordinate() {
        console.log(http.get("/coordinate"));
        return http.get("/coordinate");
    }
}

export default new Elements();