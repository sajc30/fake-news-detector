// frontend/src/index.js
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css'; // Keep this line if you have index.css
import App from './App';
// DO NOT import reportWebVitals

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// Make sure the call to reportWebVitals() is also removed from the bottom of this file.