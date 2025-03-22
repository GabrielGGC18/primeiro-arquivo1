import os

mensagens = []

nome = input("Nome: ")

while True:
    
    #Limpando Terminal
    os.system('cls')

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'],"_", m['texto'])
            


    print("_______ ")     

    #Obtendo texto]
    texto = input("mensagem:")
    if texto == "fim ":
        break

    #Adicionando Mensagem na Lista
    mensagens.append({
        "nome": nome,
        "texto": texto
        
 })
  