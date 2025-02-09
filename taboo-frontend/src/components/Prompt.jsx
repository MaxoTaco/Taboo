import { useState } from "react";

function Prompt({ onSend }) {
  const [message, setMessage] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (message.trim()) {
      onSend(message);
      setMessage(""); // Clear input after sending
    }
  };

  return (
    <form className="prompt" onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Ex: Road trip words"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />
      <button type="submit">➤</button>
    </form>
  );
}

export default Prompt;
