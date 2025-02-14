const chatHistory = document.getElementById('chat-history');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');

function appendMessage(sender, text) {
  const messageDiv = document.createElement('div');
  messageDiv.classList.add('message', sender);
  messageDiv.textContent = sender === 'user' ? `You: ${text}` : `Tabi: ${text}`;
  chatHistory.appendChild(messageDiv);
  chatHistory.scrollTop = chatHistory.scrollHeight;
}

async function sendMessage() {
  const message = userInput.value.trim();
  if (!message) return;
  appendMessage('user', message);
  userInput.value = '';

  try {
    const response = await fetch('/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message })
    });
    const data = await response.json();
    if (data.reply) {
      appendMessage('bot', data.reply);
    } else if (data.error) {
      appendMessage('bot', "Error: " + data.error);
    }
  } catch (err) {
    appendMessage('bot', "Error connecting to the server.");
  }
}

sendBtn.addEventListener('click', sendMessage);
userInput.addEventListener('keydown', (e) => {
  if (e.key === 'Enter') sendMessage();
});
