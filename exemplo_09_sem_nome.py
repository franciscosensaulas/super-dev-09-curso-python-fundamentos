from pathlib import Path
from typing import Any, Dict


def salvar_arquivo(razao_social: str, cnpj: str):

    caminho = Path("arquivos")
    # Tenta criar o diretório, caso existir não apresenta erro
    caminho.mkdir(exist_ok=True)

    with open(caminho/ f"{razao_social}.csv", "w+") as caminho:
        caminho.write(f"{razao_social};{cnpj}")


def juntar_texto(
    **parametros: Dict[str, Any]
) -> str:
    razao_social = parametros["razao_social"]
    cnpj = parametros["cnpj"]
    
    salvar_arquivo(razao_social, cnpj)


def exemplo_dicionario():
    juntar_texto(razao_social="Escola Samba S.A", cnpj="X2.VAQ.11G/0001-63")

    juntar_texto(
        razao_social="Escola Java LTDA", 
        cnpj="5S.DOB.8RI/0001-00", 
        nome_fantasia="Javita da Galera",
        telefone="(40) 23032-2012",
        endereco="Rua das flores"
    )


exemplo_dicionario()