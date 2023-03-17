const express = require("express");
const bodyparser = require("body-parser");
const app = express();

app.use(bodyparser.urlencoded({extended: true}));
app.get("/", function(req,res){
    res.sendFile(__dirname + "/index.html");
});

app.post("/",function(req,res){
    req.send("Thanks for posting");
    var num1 = Number(req.body.num1);
    var num2 = Number(req.body.num2);
    var result = num1 + num2;
    req.send("The result is " + result);
});

app.get("/bmicalculator", function(req,res){
    res.sendFile(__dirname + "/bmi-calculator.html")
})

app.post("/bmicalculator", function(req,res){
    var weight = parseFloat(req.body.weight);
    var height = parseFloat(req.body.height);
    var bmi = weight/(height*height);
    res.send("Your BMI is "+ bmi);
})
app.listen(3000, function(){
    console.log("Server started on port 3000");
});
