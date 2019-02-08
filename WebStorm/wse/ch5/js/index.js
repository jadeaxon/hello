/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */
var app = {
    // Application Constructor
    initialize: function() {
        this.bindEvents();
    },
    // Bind Event Listeners
    //
    // Bind any events that are required on startup. Common events are:
    // 'load', 'deviceready', 'offline', and 'online'.
    bindEvents: function() {
        document.addEventListener('deviceready', this.onDeviceReady, false);
    },
    // deviceready Event Handler
    // Listen to the online and resume events and load the Google Maps API
    // The scope of 'this' is the event. In order to call the 'receivedEvent'
    // function, we must explicitly call 'app.receivedEvent(...);'
    onDeviceReady: function () {
        app.receivedEvent('deviceready');
        document.addEventListener("online", app.loadGoogleMapsAPI, false);
        document.addEventListener("resume", app.loadGoogleMapsAPI, false);
        app.loadGoogleMapsAPI();
    },
    // Load the Maps API if it wasn't loaded before
    loadGoogleMapsAPI: function () {
        if (window.google !== undefined && window.google.maps) {
            return;
        }
        // load maps api
        $.getScript('https://maps.googleapis.com/maps/api/js?sensor=true&callback=app.onMapsApiLoaded');
    },
    // Get the location after we have the maps api
    // We are going to get the default location and also watch for any changes in the location
    onMapsApiLoaded: function(){
        navigator.geolocation.getCurrentPosition(app.geolocationSuccess, app.geolocationError, app.geolocationOptions);
        navigator.geolocation.watchPosition(app.geolocationSuccess, app.geolocationError, app.geolocationOptions);
    },
    // Load the map with the device positon
    geolocationSuccess: function(position){
        app.position = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
        app.updatePosition();

    },
    // If we don't have a position from the device we are going to use some default values
    geolocationError: function(error){
        if(!app.position){
            app.defaultPosition = new google.maps.LatLng(51.5, -0.1);
            app.updatePosition();
        }
    },
    // Settings object for the geolocation
    geolocationOptions: {
        maximumAge: 3000,
        timeout: 5000,
        enableHighAccuracy: true
    },
    // Show the map and update the position
    updatePosition: function(pos){
        $('.app').hide();
        $('#map').show();
        var mapOptions = {
            zoom: 10
        };
        var pos = app.position || app.defaultPosition;
        var map = new google.maps.Map(document.getElementById('map'), mapOptions);
        var infowindow = new google.maps.InfoWindow({
            map: map,
            position: pos,
            content: 'I am here!'
        });
        map.setCenter(pos);
    },
    // Update DOM on a Received Event
    receivedEvent: function(id) {
        var parentElement = document.getElementById(id);
        var listeningElement = parentElement.querySelector('.listening');
        var receivedElement = parentElement.querySelector('.received');

        listeningElement.setAttribute('style', 'display:none;');
        receivedElement.setAttribute('style', 'display:block;');

        console.log('Received Event: ' + id);
    }
};
