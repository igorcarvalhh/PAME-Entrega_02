from aluno import Aluno
import os
from materia import Materia
from professor import Professor
from turma import Turma

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def listar(lista):
    for e in lista:
        print(f"{e[0]} {e[1]}")


def menu_principal():
    clear()
    print("------------Menu Principal------------")
    print("1. Cadastro de uma nova matéria")
    print("2. Cadastro de um novo professor")
    print("3. Cadastro de um novo aluno")
    print("4. Mostrar todas as matéria cadastradas")
    print("5. Mostrar todos os professores cadastrados")
    print("6. Mostrar todos os alunos cadastrados")
    print("7. Abrir Menu de Turmas")
    print("8. Sair do Programa")

    opcao = input("Escolha uma opção: ")

    switcher = {
        "1":cadastro_materia,
        "2":cadastro_professor,
        "3":cadastro_aluno,
        "4":mostra_materias,
        "5":mostra_professores,
        "6":mostra_alunos,
        "7":menu_turma,
        "8":exit
    }
    switcher.get(opcao, menu_principal)()

def menu_turma():
    clear()
    print("------------Menu de Turmas------------")
    print("1. Cadastro de uma nova turma")
    print("2. Designar professor para uma turma")
    print("3. Adicionar alunos em uma turma")
    print("4. Remover alunos de uma turma")
    print("5. Dar a nota final dos alunos de uma turma")
    print("6. Mostrar todos os alunos de uma turma")
    print("7. Mostrar todas as turmas cadastradas")
    print("8. Voltar ao Menu Principal")

    opcao = input("Escolha uma opção: ")

    switcher = {
        "1":cadastro_turma,
        "2":designar_professor,
        "3":adiciona_aluno,
        "4":remove_aluno,
        "5":nota_final,
        "6":mostra_alunos_turma,
        "7":mostra_turmas,
        "8":menu_principal
    }
    switcher.get(opcao, menu_turma)()
    
def cadastro_materia():
    clear()
    print("------------Cadastrar Matéria------------")
    nome_materia = input("Nome da matéria: ")
    materia = Materia()
    materia.setNome(nome_materia)
    materia.post()

def cadastro_professor():
    clear()
    print("------------Cadastrar Professor------------")
    nome_professor = input("Nome do professor: ")
    professor = Professor()
    professor.setNome(nome_professor)
    professor.post()

def cadastro_aluno():
    clear()
    print("------------Cadastrar Aluno------------")
    nome_aluno = input("Nome do aluno: ")
    aluno = Aluno()
    aluno.setNome(nome_aluno)
    aluno.post()

def mostra_materias():
    clear()
    materia = Materia()
    listar(materia.get())
    input()

def mostra_professores():
    clear()
    professor = Professor()
    listar(professor.get())
    input()

def mostra_alunos():
    clear()
    aluno = Aluno()
    listar(aluno.get())
    input()

def cadastro_turma():
    clear()
    materia = Materia()
    listar(materia.get())
    opcao = input("Escolha uma matéria para turma: ")
    turma = Turma()
    turma.setMateria(opcao)

    clear()
    professor = Professor()
    listar(professor.get())
    opcao = input("Escolha um professor para turma: ")
    turma.setProfessor(opcao)

    turma.post()

def designar_professor():
    clear()
    turma = Turma()
    professor = Professor()
    materia = Materia()
    
    for i in turma.get():
        id_professor = i[1]
        id_materia = i[2]
        professor_turma = professor.get_nome(id_professor)[0][1]
        materia_turma = materia.get_nome(id_materia)[0][1]
        print(f"{i[0]} {materia_turma} {professor_turma} {i[3]}")
    opcao = input("Escolha uma turma: ")
    turma.setId(opcao)
    clear()
    professor = Professor()
    listar(professor.get())
    opcao = input("Escolha um professor para turma: ")
    turma.setProfessor(opcao)

    turma.put()
    input()

def adiciona_aluno():
    clear()
    turma = Turma()
    aluno = Aluno()
    professor = Professor()
    materia = Materia()
    
    for i in turma.get():
        id_professor = i[1]
        id_materia = i[2]
        professor_turma = professor.get_nome(id_professor)[0][1]
        materia_turma = materia.get_nome(id_materia)[0][1]
        print(f"{i[0]} {materia_turma} {professor_turma} {i[3]}")
    opcao = input("Escolha uma turma: ")

    aluno.setTurma(opcao)
    turma.setId(opcao)

    clear()
    listar(aluno.get())
    opcao = input("Escolha um aluno: ")
    
    aluno.setId(opcao)
    aluno.put()
    turma.add_aluno()

def remove_aluno():
    return 0

def nota_final():
    return 0

def mostra_alunos_turma():
    return 0

def mostra_turmas():
    clear()
    turma = Turma()
    professor = Professor()
    materia = Materia()
    
    for i in turma.get():
        id_professor = i[1]
        id_materia = i[2]
        professor_turma = professor.get_nome(id_professor)[0][1]
        materia_turma = materia.get_nome(id_materia)[0][1]
        print(f"{i[0]} {materia_turma} {professor_turma} {i[3]}")
    input()

while(True):
    menu_principal()