import { useNavigate } from "react-router-dom";

function CreateGame() {
  const navigate = useNavigate();

  return (
    <div>
      <h2>Create Game</h2>
      <button onClick={() => navigate("/play-game")}>Start Game</button>
    </div>
  );
}

export default CreateGame;
