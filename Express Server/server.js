const express = require("express");

const app = express();

app.get("/", function(request, response){
    response.send("<h1>Hellooooooo, yaha kya kar ra hai bhadu, ja ke padai kar na madarchod</h1>");
})

app.get("/contact", function(request, response){
    response.send("<h1>Contact mat karna bhosdike</h1>");
})

app.get("/about", function(request, response){
    response.send("<h1>Tere bap ne banai hai ye website ja aab jake aapni maa chuda</h1>");
})

app.get("/hobbies", function(request, response){
    response.send("<ul><li>Beer</li><li>bakchodi</li></ul>");
})

app.listen(3000, function(){
    console.log("Server started on port 3000");
});
 