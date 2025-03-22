import random
    
def play():
    user = input("'pe' para PEDRA, 'pa' para PAPEL e 'te' para TESOURA: ")
    computer = random.choice(['pe', 'pa', 'te'])

    print(computer)

    if user == computer: 
        return "empate"
    
    if is_win(user, computer):
        return "Você ganhou!"
    return "Você perdeu!"
    
def is_win(player, oponent):
    #pe>te, pa>te , te>pe
    if(player == 'pe' and oponent == 'te') or (player == 'pa' and oponent == 'te') or (player == 'te' and oponent == 'pe'):
        return True
    
print(play())

result = "empate"
while result == "empate":
    result = play()
    print(result)


