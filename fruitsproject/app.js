const mongoose = require("mongoose");
mongoose.set("strictQuery", true);
mongoose.connect("mongodb://127.0.0.1/fruitsDB");

const fruitSchema = new mongoose.Schema({
  name: {
    type: String,

  },
  rating: {
    type: Number,
    min: 1,
    max: 10,
  },
  review: String,
});

const Fruit = mongoose.model("Fruit", fruitSchema);

//const fruit = new Fruit({
//  rating: 10,
//  review: "Peaches are cute",
//});

//fruit.save();
//Fruit.insertMany([apple, banene, apepe], function (err) {
//  if (err) {
//    console.log(err);
//  } else {
//    console.log("Good");
//  }
//});

Fruit.find(function (err, fruits) {
  if (err) {
    console.log(err);
  } else {
    mongoose.connection.close;
    fruits.forEach(function (fruit) {
      console.log(fruit.name);
    });
  }
});

//Fruit.updateOne({_id: "6396aeb5b79557a55784bbf5"}, {name:"Peach"}, function(err){
//   if(err){
//      console.log(err);
//   } else {
//      console.log("Successfully updated the document.");
//   }
//});

//Fruit.deleteOne({name: "Peach"}, function(err){
//   if(err){
//      console.log(err);
//   } else {
//      console.log("Successfully deleted!! No evidence remaining!!");
//   }
//});

//Fruit.deleteMany({name: "Apple"}, function(err){
//   if(err){
//      console.log(err);
//   } else {
//      console.log("Successfully deleted!! No evidence remaining!!");
//   }
//});

const personSchema = new mongoose.Schema({
   name: String,
   age: Number,
   favouriteFruit: fruitSchema
});

const Person = mongoose.model("Person", personSchema);

const pineapple = new Fruit({
   name: "Pineapple",
   score: 9,
   review: "Fruit"
});

pineapple.save();

const person = new Person({
   name: "Amy",
   age: 12,
   favouriteFruit: pineapple
});

person.save();  