const express = require('express');
const fs = require('fs');
const path = require('path');
const cors = require("cors");

const app = express();
app.use(cors());
const port = 7575;

const connection = require("./db.js");

app.get('/search', async (req, res) => {
  const { mark, kere, aasta1, aasta2, labisoit1, labisoit2, kutus, tuup, kaigukast } = req.query;

  // Construct the base SQL query
  let sql = "SELECT * FROM soidukid WHERE 1=1";

  // Define an array to store the parameter values
  const params = [];

  if (mark) {
    sql += " AND nimi LIKE ?"; 
    params.push(`%${mark}%`); 
  }
  if(kutus) {
      sql += " and kutus LIKE ?";
      params.push(`%${kutus}`);
  }
  if(tuup) {
      sql += " and tüüp LIKE ?";
      params.push(`%${tuup}`);
  }
  if (kaigukast) {
    sql += " AND käigukast = ?";
    params.push(kaigukast);
  }
    
  if (labisoit1 && labisoit2) {
    const minLabisoit = parseFloat(labisoit1);
    const maxLabisoit = parseFloat(labisoit2);
    sql += " AND CAST(SUBSTRING_INDEX(labisoit, 'km', 1) AS DECIMAL) BETWEEN ? AND ?";
    params.push(minLabisoit, maxLabisoit);
  }
    
  if(aasta1 && aasta2) {
  	const minAasta = parseInt(aasta1);
    const maxAasta = parseInt(aasta2);
    sql += " AND aasta BETWEEN ? AND ?";
    params.push(minAasta, maxAasta);
  }

  // Execute the constructed query with parameters
  try {
    const results = await queryDatabase(sql, params);
    res.json(results); // Assuming you want to return the results as JSON
  } catch (error) {
    console.error(error);
    res.status(500).send("Error executing the search query");
  }
});


function queryDatabase(query, params) {
    return new Promise((resolve, reject) => {
        connection.query(query, params, (error, results) => {
            if (error) {
                reject(error);
            } else {
                resolve(results);
            }
        });
    });
}

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
