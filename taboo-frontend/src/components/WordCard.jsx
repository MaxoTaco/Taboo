import React from "react";

// WordCard component displays the current word and its forbidden words
const WordCard = ({ word }) => {
  return (
    <div>
      <h2>{word.main}</h2>  {/* Display the main word */}
      <h4>Forbidden Words:</h4>
      <ul>
        {word.forbidden.map((w, i) => (
          <li key={i}>{w}</li> /* List each forbidden word */
        ))}
      </ul>
    </div>
  );
};

export default WordCard;