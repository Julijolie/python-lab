print("Qual seu nome e idade?")
x = input()
lista_palavras=x.split()
nome=lista_palavras[0]
print("Bom dia, "+ nome)
idade=int(lista_palavras[1])

if idade >= 18:
    print("Legal, você tem {} anos, já é um adulto." .format(idade))
else:
    print("maneito, vc tem {} anos." .format(idade))
