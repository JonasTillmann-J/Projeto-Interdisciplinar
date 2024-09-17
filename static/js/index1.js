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