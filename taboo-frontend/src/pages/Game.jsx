import React, { useState } from "react";
import WordCard from "../components/WordCard"; // Import WordCard to use it inside the Game component

// Array of words with their forbidden words
const words = [
  {
    main: "Laptop",
    forbidden: ["Computer", "Keyboard", "Screen", "Mac", "PC"],
  },
  { main: "Pizza", forbidden: ["Cheese", "Slice", "Topping", "Crust", "Oven"] },
];

const Game = () => {
  // State variables to track the current word and score
  const [index, setIndex] = useState(0); // The current word index in the 'words' array
  const [score, setScore] = useState(0); // The player's score

  // Function to go to the next word (with wrapping)
  const nextWord = () => {
    setIndex((prev) => (prev + 1) % words.length); // Loop to the next word
  };

  return (
    <div className="page">
      <div className="title-box">
        <label className="title">Taboo Game</label> {/* Display the game title */}
      </div>
      <WordCard word={words[index]} /> {/* Render the current word */}
      <div className="correct-skip-buttons">
        <button
          onClick={() => {
            setScore(score + 1);
            nextWord;
          }}
        >
          ✅ Correct
        </button>{" "}
        {/* Increment score */}
        <button onClick={nextWord}>⏩ Skip</button>{" "}
        {/* Move to the next word */}
      </div>
      <p>Score: {score}</p> {/* Display the score */}
    </div>
  );
};

export default Game;
