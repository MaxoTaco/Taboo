import React, { useState, useEffect } from 'react';
import axios from 'axios';

const TabooCard = () => {
  const [tabooCard, setTabooCard] = useState(null);

  useEffect(() => {
    // Fetch the taboo card data from the Python backend
    axios.get('http://localhost:5000/generate-taboo')
      .then(response => {
        setTabooCard(response.data);
      })
      .catch(error => {
        console.error("There was an error fetching the taboo card:", error);
      });
  }, []);

  return (
    <div>
      {tabooCard ? (
        <div>
          <h3>Main Word: {tabooCard.main_word}</h3>
          <h4>Taboo Words:</h4>
          <ul>
            {tabooCard.taboo_words.map((word, index) => (
              <li key={index}>{word}</li>
            ))}
          </ul>
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default TabooCard;