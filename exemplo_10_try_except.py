def exemplo_sem_tratamento():
    print("Divisão: ", 10 / 0)
    print("Mensgem depois da divisão")
    # Lança a excessão: ZeroDivisionError: division by zero


def exemplo_com_tratamento():
    try:
        print("Divisão: ", 10 / 0)
    except ZeroDivisionError:
        print("Não é possível dividir um número por zero.")

    print("O programa continuou normalmente")


def exemplo_com_tratamento_conversao():
    numero_digitado: str = "dois"
    try:
        # converter de str para int
        numero: int = int(numero_digitado)
        print("Número digitado: ", numero)
    except ValueError:
        print("Texto digitado não é um número válido")
        # print("Não foi possível converter o número para inteiro")
    print("Acabou")


# Ponto de entrada da aplicação, deve ter um único da aplicação inteira
if __name__ == "__main__":
    # exemplo_sem_tratamento()
    exemplo_com_tratamento_conversao()