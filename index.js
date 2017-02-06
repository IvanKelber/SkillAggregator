let express = require('express'),
    app = express(),
    http = require('http').Server(app),
    io = require('socket.io')(http);

var port = process.env.PORT || 8000
//SET UP STATIC ASSETS FOLDER
app.use(express.static(__dirname + '/static'));

//SERVE HTML AND BEGIN LISTENING
app.get('/', function(req,res) {
  res.sendFile(__dirname + "/html/index.html");
});
http.listen(port,function() {
  console.log("Listening on ",port);
});
