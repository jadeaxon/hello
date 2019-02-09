'use strict';

// This module contains all the services within the blog app.
var blogServices = angular.module('blog.services', ['ngResource']);

// The service for dealing with blog posts.
// The built-in $resource service can help consume REST APIs.
blogServices.factory('BlogPost', ['$resource',
    function ($resource) {
        return $resource("http://www.goblog.ulboralabs.com/GolangBlog/blogPost", {}, {
            get: {method: 'GET', cache: false, isArray: false},
            save: {method: 'POST', cache: false, isArray: false},
            update: {method: 'PUT', cache: false, isArray: false},
            delete: {method: 'DELETE', cache: false, isArray: false}
        });
    }]);
