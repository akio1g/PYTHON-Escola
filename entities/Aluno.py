# nome, RA, Curso

class Aluno:
    def __init__(self: object, nome: str, ra: str, serie: str) -> None:
        self.__nome: str = nome
        self.__ra: str = ra
        self.__serie = str = serie

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def ra(self):
        return self.__ra

    @property
    def serie(self):
        return self.__serie


    def __str__(self):
        return f'Aluno {self.nome}\nRA {self.ra}\nSérie {self.serie}'