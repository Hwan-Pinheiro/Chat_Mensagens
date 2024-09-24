import os

mensagens = []

nome = input("Nome: ")

while True:
    # Limpando o terminal
    os.system('cls')

    # Exibindo mensagens anteriores
    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])

    print("_________________")

    # Obtendo texto
    texto = input("mensagem: ")
    if texto == "fim":
        break

    # Adicionando mensagens na lista
    mensagens.append({
        "nome": nome,
        "texto": texto
    })



