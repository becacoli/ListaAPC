#Escreva um programa que lê duas notas de vários alunos e armazena tais notas em um dicionário,
#onde a chave é o nome do aluno. A entrada de dados deve terminar quando for lida uma string vazia como nome. 
#Escreva uma função que retorna a média do aluno, dado seu nome.




def ReceberAlunos():
    lista_alunos = {}
    while True:
        nome = input("Digite o nome do aluno: ").lower()
        if nome == "":
            break
        notas = (input("Digite as notas separadas por vírgula: ")).split(",")

        lista_alunos[nome] = notas
    return lista_alunos

def CalcularMedia(aluno, lista_alunos):
    media = 0
    for nota in lista_alunos[aluno]:
        media += float(nota)
    return media/len(lista_alunos[aluno])
    
listaAlunos = ReceberAlunos()
print(CalcularMedia(input("Digite o nome do aluno para calcular a média: ").lower(), listaAlunos))
