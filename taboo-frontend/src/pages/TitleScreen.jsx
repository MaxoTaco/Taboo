import { useNavigate } from "react-router-dom";

function TitleScreen() {
  const navigate = useNavigate();

  return (
    <div className='page'>
      <h1 className='title'>Taboo!</h1>
      <div className='button-prompt'>
        <button className="main-button" onClick={() => navigate("/create-game")}>
          Create Game
        </button>
      </div>
    </div>
  );
}

export default TitleScreen;
