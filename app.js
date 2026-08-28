const Root = document.documentElement;
const btn = document.getElementById("btnTrocaDeTema");
const arquivo1 = document.getElementById("arquivo1");
const arquivo2 = document.getElementById("arquivo2")
const formulario = document.getElementById("formulario")

// Botão para a troca de tema
btn.addEventListener("click", () => {
    const escuro = Root.getAttribute("data-tema") === "escuro";
    if(escuro) {
        Root.removeAttribute("data-tema");
    } else {
        Root.setAttribute("data-tema", "escuro")
    };
});

// Caso algum dos campos estiverem vazios, não tem como fazer o submit
formulario.addEventListener("submit", (e) => {
    if(!arquivo1.value
    || !arquivo2.value) {
        e.preventDefault();
        alert("O campo não pode estar vazio");
    };
});
