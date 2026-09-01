import pandas as pd
from io import BytesIO

def juntarTabelas(arquivo1, arquivo2):
    contrato_viferro = pd.read_excel(arquivo1)
    contrato_clientes = pd.read_excel(arquivo2)
    
    if "CODPROD" not in contrato_viferro.columns:
        raise ValueError("A coluna 'CODPROD' não foi encontrada no arquivo principal.")
    
    if "CODPROD" not in contrato_clientes.columns:
        raise ValueError("A coluna 'CODPROD' não foi encontrada no arquivo secundário.")

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
    

