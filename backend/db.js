const mysql = require("mysql2");

var connection;

function handleDisconnect() {
    connection = mysql.createConnection({
        host: 'mysql.hinoob.xyz',
        user: 'CENSORED',
        password: 'CENSORED',
        database: 's5_aastategija'
    });

    connection.connect(function(err) { 
        if (err) {
            console.log('error when connecting to db:', err);
            setTimeout(handleDisconnect, 2000); 
        } else {
            console.log("connect finish");
        }
    }); 
    connection.on('error', function(err) {
        console.log('db error', err);
        if (err.code === 'PROTOCOL_CONNECTION_LOST') { 
            handleDisconnect(); 
        } else { 
            throw err; 
        }
    });
}

handleDisconnect();

module.exports = connection;
