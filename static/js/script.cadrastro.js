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
     const Senha1 = document.getElementById('olhoabertocad1').value;
     const Senha2 = document.getElementById('olhoabertocad2').value; 
     if (Senha1 === Senha2){
         document.getElementById('ConfereSenhas').innerHTML = '';
         return true;
        }else { document.getElementById('ConfereSenhas').innerHTML = '<p class="Senhas" id="ConfereSenhas">Senhas estão Diferentes, por favor verifique</p>'; 
         return false;
        } 
    }