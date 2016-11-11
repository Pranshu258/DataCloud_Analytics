// Set Up the server aplication
var express = require('express');
var app = express();
var mongoose = require('mongoose');
var morgan = require('morgan');
var bodyParser = require('body-parser');
var methodOverride = require('method-override');


// Configuration
app.use(express.static(__dirname + '/public'));
app.use(morgan('dev'));
app.use(bodyParser.urlencoded({'extended':'true'}));
app.use(bodyParser.json());
app.use(bodyParser.json({ type: 'application/vnd.api+json' }));
app.use(methodOverride());

// ================================================================================================

// Front End Application Route
app.get('*', function(req, res) {
	res.sendFile('./public/index.html');
});

// Listen 
app.listen(8080);
console.log("App listening on port 8080");