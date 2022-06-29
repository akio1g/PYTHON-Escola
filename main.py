from entities.Aluno import Aluno
from controller import AlunoController as ac
from typing import List


if __name__ == '__main__':
    ac.adicionarAluno(aluno=Aluno('Gabriel Akio', '1110482012040', 'ADS'))
    ac.adicionarAluno(aluno=Aluno('Marcos Eduardo', '1110482012044', 'ADS'))
    ac.adicionarAluno(aluno=Aluno('Marcola Eduarda', '1110482012042', 'ADS'))
    ac.adicionarAluno(aluno=Aluno('Julio Prestes', '1110482012047', 'ADS'))
    ac.adicionarAluno(aluno=Aluno('Fernando Noronha', '1110482012049', 'ADS'))
    ac.adicionarAluno(aluno=Aluno('Gabriel Ortiz', '1110482012045', 'ADS'))

   # ac.excluirAlunoPorRA('1110482012044')

    print(f'\nResultado do Aluno Procurado:\n{ac.procurarPorRA("1110482012047")}')

    ac.adicionarAluno(aluno=Aluno('Marcela Eduarda', '1110482012042', 'ADS'))

    print(f'\n{ac.listar()}')
