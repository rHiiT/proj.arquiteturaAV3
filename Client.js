const axios = require('axios');

axios.get('http://127.0.0.1:9000/cadeiras')
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error('Error');
  });