import os 
import re
from datetime import datetime
from pathlib import Path

## Variaveis de ambiente Global

LIST_FILE_EXCLUDE =  [".txt",".py",".fdb",".fbk"]


#Função para Gravar Log
def grava_log(type_log:str = "Execusao", dic_arquivo:dict = {}, value_exec:str = None):
    string = f"Tipo do Log: {type_log}, informações do arquivo: {dic_arquivo}, execessão: {value_exec}, data: {datetime.now()}"
    with open("gravalog.log",'a') as gravalog :
        gravalog.write(string + '\n')

# capturar o local a onde está sendo executado o arquivo
def name_path():
    return  os.getcwd() 

#listando os arquivos.
def list_files(diretorio = None):
    lista_files_diretorio =[]
    lista_files_diretorio_temp = []
    if diretorio == None:
        lista_files_diretorio_temp = os.listdir()
    else :
        lista_files_diretorio_temp = os.listdir(diretorio)    

    for i in lista_files_diretorio_temp:
        if i.endswith('.zip'):
            lista_files_diretorio.append(i)

    return lista_files_diretorio

# Extraindo as informações no arquivo
def extrair_informacoes(nome_arquivo:str):
    # Define o padrão regex para os nomes de arquivos
    padrao = r"(FB[234])(_SW)?_(\w+)_([0-9]{1,2})_([0-9]{1,2})_([0-9]{4})__(\d{1,2})_(\d{1,2})_(\d{1,2})_FBK"
    nome_arquivo = os.path.splitext(nome_arquivo)
    # Faz a correspondência com o padrão
    correspondencia = re.match(padrao, nome_arquivo)
    
    if correspondencia:
        tipo_firebird = correspondencia.group(1)
        sw = correspondencia.group(2)
        sistema = correspondencia.group(3)
        dia = correspondencia.group(4)
        mes = correspondencia.group(5)
        ano = correspondencia.group(6)
        hora = correspondencia.group(7)
        minuto = correspondencia.group(8)
        segundo = correspondencia.group(9)
        
        return {
            "tipo_firebird": tipo_firebird,
            "sw": sw,
            "sistema": sistema,
            "dia": dia,
            "mes": mes,
            "ano": ano,
            "hora": hora,
            "minuto": minuto,
            "segundo": segundo
        }
    else:
        return None

# Criando dicionario com informações do arquivo
def obter_informacoes_arquivo(caminho_arquivo):
    ext = extrair_informacoes(str(caminho_arquivo))
    # Obtém o caminho completo do arquivo
    caminho_completo = Path(caminho_arquivo).resolve()
    # Obtém a data de criação (somente no Windows)
    data_criacao = datetime.fromtimestamp(os.path.getctime(caminho_arquivo))

    # Obtém a data de modificação
    data_modificacao = datetime.fromtimestamp(os.path.getmtime(caminho_arquivo))

    # Obtém o tamanho do arquivo em bytes
    tamanho_arquivo = os.path.getsize(caminho_arquivo)

    # Retorna as informações
    return {
        "nome_arquivo": caminho_arquivo,
        "tipo":ext['sw'].replace('_','') , 
        "caminho_completo": caminho_completo,
        "data_criacao": data_criacao,
        "data_modificacao": data_modificacao,
        "tamanho_arquivo": tamanho_arquivo,
        "data_arquivo": f"{ext['dia']}-{ext['mes']}-{ext['ano']}",
        "hora_arquivo": f"{ext['hora']}:{ext['minuto']}:{ext["segundo"]}",
        "Firebird": ext['tipo_firebird']
    }


if __name__=='__main__':
    a  = list_files()

    for i in a:
        # # print(a)
        #  print(type(i))
        f = obter_informacoes_arquivo(str(i))
        print(f)

    pass