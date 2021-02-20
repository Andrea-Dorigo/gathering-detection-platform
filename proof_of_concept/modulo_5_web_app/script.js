function initialize(){
    var mymap = L.map('mapid').setView([41.890251, 12.492373], 12);
    /*L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png?{foo}', {
        foo: 'bar',
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(mymap);*/
    L.tileLayer('https://cartodb-basemaps-{s}.global.ssl.fastly.net/light_all/{z}/{x}/{y}{r}.png', {
        attribution: '© OpenStreetMap © CartoDB',
        subdomains: 'abcd',
        maxZoom: 19
    }).addTo(mymap);

    //addressPoints = addressPoints.map(function (p) { return [p[0], p[1]]; });
    console.log(RomaPoints);
    RomaPoints = RomaPoints.map(function (p) { return [p[0], p[1]]; });

    var heat = L.heatLayer(RomaPoints).addTo(mymap);

    /*var heatMapPoints = [];

    var heat = L.heatLayer([41.905697, 12.482327, 0.2], [41.890210, 12.492231, 0.5] , {
        radius: 25,
        minOpacity: 1,
        gradient: {0.4: 'blue', 0.65: 'lime', 1: 'red'}
    }).addTo(mymap);*/
}
