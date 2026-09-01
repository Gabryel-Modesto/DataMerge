# DataMerge

O DataMerge é uma aplicação web desenvolvida para automatizar a junção e organização de dados presentes em diferentes arquivos Excel.

## 🎯 O problema

O projeto nasceu de um problema real: vendedores precisavam alimentar manualmente a planilha enviada pelos clientes com os produtos correspondentes da nossa empresa.

Esse processo podia consumir mais de 4 horas por dia, além de ser uma atividade repetitiva e sujeita a erros durante a manipulação das informações.

Pensando nisso, desenvolvi o DataMerge com o objetivo de automatizar esse processo, reduzindo o tempo necessário para preparar as planilhas e aumentando a produtividade.

## 💡 A solução

O DataMerge permite que o usuário envie duas planilhas:

- **Planilha principal:** define a estrutura e a sequência correta dos itens.
- **Planilha do cliente:** contém os dados que serão utilizados para alimentar a planilha principal.

A planilha principal possui prioridade na organização do resultado. Isso significa que a sequência dos itens deve ser preservada, enquanto as informações da segunda planilha são utilizadas para complementar os dados.

Ao final do processamento, o sistema gera automaticamente uma nova planilha Excel para download.

## 🛠️ Tecnologias utilizadas

### Front-end

- **HTML5** — estrutura da aplicação.
- **CSS3** — estilização e temas claro/escuro.
- **JavaScript** — interação com a interface, validações e comunicação com o Back-end.
- **Fetch API** — comunicação com o servidor através de requisições HTTP.

### Back-end

- **Python** — processamento dos arquivos.
- **Flask** — servidor, rotas e recebimento dos arquivos.
- **Flask-CORS** — comunicação entre Front-end e Back-end.

### Manipulação de dados

- **Pandas** — leitura, manipulação e junção dos dados.
- **OpenPyXL** — suporte à leitura e geração de arquivos `.xlsx`.

### Ferramentas

- **venv** — isolamento das dependências Python.

## 🌐 Acesse

[🚀 Acessar o DataMerge](https://datamerge-4itn.onrender.com/)

> O DataMerge está hospedado no Render e pode ser utilizado diretamente pelo navegador.
