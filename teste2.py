import os
import re
from collections import defaultdict

def extrair_data(nome_arquivo):
    # Regex para capturar a data no formato dd_mm_aaaa dentro do nome do arquivo
    match = re.search(r"(\d{2}_\d{2}_\d{4})", nome_arquivo)
    if match:
        return match.group(1)  # Retorna a data como string
    return None

def processar_pastas(base_dir):
    for root, dirs, files in os.walk(base_dir):
        arquivos_por_data = defaultdict(list)
        
        # Itera sobre os arquivos
        for file in files:
            if file.endswith(".zip"):
                # Ignorar arquivos com "SW" no nome
                if "SW" in file:
                    novo_nome = f"Z_{file}"
                    os.rename(os.path.join(root, file), os.path.join(root, novo_nome))
                    print(f"Arquivo renomeado (SW): {novo_nome}")
                    continue
                
                # Extrair a data do nome do arquivo
                data = extrair_data(file)
                if data:
                    caminho_completo = os.path.join(root, file)
                    tamanho = os.path.getsize(caminho_completo)
                    arquivos_por_data[data].append((file, tamanho, caminho_completo))
        
        # Para cada data, manter apenas o maior arquivo
        for data, arquivos in arquivos_por_data.items():
            if len(arquivos) > 1:
                # Ordenar pelo tamanho e manter o maior
                arquivos.sort(key=lambda x: x[1], reverse=True)
                maior_arquivo = arquivos[0]
                print(f"Arquivo mantido: {maior_arquivo[0]}")

                # Renomear os demais com "Z" no início
                for arquivo in arquivos[1:]:
                    novo_nome = f"Z_{arquivo[0]}"
                    os.rename(arquivo[2], os.path.join(root, novo_nome))
                    print(f"Arquivo renomeado: {novo_nome}")
                    
if __name__ == "__main__":
    # Caminho base onde estão as pastas das entidades
    base_dir = r"D:/1/CONTABILIDADE"
    processar_pastas(base_dir)
