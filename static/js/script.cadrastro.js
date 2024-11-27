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



function VerificaSenha() {
    let Senha1 = document.getElementById('olhoabertocad1').value;
    let Senha2 = document.getElementById('olhoabertocad2').value;
    let Mensagem = document.getElementById('mensagem');

    const hasUppercase = /[A-Z]/.test(Senha1);
    const hasSpecialChar = /[!@#$%^&*(),.?":{}|<>]/.test(Senha1);

    // Verificar se a senha tem pelo menos 8 caracteres
    if (Senha1.length < 8) {
        Mensagem.textContent = "A senha deve conter no mínimo 8 caracteres.";
        Mensagem.style.backgroundColor = "#ff4d4d";  // Mensagem de erro
        return false;  // Impede o envio do formulário
    }

    // Verificar se a senha contém pelo menos uma letra maiúscula ou um caractere especial
    if (!hasUppercase && !hasSpecialChar) {
        Mensagem.textContent = "A senha deve conter pelo menos uma letra maiúscula ou um caractere especial.";
        Mensagem.style.backgroundColor = "#ff4d4d";  // Mensagem de erro
        return false;  // Impede o envio do formulário
    }

    // Verificar se as senhas coincidem
    if (Senha1 === Senha2) {
        Mensagem.textContent = "Senhas Iguais";
        Mensagem.style.backgroundColor = "#4CAF50";  // Mensagem de sucesso
        return true;  // Permite o envio do formulário
    } else {
        Mensagem.textContent = "Senhas Não Conferem";
        Mensagem.style.backgroundColor = "#ff4d4d";  // Mensagem de erro
        return false;  // Impede o envio do formulário
    }
}




