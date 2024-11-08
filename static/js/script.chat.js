console.log("JavaScript Rodando -- Chat ativo");

async function sendMessage() {
  const prompt = document.getElementById('inputtxt').value;

  // Envia a mensagem para a API
  const response = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: prompt })
  });
  
  const data = await response.json();

  const messagesContainer = document.getElementById('messages');

  // Cria um elemento para a mensagem do usuário
  const userMessage = document.createElement('div');
  userMessage.classList.add('message', 'user-message');
  userMessage.innerText = `Você: ${prompt}`;
  messagesContainer.appendChild(userMessage);

  // Cria um elemento para a resposta da IA
  const iaMessage = document.createElement('div');
  iaMessage.classList.add('message', 'ia-message');
  iaMessage.innerText = `IA: ${data.response || data.error}`;
  messagesContainer.appendChild(iaMessage);

  // Limpa o campo de input após o envio
  document.getElementById('inputtxt').value = '';
}