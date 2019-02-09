'use strict';

var blogServices = angular.module('blog.services', ['ngResource']);

// Define a client-side AngularJS service that consumes a REST API (a web service).
// This service does work.  You have to use the CorsE plugin in Firefox to disable CORS checking though.
blogServices.factory('$$BlogPost', ['$resource',
    function ($resource) {
        return $resource("http://www.goblog.ulboralabs.com/GolangBlog/blog/:id", {}, {
            get: {method: 'GET', cache: false, isArray: false},
            save: {method: 'POST', cache: false, isArray: false},
            update: {method: 'PUT', cache: false, isArray: false},
            delete: {method: 'DELETE', cache: false, isArray: false}
        });
    }]);

// This service DNE, and the request is getting CORS-blocked anyway.
blogServices.factory('$$BlogList', ['$resource',
    function ($resource) {
        return $resource("http://nodeblog-micbuttoncloud.rhcloud.com/NodeBlog/blogList", {}, {
            get: {method: 'GET', cache: false, isArray: true}            
        });
    }]);
