class Estudante:
    escola = "ESCOLA"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

aluno_1 = Estudante("Giuliano", 1)
aluno_2 = Estudante("Glaucia", 2)
mostrar_valores(aluno_1, aluno_2)

Estudante.escola = "Python"
aluno_3 = Estudante("Nina", 3)
mostrar_valores(aluno_1, aluno_2, aluno_3)
