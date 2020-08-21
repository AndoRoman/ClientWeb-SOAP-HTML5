//--GEOLOCATION-----//
function GEOLOCATION(){

    function success(pos){
        var crd = pos.coords
        document.querySelector("#lati").value = crd.latitude;
        document.querySelector("#longi").value = crd.longitude;
    }
    navigator.geolocation.getCurrentPosition(success)
}
