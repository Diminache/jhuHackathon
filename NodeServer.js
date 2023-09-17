const express = require('express');
const app = express();
const port = 80; // You can change this to any available port

// Serve static files (e.g., HTML) from a directory named 'public'
app.use(express.static('Backend'));

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});