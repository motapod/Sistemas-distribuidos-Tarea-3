const express = require("express");
const port = process.env.PORT || 3000;
const app = express();


app.post("/", async (req, res) => {
    
});


app.listen(port, () => {
  console.log(`La API esta corriendo en  http://localhost:${port}`);
});