# exemplo_08_classes_heranca.py


class Usuario:
    def __init__(self, id: int, nome: str, email: str, senha: str):
        # __ é utilizado para definir algo como privado
        self.__id = id 
        self.__nome = nome
        self.__email = email
        self.__senha = senha

    def cadastrar(self):
        print("Cadastrando no banco de dados")
    
    def autenticar(self, email: str, senha: str) -> bool:
        if self.__email == email and self.__senha == senha:
            return True
        else:
            return False
    
    def alterar_dados(self, nome: str, email: str):
        self.__nome = nome
        self.__email = email
    

class Cliente(Usuario):
    def __init__(self, id: int, nome: str, email: str, senha: str, endereco: str, telefone: str, cpf: str):
        super().__init__(id, nome, email, senha) # passando para o construtor do pai o que é necessário
        self.__endereco = endereco
        self.__telefone = telefone
        self.__cpf = cpf


def exemplo_usuario():
    chico = Usuario(1, "Chico", "chiquinho@gmail.com", "1234")


    email: str = input("Digite o e-mail para entrar no sistema: ")
    senha: str = input("Digite o senha: ")
    if(chico.autenticar(email, senha) == True):
        print("Pode entrar no sistema")
    else:
        print("Usuário não autorizado")


exemplo_usuario()