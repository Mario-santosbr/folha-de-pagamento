class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self):
        raise NotImplementedError

    def __str__(self):
        return f"{self.nome}: R$ {self.calcular_salario():.2f}"


class Gerente(Funcionario):
    def __init__(self, nome, salario_base, bonus):
        super().__init__(nome, salario_base)
        self.bonus = bonus

    def calcular_salario(self):
        return self.salario_base + self.bonus


class Vendedor(Funcionario):
    def __init__(self, nome, salario_base, vendas):
        super().__init__(nome, salario_base)
        self.vendas = vendas

    def calcular_salario(self):
        return self.salario_base + self.vendas * 0.05


class Estagiario(Funcionario):
    def calcular_salario(self):
        return self.salario_base


class VendedorSenior(Vendedor):
    def calcular_salario(self):
        return self.salario_base + self.vendas * 0.08


def total_folha(lista):
    total = 0

    for funcionario in lista:
        total += funcionario.calcular_salario()

    return total


# Programa principal
equipe = [
    Gerente("Ana", 8000, 2000),
    Vendedor("Bruno", 3000, 40000),
    VendedorSenior("Carla", 3500, 40000),
    Estagiario("Davi", 1500)
]

print("=== FOLHA DE PAGAMENTO ===")

for funcionario in equipe:
    print(funcionario)

print(f"\nTotal da folha: R$ {total_folha(equipe):.2f}")

print("\n=== FUNCIONARIOS COMISSIONADOS ===")

for funcionario in equipe:
    if isinstance(funcionario, Vendedor):
        print(funcionario.nome)
        