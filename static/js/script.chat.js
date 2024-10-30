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
/*
const valornecessario = false;
const navbar = document.getElementById("navbar");
const navmenu = document.getElementById("navmenu");
const navbuttons = document.getElementById("navbuttons");
function depuração(valornecessario) {
  if (valornecessario === true) {
    console.log("depuração ativa");
    //alert("depuração ativa")
    navbar.style.background = "red";
    navmenu.style.background = "green";
    navbuttons.style.background = "blue";
  } else {
    //alert("depuração desativada")
    console.log("depuração desativada");
    navbar.style.background = "transparent";
    navmenu.style.background = "transparent";
    navbuttons.style.background = "transparent";
  }
}
depuração(valornecessario)
let date = new Date();
let year = date.getFullYear();
let month = date.getMonth();

const day = document.querySelector(".calendar-dates");
const currdate = document.querySelector(".calendar-current-date");
const prenexIcons = document.querySelectorAll(".calendar-navigation span");
const todayBtn = document.getElementById("today-btn");

// Array of month names
const months = [
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro"
  ];

// Function to generate the calendar
const manipulate = () => {
  // Get the first day of the month
  let dayone = new Date(year, month, 1).getDay();
  // Get the last date of the month
  let lastdate = new Date(year, month + 1, 0).getDate();
  // Get the day of the last date of the month
  let dayend = new Date(year, month, lastdate).getDay();
  // Get the last date of the previous month
  let monthlastdate = new Date(year, month, 0).getDate();

  let lit = "";

  // Loop to add the last dates of the previous month
  for (let i = dayone; i > 0; i--) {
    lit += `<li class="inactive">${monthlastdate - i + 1}</li>`;
  }

  // Loop to add the dates of the current month
  for (let i = 1; i <= lastdate; i++) {
    // Check if the current date is today
    let isToday = i === date.getDate() && month === date.getMonth() && year === date.getFullYear();
    lit += `<li ${isToday ? 'class="active"' : ""}>${i}</li>`;
  }

  // Loop to add the dates of the next month
  for (let i = 1; i < 7 - dayend; i++) {
    lit += `<li class="inactive">${i}</li>`;
  }

  day.innerHTML = lit;

  // Update the current date display
  currdate.textContent = `${months[month]} ${year}`;
};

// Function to handle navigation between months
const navigate = (direction) => {
  if (direction === "prev") {
    month--;
    if (month < 0) {
      month = 11;
      year--;
    }
  } else if (direction === "next") {
    month++;
    if (month > 11) {
      month = 0;
      year++;
    }
  }
  manipulate();
};

// Add event listeners to the navigation icons
prenexIcons.forEach((icon) => {
  icon.addEventListener("click", () => {
    navigate(icon.id === "calendar-prev" ? "prev" : "next");
  });
});

// Add event listener to the today button
todayBtn.addEventListener("click", () => {
  date = new Date();
  year = date.getFullYear();
  month = date.getMonth();
  manipulate();
});

// Initialize the calendar
manipulate();
*/