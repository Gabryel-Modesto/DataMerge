import pandas as pd
from io import BytesIO

def juntarTabelas(arquivo1, arquivo2):
    contrato_viferro = pd.read_excel(arquivo1)
    contrato_clientes = pd.read_excel(arquivo2)
    
    resultado = pd.merge(
        contrato_viferro,
        contrato_clientes,
        on="CODPROD",
        how="left"
    )
    
    # Cria um excel na memoria
    arquivo_saida = BytesIO()
    
    # Escreve o DataFrame dentro desse arquivo
    resultado.to_excel(arquivo_saida, index=False)
    
    # Volta para o começo do arquivo
    arquivo_saida.seek(0)
    
    return arquivo_saida
    

