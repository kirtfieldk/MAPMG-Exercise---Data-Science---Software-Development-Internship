import React, { useEffect } from 'react';
import axios from 'axios';

function App() {
  const fetch = async () => {
    const response = await axios.get('localHost:5000/api/v1/applicants');
    if (response) console.log(response);
    else console.log('Nothing');
  };
  useEffect(() => {
    fetch();
  });
  return (
    <div>
      <a
        className="App-link"
        href="https://reactjs.org"
        target="_blank"
        rel="noopener noreferrer"
      >
        Learn React
      </a>
      <div>Hello</div>
    </div>
  );
}

export default App;
