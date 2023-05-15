// Imports
const express = require("express");
const app = express();
const sqlite3 = require('sqlite3');
const bodyParser = require("body-parser");
const path = require('path');
const port = 3000


// DATABASE CONNECTION
const dbname = path.join(__dirname, "database", "database.db");
const db = new sqlite3.Database(dbname, err => {
    if (err) {
        return console.log(err.message);
    }
    console.log("DATA BASE CONNECTED");
})

// TABLE CREATION

const sql = `CREATE TABLE if not exists exam(project varchar(30),groupnum int,email varchar(60),phone varchar(60),roll varchar(60))`;




db.run(sql, err => {
    if (err) {
        return console.log(err.message);
    }
    console.log("TABLE ADDED IN THE DATABASE");
})
app.use(bodyParser.urlencoded({ extended: true }));

// Static Files
app.use(express.static('public'));

// Set Views
app.set('view engine', 'ejs');
app.set('views', './views');

// GET
app.get("/", function (req, res) {
    res.render('index');
});

app.get("/tabledata", function (req, res) {
    db.all(`select * from exam`, [], (err, rows) => {
        if (err) {
            console.log(err.message);
        }
        res.render('tabledata', { records: rows });
    })
});

// POST
app.post("/tabledata", function (req, res) {

    var data1 = (req.body.project);
    var data2 = (req.body.groupnum);
    var data3 = (req.body.email);
    var data4 = (req.body.phone);
    var data5 = (req.body.roll);



    let data_insert = `insert into exam(project, groupnum, email,phone,roll) values(?,?,?,?,?)`;

    db.run(data_insert, [data1, data2, data3, data4, data5], err => {
        if (err) {
            return console.log(err.message);
        }
        console.log(data2);
        console.log("DATA INSERTED");
    })
    res.redirect('/tabledata')
});


app.listen(port, function () {
    console.log("server is runnig on the port 3000");
});