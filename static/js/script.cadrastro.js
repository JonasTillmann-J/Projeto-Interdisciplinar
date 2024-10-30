console.log("JavaScrip Rodando -- Cadastro ativo")
function eyeopen(inputNumber) {
    // Definir os elementos para o primeiro ou segundo campo de senha
    const passwordField = document.getElementById(`olhoabertocad${inputNumber}`);
    const imageField = document.getElementById(`olhoaberto${inputNumber}`);

    // Verificar o tipo do input de senha
    if (passwordField.type === "password") {
        passwordField.type = "text"; // Mostrar senha
        imageField.src = '/Imgs Gerais/imgs/hide.png'; // Alterar o ícone
    } else {
        passwordField.type = "password"; // Ocultar senha
        imageField.src = '/Imgs Gerais/imgs/visible.png'; // Restaurar o ícone
    }
}
/*
const password1 = document.getElementById("olhoabertocad1")
const password2 = document.getElementById("olhoabertocad2")
const imagematual1 = document.getElementById("olhoaberto1")
const imagematual2 = document.getElementById("olhoaberto2")
const btnEntrar = document.getElementById("btnEntrarLOGIN")
function tclaEnter(event) {
    if (event.key === 'Enter') {
        document.getElementById('myButton').click();
    }
}
function eyeopen() {
    if (password1.type == "password") {
        password1.type = "text"
        olhoaberto1.src = '/Imgs Gerais/imgs/hide.png';
    } else {
        password1.type = "password"
        olhoaberto1.src = '/Imgs Gerais/imgs/visible.png';
    }
}*/