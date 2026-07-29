# exemplo_08_classes_heranca.py

class Pessoa:
    def __init__(self, nome: str, sobrenome: str):
        self.nome = nome
        self.sobrenome = sobrenome

    def gerar_nome_completo(self) -> str:
        return f"{self.nome} {self.sobrenome}"
    

# Herança(inheritance) permite uma classe (filha) herdar da classe pai 
class Funcionario(Pessoa):
    def __init__(self, nome: str, sobrenome: str, cargo: str, quantidade_horas: int, valor_hora: float):
        # super() permite ter acesso a propriedades e funções da classe pai
        super().__init__(nome, sobrenome)
        self.cargo = cargo
        self.quantidade_horas = quantidade_horas
        self.valor_hora = valor_hora
    
    def calcular_salario(self) -> float:
        salario = self.valor_hora * self.quantidade_horas
        return salario


class AuxiliarAdministrativo(Funcionario):
    def __init__(self, nome: str, sobrenome: str, quantidade_horas: int):
        super().__init__(nome, sobrenome, "Auxiliar Administrativo", quantidade_horas, 10.50)


class DiretorExecutivo(Funcionario):
    def __init__(self, nome: str, sobrenome: str):
        super().__init__(nome, sobrenome, cargo="Diretor Executivo", quantidade_horas=220, valor_hora=45.45)
    
    def calcular_salario(self):
        bonificacao = 3001
        salario = super().calcular_salario() + bonificacao
        return salario


class Chefe(Pessoa):
    def __init__(self, nome: str, sobrenome: str, meta: float):
        super().__init__(nome, sobrenome)
        self.meta = meta


def exemplo_funcionario():
    pessoa = Pessoa("Ronaldo", "Femomemo")
    print("Nome completo:", pessoa.gerar_nome_completo())

    messi = AuxiliarAdministrativo("Lionel", "Messi", 220)
    print("Nome completo do auxiliar administrativo:", messi.gerar_nome_completo())
    print("Salário: ", messi.calcular_salario())

    pele = DiretorExecutivo("Pelé", "Futebol")
    print("Nome completo do diretor executivo:", pele.gerar_nome_completo())
    print("Salário: ", pele.calcular_salario())


exemplo_funcionario()