import { useNavigate } from "react-router-dom";

function TitleScreen() {
  const navigate = useNavigate();

  return (
    <div className="page">
      <div className="title-box">
        <label className="title">Taboo!</label>
      </div>
      <div className="button-prompt">
        <button
          className="main-button"
          onClick={() => navigate("/create-game")}
        >
          Create Game
        </button>
      </div>
    </div>
  );
}

export default TitleScreen;
