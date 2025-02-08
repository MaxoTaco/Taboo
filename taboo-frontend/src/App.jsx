import "./App.css";
import TitleScreen from "./pages/TitleScreen";
import CreateGame from "./pages/CreateGame";
import Game from "./pages/Game";
import { Route, Router, Routes } from "react-router-dom";

function App() {
  return (
    <Routes>
      <Route path="/" element={<TitleScreen />} />
      <Route path="/create-game" element={<CreateGame />} />
      <Route path="/play-game" element={<Game />} />
    </Routes>
  );
}

export default App;
