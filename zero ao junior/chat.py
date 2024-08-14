import os

mensagens = []

nome = input("nome: ")

while True:

    #limpando terminal
    os.system('cls')
    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])
    
    print("_________________")

    # obternha o texto
    texto = input("mensagem: ")
    if texto == "fim":
        break

    # adicionando mensagem na lista
    mensagens.append({
        "nome": nome,
        "texto": texto 

    })



