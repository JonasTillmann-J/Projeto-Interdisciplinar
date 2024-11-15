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


function VerificarSenha(){
    const senha = document.getElementById('olhoabertocad1').value;
    const confirmarSenha = document.getElementById('olhoabertocad2').value;

    if (senha !== confirmarSenha) {
        alert('As senhas não coincidem.');
    } else {
        // Enviar os dados para o Flask
        fetch('/cadastrar', {
            method: 'POST',
            body: JSON.stringify({ senha })
        })
        .then(response => response.json())
        .then(data => {
            // Tratar a resposta do Flask
            console.log(data);
        })
        .catch(error => {
            console.error('Erro ao enviar os dados:', error);
        });
    }
};

/*
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
*/