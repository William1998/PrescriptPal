const http = require('http');
var express = require('express');
var app = express()
var MongoClient = require('mongodb').MongoClient,
  test = require('assert');

//Using online server rather than local.
var url = 'mongodb+srv://admin:1234@cluster0-mr1r8.mongodb.net/PrescriptPal?retryWrites=true'

//To enable __dirname
var path = require('path');

var server = app.listen(8080, function(){
  console.log('listening to requests on 8080');
})

//Provides the public folder to the client so stylesheets etc can be accessed.
app.use(express.static(path.join(__dirname, '/public')))

//Homepage
app.get('/', (req, res) => {
  console.log('home reached');
  res.sendFile(path.join(__dirname + "/public/index.html"));
})

//Search Page
app.get('/search', (req, res) => {
  console.log('search reached');
  res.sendFile(path.join(__dirname + "/public/searchwithoutlogin.html"));
})

app.get('/rsearch', (req, res) => {
  console.log('rsearch reached');
  res.sendFile(path.join(__dirname + "/public/loginpage.html"));
})

app.get('/rsearch/:reference', (req, res) => {
  var my_param = req.params.reference;
  console.log('search for ' + my_param);
  MongoClient.connect(url, function(err, db){
    if (err) throw err;
    var dbo = db.db('PrescriptPal');
    var query = {reference: myparam};
    dbo.collection('Prescription').find(query).toArray(function(err, result){
      if (err) throw err;
      console.log(JSON.stringify(result));
      db.close();
    })
  })
})

app.get('/search/:name', (req, res) => {
  var my_param = req.params.name;
  console.log('search for ' + my_param);
  MongoClient.connect(url, function(err, db){
    if (err) throw err;
    var dbo = db.db('PrescriptPal');
    //Query to search
    var query = {name: my_param};
    dbo.collection("Medicines").find(query).toArray(function(err, result){
      if (err) throw err;
      console.log(JSON.stringify(result));
      db.close();
    })
  })
})

/*
app.get('/search', (req, res)=> {
  console.log('endpoint reached');
  MongoClient.connect(url, function(err, db){
    if (err) throw err;
    var dbo = db.db('PrescriptPal');
    dbo.collection("Medicines").findOne({}, function(err, result){
      if (err) throw err;
      console.log(result);
      db.close();
    });
  });
})
*/
