var oracledb = require('oracledb');
 
oracledb.getConnection(
  {
    user          : "andre_francisco",
    password      : "Francisco4",
    connectString : "192.168.3.170:1521/TMHML"
  },
  function(err, connection) {
    if (err) {
      console.error(err.message);
      return;
    }
    connection.execute(
        "SELECT * FROM TMHML.SC5010 SC5 WHERE SC5.C5_NUM = '000001'",
      [],  
      function(err, result) {
        if (err) {
          console.error(err.message);
          doRelease(connection);
          return;
        }
        console.log(result.rows);
        doRelease(connection);
      });
  });
 
function doRelease(connection) {
  connection.close(
    function(err) {
      if (err)
        console.error(err.message);
    });
}

console.log(result.rows)