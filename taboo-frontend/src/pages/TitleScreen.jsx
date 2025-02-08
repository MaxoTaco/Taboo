import { useNavigate } from "react-router-dom";

function TitleScreen() {
  const navigate = useNavigate();

  return (
    <div>
      <h1>Taboo!</h1>
      <button onClick={() => navigate("/create-game")}>Create Game</button>
    </div>
  );
}

export default TitleScreen;
