from main import app

from flask import render_template, request, send_file, jsonify
from service.merge import juntarTabelas


# Extensões de arquivos que o DataMerge aceita
ALLOWED_EXTENSIONS = {'csv', 'xlsx', 'xls'}

# Verifica se o arquivo possui uma extensão permitida
def allowed_file(filename):
    return ( '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/merge", methods=['GET', 'POST'])
def postar():
    
    if request.method == 'POST':

        # request.files contém os arquivos enviados pelo formulário.
        if 'arquivo1' not in request.files:
            return jsonify({
                "erro": "Arquivo principal não foi enviado!"
            }), 400

        # Verifica se o arquivo2 foi enviado.
        if 'arquivo2' not in request.files:
            return jsonify({
                "erro": "Arquivo secundário não enviado!"
            }), 400

        # Pega os arquivos enviados usando o mesmo "name"
        arquivo1 = request.files['arquivo1']
        arquivo2 = request.files['arquivo2']
        
        if arquivo1.filename == "":
            return jsonify({
                "erro": "Arquivo principal não foi selecionado!"
            }), 400
            
        if arquivo2.filename == "":
            return jsonify({
                "erro": "Arquivo secundário não foi selecionado!"
            }), 400

        if not allowed_file(arquivo1.filename):
            return jsonify({
                "erro": "A extensão do arquivo principal não é permitida!"
            }), 400

        if not allowed_file(arquivo2.filename):
            return jsonify({
                "erro": "A extensão do arquivo secundário não é permitida!"
            }), 400

        # Processa as planilhas
        try:
            arquivo_saida = juntarTabelas(arquivo1, arquivo2)
            
        except Exception as erro:
            return jsonify({
                "erro": str(erro)
            }), 500
        
        return send_file(
            arquivo_saida,
            as_attachment=True,
            download_name="DataMerge.xlsx",
            mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
            
                       
    