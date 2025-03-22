import json

def Adiciona_Palavras():
    dicionario = {}
    
    #Abre o arquivo e adiciona as palavras.
    try:
        with open("Dicionário_palavras.json", "r") as arquivo:
            dicionario = json.load(arquivo)
    except FileNotFoundError:
        #Se o arquivo não existir, cria um dicionário vazio
        pass

    while True:
        add_palavra = input("Digite a palavra ou S para sair ao menu: ")
        if add_palavra.lower() == "s":
            break
        add_retorno = input(("Digite a tradução ou S para sair ao menu: "))
        
        #Adiciona a palavra e a tradução ao dicionário
        dicionario[add_palavra] = add_retorno

    #Escreve o dicionário atualizado no arquivo com a indentação que deseja
    with open("Dicionário_palavras.json", "w") as arquivo:
        json.dump(dicionario, arquivo, indent=4)

Adiciona_Palavras()