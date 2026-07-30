from datetime import datetime
from pathlib import Path


def exemplo_sem_erro():
    try:
        resultado = 10 / 2
        print("Resultado:", resultado)
    except ZeroDivisionError:
        print("Erro: divisão por zero.")
    finally:
        print("FINALLY: executei mesmo sem erro.")


def exemplo_com_erro():

    divisor = int(input("Digite o divisor: "))
    try:
        resultado = 10 / divisor
        print("Resultado:", resultado)
    except ZeroDivisionError:
        print("Erro: divisão por zero.")
    finally:
        print("FINALLY: executei mesmo com erro.")


# from datetime import datetime
# from pathlib import Path

def exemplo_tratar_criacao_diretorio():
    try:
        caminho_diretorio = Path("relatorios")
        caminho_diretorio.mkdir()
        print("Criado com sucesso")
    except FileExistsError:
        print("Diretório já existe")
    finally:
        mensagem = input("Digite uma mensagem para salvar no arquivo: ")

        caminho_arquivo = caminho_diretorio / "relatorio-2026-07-29.txt"
        with open(caminho_arquivo, "a", encoding="UTF-8") as f:
            data_hora_atual = datetime.now()
            f.write(str(data_hora_atual) + " " + mensagem + " \n")
            print("arquivo gerado ")


if __name__ == "__main__":
    # exemplo_sem_erro()
    exemplo_com_erro()
