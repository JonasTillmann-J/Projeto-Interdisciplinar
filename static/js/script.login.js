console.log("JavaScrip Rodando -- Login ativo")
const password = document.getElementById("input-senha")
const imagematual = document.getElementById("olhoaberto")
const btnEntrar = document.getElementById("btnEntrarLOGIN")
function tclaEnter(event) {
    if (event.key === 'Enter') {
        document.getElementById('myButton').click();
    }
}
function eyeopen() {
    if (password.type == "password") {
        password.type = "text"
        olhoaberto.src = '/static/imgs/visible.png';
    } else {
        password.type = "password"
        olhoaberto.src = '/static/imgs/hide.png';
    }
}

