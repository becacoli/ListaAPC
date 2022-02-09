arq = open(input("Qual arquivo você deseja abrir? "))

dic = {}
for linha in arq:
    ident, nome = linha.split()
    dic[ident] = nome

    
print(dic)
arq.close()

