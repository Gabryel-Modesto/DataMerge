const Root = document.documentElement;
const btn = document.getElementById("btnTrocaDeTema");
const arquivo1 = document.getElementById("arquivo1");
const arquivo2 = document.getElementById("arquivo2");
const formulario = document.getElementById("formulario");
const alertaError = document.getElementById("alertaErro");
const mensagemErro = document.getElementById("mensagemErro");
const removerArquivo1 = document.getElementById("removerArquivo1");
const removerArquivo2 = document.getElementById("removerArquivo2");
const btnPrimario = document.getElementById("btnPrimario");
const temaSalo = localStorage.getItem("tema");
const API_URL = "http://localhost:3000/merge";

function mostrarErro(mensagem) {
  mensagemErro.textContent = mensagem;
  alertaError.classList.add("visivel");

  setTimeout(() => {
    alertaError.classList.remove("visivel");
  }, 4000);
};

removerArquivo1.addEventListener("click", () => {
  arquivo1.value = "";
});

removerArquivo2.addEventListener("click", () => {
  arquivo2.value = "";
});

// Botão para a troca de tema
btn.addEventListener("click", () => {
  const escuro = Root.getAttribute("data-tema") === "escuro";
  if (escuro) {
    Root.removeAttribute("data-tema");
    localStorage.setItem("tema", "claro");
  } else {
    Root.setAttribute("data-tema", "escuro");
    localStorage.setItem("tema", "escuro");
  }
});

// Mantendo o tema salvo no localStorage
if(temaSalo === "escuro") {
  Root.setAttribute("data-tema", "escuro");
}

// Validando campos
function validarDados() {
  if (!arquivo1.value || !arquivo2.value) {
    mostrarErro("Campo não pode ser vázio!");
    return false;
  }
  return true;
};

// Fetch
async function enviarDados(formData) {
  btnPrimario.textContent = "Processando...";
  btnPrimario.disable = true;

  try {
    const res = await fetch(API_URL, {
      method: "POST",
      body: formData,
    });

    if (!res.ok) {
      const erro = await res.json();
      mostrarErro(erro.erro);
      return;
    }

    // Pegando a resposta que veio do Flask
    const blob = await res.blob();

    // Criando uma URL temporária
    const url = URL.createObjectURL(blob);

    const link = document.createElement("a");

    link.href = url;

    link.download = "DataMerge.xlsx";

    link.click();

    URL.revokeObjectURL(url);

  } catch (error) {
    mensagemErro("Não foi possível conectar ao servidor!");

  } finally {
    btnPrimario.textContent = "Baixar";
    btnPrimario.disable = false;
  };
};

// Enviando para o BackEnd
formulario.addEventListener("submit", (e) => {
  e.preventDefault();

  if (!validarDados()) {
    return;
  }

  const formData = new FormData(formulario);

  enviarDados(formData);
});
