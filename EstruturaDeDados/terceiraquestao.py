#Escreva um programa para armazenar uma agenda de telefones em um dicionário. 
#Cada pessoa pode ter um ou mais telefones e a chave do dicionário é o nome da pessoa.
#Seu programa deve ter as seguintes funções: 
#  – incluirNovoNome – essa função acrescenta um novo nome na agenda, com um ou mais telefones. Ela deve receber como argumentos o nome e os telefones.
#  – incluirTelefone – essa função acrescenta um telefone em um nome existente na agenda.
#  Caso o nome não exista na agenda, você deve perguntar se a pessoa deseja incluílo. 
#  Caso a resposta seja afirmativa, use a função anterior para incluir o novo nome. 
# excluirTelefone – essa função exclui um telefone de uma pessoa que já está na agenda.
#  Se a pessoa tiver apenas um telefone, ela deve serexcluída da agenda. 
#  – excluirNome – essa função exclui uma pessoa da agenda.
# – consultarTelefone – essa função retorna os telefones de uma pessoa na agenda.

Agenda = {"Rebeca": ["0001"], "Hicaro": ["9832"], "Maria": ["4324"]} #Os números do telefone estão entre colchetes porque estão em uma lista

def incluirNovoNome(nome, telefones):
    if nome not in Agenda:
        Agenda[nome] = telefones
    else:
        print("O contato já foi cadastrado!")

def incluirTelefone(nome, telefones):
    if nome not in Agenda:
        n = input("Contato não encontrado. Deseja cadastrá-lo? sim/não\n").lower()
        if n == "sim":
            incluirNovoNome(nome, telefones)
        else:
            print("O contato não foi salvo.")
    else:
        Agenda[nome].append(telefones) #Considerando os números em uma lista, a gente pode atribuir vários números de telefone a um único contato

def excluirNome(nome):
    if nome in Agenda:
        Agenda.pop(nome, None)
    else: 
        print("Esse contato não está cadastrado!")

def excluirTelefone(nome, telefone):
    if nome not in Agenda:
        print("O contato não está cadastrado!")
    else:
        if len(Agenda[nome]) <= 1: 
            excluirNome(nome)
        else:
            Agenda[nome][Agenda[nome].index(telefone)]

def ConsultarTelefone(nome):
   if not nome in Agenda:
       print("Este nome não está cadastrado!")
   else:
       print(Agenda[nome])


incluirNovoNome(nome = input("Digite o nome do seu contato: "), telefones = input("Digite o telefone do contato: "))
#incluirTelefone(nome = input("Digite o nome do contato: "), telefones = input("Digite o telefone do contato: "))
#excluirNome(nome = input("Digite o nome do contato que você deseja excluir: "))
#ConsultarTelefone(nome = input("Digite o nome do seu contato: "))
#excluirTelefone(nome = input("Digite o nome do seu contato: "), telefone = input("Digite o telefone do contato: "))

   
print(Agenda)
