console.log("JavaScrip Rodando -- Chat ativo")
// Função para salvar o estado do switch no LocalStorage
function salvarEstado() {
  var checkbox = document.getElementById('switch');
  // Salva o estado do checkbox no LocalStorage (true ou false)
  localStorage.setItem('switchEstado', checkbox.checked);
}

// Função para restaurar o estado do switch quando a página é carregada
function restaurarEstado() {
  var checkbox = document.getElementById('switch');
  var estadoSalvo = localStorage.getItem('switchEstado');
  var chat = document.getElementById('chat');
  
  // Se existir um estado salvo, define o estado do checkbox
  if (estadoSalvo !== null) {
    checkbox.checked = (estadoSalvo === 'true'); // Converte a string 'true' em booleano
  }

  // Função para fechar ou abrir a tela do chat
  if (checkbox.checked) {
    chat.style.backgroundColor=red; // Mostra o chat se o switch estiver ligado
  } else {
    chat.style.backgroundColor=blue; // Esconde o chat se o switch estiver desligado
  }
}

// Evento para salvar o estado sempre que o checkbox for alterado
document.getElementById('switch').addEventListener('change', function() {
  salvarEstado();
  restaurarEstado(); // Atualiza a exibição do chat ao alterar o switch
});

// Restaura o estado do switch e a exibição do chat quando a página for carregada
window.onload = restaurarEstado;