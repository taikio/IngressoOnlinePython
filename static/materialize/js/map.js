/**
 * Created by Welker on 10/10/2015.
 */

var map;
var markerList = [];
function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {
            lat: 37.7577,
            lng: -122.4376
        },
        mapTypeControlOptions: {
            style: google.maps.MapTypeControlStyle.DROPDOWN_MENU
        },
        zoom: 12,
        scrollwheel: false
    });


    var objectList = [];

    var marker;

    var object1 = ({
        name : "Toreba Taxi",
        desc : "Trabalhamos 24 horas para te servir",
        lat  : 37.7577,
        lng  : -122.4376,
        icon : 'img/MapMarkers/ion-model-s.png'

    });

    var object2 = ({
        name : "Transporte da quebrada",
        desc : "Aque é correria",
        lat  : 37.757720,
        lng  : -122.41705,
        icon : 'img/MapMarkers/ion-model-s.png'
    });

    var object3 = ({
        name : "Lux Cars",
        desc : "Os melhores veículos a sua disposição",
        lat  : 37.759327,
        lng  : -122.412558,
        icon : 'img/MapMarkers/ion-model-s.png'
    });



    objectList.push(object1);
    objectList.push(object2);
    objectList.push(object3);
    // limpa o mapa... ou tenta kkk
    for(var m in markerList) {
        m.setMap(null);
    }

    markerList = [];
    // carrega o mapa, preenche o array de markers e ativa o clusterer
    $.each(objectList, function (i, data) {

        marker = new google.maps.Marker({
            position: new google.maps.LatLng(data.lat, data.lng),
            map: map,
            title: data.name,
            icon: data.icon,
            animation: google.maps.Animation.DROP
        });


        // evento que chama o modal
        google.maps.event.addListener(marker, 'click', function () {


            // função que abre o modal e insere as informações
            openModalInfo(data.name,data.desc);

        });
        markerList.push(marker);

        var markerCluster = new MarkerClusterer(map, markerList);

    });

}

function initVeiculosCategory() {
    var objectList = [];

    var marker;

    var object1 = ({
        name : "Toreba Taxi",
        desc : "Trabalhamos 24 horas para te servir",
        lat  : 37.7577,
        lng  : -122.4376,
        icon : 'img/MapMarkers/ion-model-s.png'

    });

    var object2 = ({
        name : "Transporte da quebrada",
        desc : "Aque é correria",
        lat  : 37.757720,
        lng  : -122.41705,
        icon : 'img/MapMarkers/ion-model-s.png'
    });

    var object3 = ({
        name : "Lux Cars",
        desc : "Os melhores veículos a sua disposição",
        lat  : 37.759327,
        lng  : -122.412558,
        icon : 'img/MapMarkers/ion-model-s.png'
    });



    objectList.push(object1);
    objectList.push(object2);
    objectList.push(object3);
    // limpa o mapa... ou tenta kkk
    for(var m in markerList) {
        m.setMap(null);
    }

    markerList = [];
    // carrega o mapa, preenche o array de markers e ativa o clusterer
    $.each(objectList, function (i, data) {

        marker = new google.maps.Marker({
            position: new google.maps.LatLng(data.lat, data.lng),
            map: map,
            title: data.name,
            icon: data.icon,
            animation: google.maps.Animation.DROP
        });


        // evento que chama o modal
        google.maps.event.addListener(marker, 'click', function () {


            // função que abre o modal e insere as informações
            openModalInfo(data.name,data.desc);

        });
        markerList.push(marker);

        var markerCluster = new MarkerClusterer(map, markerList);

    });
}

function initPontosTuristicosCategory() {
    var objectList = [];

    var marker;

    var object1 = ({
        name : "dajf",
        desc : "Trabalhamos 24 horas para te servir",
        lat  : 37.7584,
        lng  : -122.4476,
        icon: 'img/MapMarkers/ion-earth.png'

    });

    var object2 = ({
        name : "kdjfaoidjf",
        desc : "Aque é correria",
        lat  : 37.757754,
        lng  : -122.417058,
        icon: 'img/MapMarkers/ion-earth.png'
    });

    var object3 = ({
        name : "djfoiajdf",
        desc : "Os melhores veículos a sua disposição",
        lat  : 37.759327,
        lng  : -122.412558,
        icon: 'img/MapMarkers/ion-earth.png'
    });



    objectList.push(object1);
    objectList.push(object2);
    objectList.push(object3);


    if(markerList != 0 || markerList != null){


            for (var i = 0; i < markerList.length; i++ ) {
                markerList[i].setMap(null);
            }
            markerList.length = 0;

    }



    $.each(objectList, function (i, data) {

        marker = new google.maps.Marker({
            position: new google.maps.LatLng(data.lat, data.lng),
            map: map,
            title: data.name,
            icon: data.icon,
            animation: google.maps.Animation.DROP
        });



        google.maps.event.addListener(marker, 'click', function () {



            openModalInfo(data.name,data.desc);

        });
        markerList.push(marker);

        var markerCluster = new MarkerClusterer(map, markerList);

    });
}

function initServicosCategory() {
    var markerList = [];
    var marker;
    var myLatLng;

    myLatLng = [
        {"lat": 37.7587,"lng": -122.4186},
        {"lat": 37.754720,"lng": -122.417453},
        {"lat": 37.756327,"lng": -122.412558},
        {"lat": 37.755857,"lng": -122.415315}
    ];
    $.each(myLatLng,function(i,pos){

        marker = new google.maps.Marker({
            position: new google.maps.LatLng(pos.lat,pos.lng),
            map: map,
            title: 'Hello World!',
            icon: 'img/MapMarkers/ion-android-hand.png',
            animation: google.maps.Animation.DROP
        });
        markerList.push(marker);

    });

    var markerCluster = new MarkerClusterer(map, markerList);

}

function initAlimentacaoCategory() {
    var markerList = [];
    var marker;
    var myLatLng;

    myLatLng = [
        {"lat": 37.7877, "lng": -122.4377},
        {"lat": 37.767720, "lng": -122.417055},
        {"lat": 37.749327, "lng": -122.412559},
        {"lat": 37.729857, "lng": -122.415014}
    ];
    $.each(myLatLng, function (i, pos) {

        marker = new google.maps.Marker({
            position: new google.maps.LatLng(pos.lat, pos.lng),
            map: map,
            title: 'Hello World!',
            icon: 'img/MapMarkers/ion-fork.png',
            animation: google.maps.Animation.DROP
        });
        markerList.push(marker);

    });

    var markerCluster = new MarkerClusterer(map, markerList);

}

function initClassificadosCategory() {
    var markerList = [];
    var marker;
    var myLatLng;

    myLatLng = [
        {"lat": 37.7357,"lng": -122.4376},
        {"lat": 37.756520,"lng": -122.427053},
        {"lat": 37.757827,"lng": -122.442558},
        {"lat": 37.754757,"lng": -122.455015}
    ];
    $.each(myLatLng,function(i,pos){

        marker = new google.maps.Marker({
            position: new google.maps.LatLng(pos.lat,pos.lng),
            map: map,
            title: 'Hello World!',
            icon: 'img/MapMarkers/ion-paper.png',
            animation: google.maps.Animation.DROP
        });
        markerList.push(marker);

    });

    var markerCluster = new MarkerClusterer(map, markerList);

}

function initRedesSociaisCategory() {
    var markerList = [];
    var marker;
    var myLatLng;

    myLatLng = [
        {"lat": 37.7337,"lng": -122.4376},
        {"lat": 37.754720,"lng": -122.417053},
        {"lat": 37.796927,"lng": -122.412558},
        {"lat": 37.768157,"lng": -122.415015}
    ];
    $.each(myLatLng,function(i,pos){

        marker = new google.maps.Marker({
            position: new google.maps.LatLng(pos.lat,pos.lng),
            map: map,
            title: 'Hello World!',
            icon: 'img/MapMarkers/ion-person-stalker.png',
            animation: google.maps.Animation.DROP
        });
        markerList.push(marker);

    });

    var markerCluster = new MarkerClusterer(map, markerList);

}

function openModalInfo(nome,descricao){

    var string = "";

    string = '<h4>'+nome+'</h4>'+
        '<p>'+descricao+'</p>';

    $('.modal-content').html(string);

    $('#modal1').openModal();
}
