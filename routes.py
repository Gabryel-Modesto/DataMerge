from main import app

from flask import render_template, request, flash, redirect, url_for


# Extensões de arquivos que o DataMerge aceita
ALLOWED_EXTENSIONS = {'csv', 'xlsx', 'xls'}

# Verifica se o arquivo possui uma extensão permitida
def allowed_file(filename):
    return (
        '.' in filename
        and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    )

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/merge", methods=['GET', 'POST'])
def postar():
    
    if request.method == 'POST':

        # request.files contém os arquivos enviados pelo formulário.
        if 'arquivo1' not in request.files:
            flash('arquivo1')
            return redirect(request.url)

        # Verifica se o arquivo2 foi enviado.
        if 'arquivo2' not in request.files:
            flash('arquivo2')
            return redirect(request.url)

        # Pega os arquivos enviados usando o mesmo "name"
        arquivo1 = request.files['arquivo1']
        arquivo2 = request.files['arquivo2']

        if arquivo1.filename == '':
            flash('Campo não pode ser vazio')
            return redirect(request.url)

        if arquivo2.filename == '':
            flash('Campo não pode ser vazio')
            return redirect(request.url)

        # Verifica se os DOIS arquivos possuem extensões permitidas.
        if allowed_file(arquivo1.filename) and allowed_file(arquivo2.filename):
            return "Arquivos válidos"

        else:
            return "Arquivos inválidos"