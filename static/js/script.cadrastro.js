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



function VerificaSenha(){
    let Senha1 = document.getElementById('olhoabertocad1').value;
    let Senha2 = document.getElementById('olhoabertocad2').value;
    let Mensagem = document.getElementById('mensagem');

    if (Senha1.length != 0) {
        if (Senha1 === Senha2) {
            Mensagem.textContent = "Senhas Iguais";
            Mensagem.style.backgroundColor = "#4CAF50";  // Mensagem de sucesso
            window.location.href = "/chat";  // Redireciona para a página de chat
            return true;
        } else {
            Mensagem.textContent = "Senhas Não Conferem";
            Mensagem.style.backgroundColor = "#ff4d4d";  // Mensagem de erro
        }
    return false;  // Impede o envio do formulário para permitir a verificação de senha
}
}