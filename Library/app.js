const express = require('express');

const app = express();

const fs = require("fs");
   
app.use(express.json())
var books = {}


const readData = () => {
    fs.readFile("books.json", function(err, data) {
        
        if (err) throw err;
        
        books = JSON.parse(data);
        
    });
    
}
readData()
const writeData = () => {
    fs.writeFile("books.json", JSON.stringify(books), err => {
     
        // Checking for errors
        if (err) throw err; 
       
        console.log("Done writing"); // Success
    });

}


app.post("/list", (req, res) => {
    if(req.body.author){
        let result = books.filter((a) => a.author == req.body.author)
        res.status(200).json({books: result})
    }
    else{
        res.status(200).json({books})
    }
})

app.post("/add", (req, res) => {
    books.push({
        book_name: req.body.book_name,
        author: req.body.author,
        category: req.body.category,
        price: req.body.price,
    })
    writeData()
    res.status(200).json({message: "Added book"})
})

app.post("/delete", (req, res) => {
    books = books.filter(item => item.author !== req.body.author);
    writeData()
    res.status(200).json({message: "Removed book"})
})
 
app.listen(3000, (req, res) => {
    console.log("App is running on port 3000")
})