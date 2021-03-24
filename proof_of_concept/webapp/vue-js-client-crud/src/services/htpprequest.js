import http from "../http-common";

class Elements {
    get() {
        return http.get("/pippo");
    }
}

export default new Elements();