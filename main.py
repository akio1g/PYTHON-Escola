from entities.Aluno import Aluno
from controller import AlunoController as ac
from typing import List


if __name__ == '__main__':
    ac.adicionarAluno(aluno=Aluno('Gabriel Akio', '1110482012040', 'ADS'))
    ac.adicionarAluno(aluno=Aluno('Marcos Eduardo', '1110482012044', 'ADS'))
    ac.adicionarAluno(aluno=Aluno('Marcola Eduarda', '1110482012042', 'ADS'))

    ac.excluirAlunoPorRA('1110482012044')

    print(ac.listar())
