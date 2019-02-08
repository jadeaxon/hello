module.exports = function (grunt) {

    'use strict';

    grunt.initConfig({
        serve: {
            options: {
                port: 9000
            }
        }

    });

    grunt.loadNpmTasks('grunt-serve');


    grunt.registerTask('default', ['serve']);
};
