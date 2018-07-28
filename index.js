const http = require('http');
var express = require('express');
var app = express()
var MongoClient = require('mongodb').MongoClient,
  test = require('assert');
var url = 'mongodb+srv://admin:1234@cluster0-mr1r8.mongodb.net/PrescriptPal?retryWrites=true'
var path = require('path');

var server = app.listen(8080, function(){
  console.log('listening to requests on 8080');
})

app.use(express.static(path.join(__dirname, '/public')))

app.get('/', (req, res) => {
  console.log('home reached');
  res.sendFile(path.join(__dirname + "/public/index.html"));
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
