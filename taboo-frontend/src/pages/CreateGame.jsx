import { useNavigate } from "react-router-dom";
import Prompt from "../components/Prompt";

function CreateGame() {
  const navigate = useNavigate();

  const handleSendMessage = (message) => {
    console.log("User Input:", message);
    // TODO: Send message to backend
  };

  return (
    <div className="page">
      <div className="title-box">
        <label className="title">Create Game</label>
      </div>
      <table>
        <td>Settings</td>
        <td>
          <tr>Forbidden words:</tr>
          <tr>
            <select></select>
          </tr>
        </td>
        <td>
          <tr>Guessing time:</tr>
          <tr>
            <select></select>
          </tr>
        </td>
        <td>
          <tr>Category:</tr>
          <tr>
            <Prompt onSend={handleSendMessage} />
          </tr>
        </td>
      </table>
      <div className="button-prompt">
        <button className="main-button" onClick={() => navigate("/play-game")}>
          Start Game
        </button>
      </div>
    </div>
  );
}

export default CreateGame;
