const Root = document.documentElement;
const btn = document.getElementById("btnTrocaDeTema");
const arquivo1 = document.getElementById("arquivo1");
const arquivo2 = document.getElementById("arquivo2")
const formulario = document.getElementById("formulario")
const API_URL  = "http://localhost:3000/merge";

// Botão para a troca de tema
btn.addEventListener("click", () => {
    const escuro = Root.getAttribute("data-tema") === "escuro";
    if(escuro) {
        Root.removeAttribute("data-tema");
    } else {
        Root.setAttribute("data-tema", "escuro")
    };
});

// Validando campos
function validarDados(){
    if(!arquivo1.value || !arquivo2 .value) {
        alert("Campo não pode ser vázio!");
        return false;
    };
    return true;
};

// Fetch
async function enviarDados(formData) {
    const res = await fetch(API_URL ,
        {
            method: "POST",
            body: formData
        });
        // Pegando a resposta que veio do Flask
        const blob = await res.blob();

        // Criando uma URL temporária
        const url = URL.createObjectURL(blob);

        const link = document.createElement("a");

        link.href = url;

        link.download = "DataMerge.xlsx";

        link.click();

        URL.revokeObjectURL(url);
};

// Enviando para o BackEnd
formulario.addEventListener("submit", (e) => {
    e.preventDefault();
    
    if(!validarDados()) {
        return;
    }
    
    const formData = new FormData(formulario);

    enviarDados(formData);
});