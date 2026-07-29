# exemplo_08_classes_heranca.py

class Pessoa:
    def __init__(self, nome: str, sobrenome: str):
        self.nome = nome
        self.sobrenome = sobrenome

    def gerar_nome_completo(self):
        return f"{self.nome} {self.sobrenome}"
    

# Herança(inheritance) permite uma classe (filha) herdar da classe pai 
class Funcionario(Pessoa):
    def __init__(self, nome: str, sobrenome: str, cargo: str):
        # super() permite ter acesso a propriedades e funções da classe pai
        super().__init__(nome, sobrenome)
        self.cargo = cargo


def exemplo_funcionario():
    pessoa = Pessoa("Ronaldo", "Femomemo")
    print("Nome completo:", pessoa.gerar_nome_completo())

    funcionario = Funcionario("Lionel", "Messi", "Administrativo")
    print("Nome completo do funcionário:", funcionario.gerar_nome_completo())

exemplo_funcionario()


"""
Criar uma classe Pessoa com os seguintes dados:
    - nome
    - numero telefone
    - email
    Criar uma função para apresentar todos os dados

Criar uma classe Professor com os seguintes dados:
    - nome
    - numero telefone
    - email
    - salário

    Herança de Pessoa
    Criar uma função para apresentar todos os dados

Criar uma classe Aluno com os seguintes dados:
    - nome
    - numero telefone
    - email
    - nota 1
    - nota 2
    - nota 3

    Herança de Pessoa
    Criar uma função para apresentar todos os dados
    Criar uma função para apresentar a média


"""

class Pessoa:

    # Construtor
    def __init__(self, nome: str, telefone: str, email: str):
        self.nome = nome
        self.telefone = telefone
        self.email = email


    def apresentar_dados(self):
        print(f"""
Nome: {self.nome}
Telefone: {self.telefone}
Email: {self.email}""")
        

class Professor(Pessoa):
    def __init__(self, nome: str, telefone: str, email: str, salario: float):
        super().__init__(nome, telefone, email)
        self.salario = salario

    def apresentar_dados(self): # Override: sobrescrever o comportamento do método da classe pai
        super().apresentar_dados()
        print(f"""
Salário: {self.salario}""")
        

class Aluno(Pessoa):


    def __init__(self, nome: str, telefone: str, email: str, nota1: float, nota2: float, nota3: float):
        super().__init__(nome, telefone, email)
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def apresentar_dados(self):
        super().apresentar_dados()
        print(f"""
Nota 1: {self.nota1}
Nota 2: {self.nota2}
Nota 3: {self.nota3}
""")
    
    def apresentar_media(self):
        media: float = (self.nota1 + self.nota2 + self.nota3) / 3

        print(f"Média: {media}")


def exemplo_heranca_pessoa():
    aluno1 = Aluno("Aluno1", "00000000000", "email@email.com", 9, 8, 4.5)

    professor1 = Professor("Professor1", "0000000000", "email@email.com", 1500)

    aluno1.apresentar_dados()
    aluno1.apresentar_media()

    professor1.apresentar_dados()

exemplo_heranca_pessoa()

