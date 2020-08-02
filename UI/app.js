var http = require('http');
var formidable = require('formidable');
var fs = require('fs');
var openTab = require('open-new-tab')
var bodyParser  = require("body-parser");
const { exec } = require('child_process');
var express = require("express");
var app = express();


app.use(bodyParser.urlencoded({extended: true}));
app.set("view engine", "ejs");
app.use(express.static('./'));


const PORT=8080; 


app.get("/", function(req, res){
  res.render("landing"); 
});

app.get("/cluster", function(req, res){
  res.render("cluster"); 
});

app.get("/view3d", function(req, res){
  res.render("view3d"); 
});

app.get("/predictions", function(req, res){
  res.render("predictions"); 
});

app.get("/predview3dall", function(req, res){
  res.render("predview3dall"); 
});

app.get("/cluster/:map", function(req, res){
  var fname=req.params.map;
  // console.log(fname);
  res.render("maps/"+fname); 
});

app.post("/2D", function(req, res){
  var fname=req.body.key;
  console.log(fname);
  var command="python3 plt.py "+fname;
  exec(command, (err, stdout, stderr) => {
    if (err) {
      console.error(err);
      return;
    }
    res.json({ ok: true }); 
  });  
});

app.post("/3D", function(req, res){
  var fname=req.body.key;
  console.log(fname);
  var command="python view3d.py "+fname;
  exec(command, (err, stdout, stderr) => {
    if (err) {
      console.error(err);
      return;
    }
    res.json({ ok: true }); 
  });  
});



app.get("/predictedmaps/:map", function(req, res){
  var fname=req.params.map;
  // console.log(fname);
  res.render("predictedmaps/"+fname); 
});

app.post("/2dp", function(req, res){
  var fname=req.body.key;
  var command="python3 pltpred.py "+fname;
  exec(command);
  res.json({ ok: true });   
});

app.post("/3dp", function(req, res){
  var fname=req.body.key;
  console.log(fname);
  var command1="python merge.py "+fname;
  var command2="python predview3d.py "+fname;
  exec(command1, (err, stdout, stderr) => {
    if (err) {
      console.error(err);
      return;
    }
    exec(command2, (err, stdout, stderr) => {
      if (err) {
        console.error(err);
        return;
      }
    }); 
    res.json({ ok: true }); 
  }); 
});

app.listen(PORT, process.env.IP, function(){
  console.log("The Server Has Started!");
});


