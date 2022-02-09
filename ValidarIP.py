def ValideIP(endereco_ip): #Comparando e validando
    for numero in endereco_ip:
        if int(numero) > 255: 
            return False
    return True

arq = open("ips.txt")
EnderecoDeIps = []

for endereco_ip in arq:
    EnderecoDeIps.append(endereco_ip.rstrip().split(".")) #Tirando os espaço e o ponto do IP para comparação
print(EnderecoDeIps)

for endereco_ip in EnderecoDeIps: 
    endereco_formatado = ".".join(endereco_ip)
    if ValideIP(endereco_ip):               #Chamando a função validadora
        print(f"{endereco_formatado} é válido")
    else:
        print(f"{endereco_formatado} é inválido")

arq.close()
