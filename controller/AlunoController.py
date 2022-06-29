from entities.Aluno import Aluno
from typing import List

ALUNOS: List[Aluno] = []


def adicionarAluno(aluno: Aluno) -> None:
    contador: int = 0
    if not any(ALUNOS):
        ALUNOS.append(aluno)
        print('Aluno cadastrado!\n')
    else:
        for x in ALUNOS:
            if (ALUNOS[-1].ra == x.ra):
                ALUNOS.append(aluno)
                print('Aluno cadastrado!\n')
                break;
            if (x.ra == aluno.ra):
                ALUNOS[contador] = aluno
                print('Aluno Alterado')
                break
            contador += 1


def excluirAlunoPorRA(ra: str) -> None:
    for x in ALUNOS:
        if (x.ra == ra):
            ALUNOS.remove(x)
            print('Aluno removido\n')
            break
        if(ALUNOS[-1].ra == x.ra):
            print('Aluno não encontrado\n')


def procurarPorRA(ra: str) -> Aluno:
    for x in ALUNOS:
        if (x.ra == ra):
            a: Aluno = x
            break
        if(ALUNOS[-1].ra == x.ra):
            print('Aluno não encontrado\n')
    return a


def listar() -> str:
    lista: str = ''
    for x in ALUNOS:
        lista = lista + f'\n{x}'
    return lista
