from typing import Dict, List

def exemplo_basico_dicionario():
    carros = {}

    carros["bmw"] = "M5"
    carros["mercedes"] = "GLA 250"
    carros["fiat"] = "uno"

    carros["mercedes"] = "GLA 200"
    print("Dicionário:", carros)

    # Obter as chaves que tenho no meu dicionário
    print(carros.keys())

    # Obter os valores que tenho no meu dicionário
    print(carros.values())

# função que tem um parâmetro do tipo dicionário
def obter_clientes_com_score_alto(clientes: Dict[str, Dict[str, float]]):
    # Descobrir quais clientes tem score alto(acima de 650)

    clientes_selecionados: List[str] = []
    for nome_cliente, dados_cliente  in clientes.items():
        score = dados_cliente["score"]
        if score > 650:
            clientes_selecionados.append(nome_cliente)
    
    return clientes_selecionados


def somar_salarios(clientes: Dict[str, Dict[str, float]]) -> float:
    total = 0
    for dados in clientes.values():
        salario = dados["salario"]
        total = total + salario
    return total

def obter_nome_clientes(clientes: Dict[str, Dict[str, float]]) -> List[str]:
    nomes = []
    for nome_cliente in clientes.keys():
        nomes.append(nome_cliente)
    return nomes


def processar_disponibilidade_emprestimo():
    clientes: Dict[str, Dict[str, float]]  = {
        "Amanda": {
            "salario": 2000,
            "id": 100,
            "score": 997
        },
        "Pedro": {
            "salario": 20_951.29,
            "id": 101,
            "score": 130
        },
        "Steffany": {
            "salario": 4593.29,
            "id": 102,
            "score": 520
        },
        "Rogério": {
            "salario": 17231.39,
            "id": 103,
            "score": 776
        }
    }
    clientes_aprovados_para_emprestimo = obter_clientes_com_score_alto(clientes)
    total_salarios = somar_salarios(clientes)
    nome_clientes = obter_nome_clientes(clientes)

    print("Clientes aprovados para empréstimo:", clientes_aprovados_para_emprestimo)
    print("Total dos salários:", total_salarios)
    print("Clientes: ", nome_clientes)


processar_disponibilidade_emprestimo()