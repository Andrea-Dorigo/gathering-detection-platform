 /* eslint no-use-before-define: 0 */
export const getTime = {
    getTime: function () {
        var methodurl;
        methodurl = "/coordinate";
        var map;
        // eslint-disable-next-line no-undef
        $.ajax({
            type: 'GET',
            url: methodurl,
            dataType: 'json',
            success: function (data) {
                map.remove();
                var dataToString = JSON.stringify(data);
                var datatext = '{"webcam":' + dataToString + '}';
                var test = JSON.parse(datatext);
                var t = document.getElementById("myRange").value;
                var ore;
                var s;
                var k = Object.keys(test.webcam).length;
                for (var i = 0; i < k; i++) {
                    s = test.webcam[i].time;
                    ore = s.split(".");
                    if (ore[0] == t) {
                        break;
                    }
                }
                if (i == test.webcam.length) {
                    document.getElementById("myRange").value = t;
                    document.getElementById("range").textContent = t;
                    alert("Non ci sono dati disponibili per questa fascia oraria");
                    this.loadEmptyMap();
                }
                else {
                    var r = test.webcam[i].time;
                    r = r.split(".");
                    document.getElementById("myRange").value = r[0];
                    document.getElementById("range").textContent = r[0];
                    this.loadMapByTime(test, i);
                }
            }
        });
    }
}