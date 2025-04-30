// Simple Node.js App Template (Express Placeholder)

const express = require("express");
const app = express();
const port = process.env.PORT || 3000;

app.get("/", (req, res) => {
  res.send("Welcome to the Node.js App Template!");
});

app.get("/health", (req, res) => {
  res.json({ status: "ok" });
});

// Add more routes as needed for the template

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});

