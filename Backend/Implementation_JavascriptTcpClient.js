// Create a WebSocket connection
//const WebSocket = window.WebSocket; // If you're running this in a browser

const WebSocket = require('ws'); // If you're running this in a Node.js environment

const socket = new WebSocket("ws://localhost:5001"); // Replace with your WebSocket server URL

// Function to handle messages received from the server
socket.onmessage = (event) => {
    console.log(`Received: ${event.data}`);
};

// Function to handle errors
socket.onerror = (error) => {
    console.error(`WebSocket Error: ${error.message}`);
};

// Function to handle connection open event
socket.onopen = (event) => {
    console.log("Connected to server.");

    // Example: Send a message to the server after the connection is open
    sendMessage("Hello, WebSocket server!");
};

// Function to handle connection close event
socket.onclose = (event) => {
    if (event.wasClean) {
        console.log(`Connection closed cleanly, code=${event.code}, reason=${event.reason}`);
    } else {
        console.error("Connection died");
    }
};

// Function to send a message to the server
function sendMessage(message) {
    socket.send(message);
}

// Keep the script running until explicitly exited
console.log("WebSocket client is running. Press Ctrl+C to exit.");