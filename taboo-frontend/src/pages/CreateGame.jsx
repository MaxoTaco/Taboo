import { useNavigate } from "react-router-dom";
import Prompt from "../components/Prompt";

function CreateGame() {
  const navigate = useNavigate();

  const handleSendMessage = (message) => {
    console.log("User Input:", message);
    // TODO: Send message to backend
  };

  return (
    <div>
      <h2>Create Game</h2>
      <button onClick={() => navigate("/play-game")}>Start Game</button>
      <Prompt onSend={handleSendMessage} />
    </div>
  );
}

export default CreateGame;
