'use strict';

var directory = angular.module("directory", ['ngRoute', 'ngAnimate']);

directory.config(function ($routeProvider) {
	$routeProvider
		.when('/', {
			templateUrl: 'pages/bar.html',
		})
});