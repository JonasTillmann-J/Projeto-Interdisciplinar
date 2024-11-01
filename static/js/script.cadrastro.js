console.log("JavaScrip Rodando -- Cadastro ativo")

function eyeopen(inputNumber) {
    // Definir os elementos para o primeiro ou segundo campo de senha
    const passwordField = document.getElementById(`olhoabertocad${inputNumber}`);
    const imageField = document.getElementById(`olhoaberto${inputNumber}`);

    // Verificar o tipo do input de senha
    if (passwordField.type === "password") {
        passwordField.type = "text"; // Mostrar senha
        imageField.src = '/static/imgs/hide.png'; // Alterar o ícone
    } else {
        passwordField.type = "password"; // Ocultar senha
        imageField.src = '/static/imgs/visible.png'; // Restaurar o ícone
    }
}