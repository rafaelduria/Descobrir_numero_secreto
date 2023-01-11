import random
from time import sleep

def play():
    print('Bem vindo !')

    numero_secreto = random.randrange(1,101)

    try:
        dificuldade = str(input('Escolha nivel EASY or HARD: ')).upper().strip()
        if dificuldade == 'EASY':
            tentativas = 10
            saque = 100
        
        if dificuldade == 'HARD':
            tentativas = 5
            saque = 200

        imprime_dificuldade_tentativas(dificuldade,tentativas)

    except:
        if dificuldade != 'EASY' and  dificuldade != 'HARD':    
            while True:
                dificuldade = str(input(f'Você digitou {dificuldade} por gentileza escolher:  EASY or HARD: ')).upper().strip()
                if dificuldade == 'EASY':
                    tentativas = 10
                    saque = 100
                
                if dificuldade == 'HARD':
                    tentativas = 5
                    saque = 200

                if dificuldade == 'EASY'or dificuldade == 'HARD':
                    imprime_dificuldade_tentativas(dificuldade,tentativas)
                    break

    score = 1000
    chutes_Tentados = 0
    chute = int(input('Escolha numero de 1 até 100: '))
    chutes_Tentados = chutes_Tentados + 1
       
    if chute == numero_secreto:
        imprime_mensagem_ganhador(numero_secreto,chutes_Tentados,score)

    else:
        while chute != numero_secreto:
            if dificuldade == 'HARD' and chutes_Tentados == 5 or dificuldade == 'EASY' and chutes_Tentados == 10 :
                imprime_mensagem_perdedor(numero_secreto,chutes_Tentados)
                break
                
            if chute > numero_secreto:
                score = score - saque
                chute = int(input(f'Você Digitou {chute}\n\nMas número secreto é MENOR\n\nVocê perdeu {saque} PONTOS\n\nSeu score é de {score} pontos\n\nTente novamente: '))
                chutes_Tentados = chutes_Tentados + 1

            if chute < numero_secreto:
                score = score - saque
                chute = int(input(f'Você Digitou {chute}\n\nMas número secreto é MAIOR\n\nVocê perdeu {saque} PONTOS\n\nSeu score é de {score} pontos\n\nTente novamente: '))
                chutes_Tentados = chutes_Tentados + 1

            if numero_secreto == chute:
                imprime_mensagem_ganhador(numero_secreto,chutes_Tentados,score)
                break


def imprime_dificuldade_tentativas(dificuldade,tentativas):
    print(f'Você escolher nivel "{dificuldade}" você terá {tentativas} tentativas, BOA SORTE.')



def imprime_mensagem_ganhador(numero_secreto,chutes_Tentados,score):
            print(f'Você ACERTOU o número secreto é {numero_secreto}, você usou {chutes_Tentados} chutes e seu score é de {score} pontos.')
            print("       ___________      ")
            sleep(0.3)
            print("      '._==_==_=_.'     ")
            sleep(0.3)
            print("      .-\\:      /-.    ")
            sleep(0.3)
            print("     | (|:.     |) |    ")
            sleep(0.3)
            print("      '-|:.     |-'     ")
            sleep(0.3)
            print("        \\::.    /      ")
            sleep(0.3)
            print("         '::. .'        ")
            sleep(0.3)
            print("           ) (          ")
            sleep(0.3)
            print("         _.' '._        ")
            sleep(0.3)
            print("        '-------'       ")
            print('############')
            print('PARABÉNS')
            print('############')


def imprime_mensagem_perdedor(numero_secreto,chutes_Tentados):
    print(f'Você PERDEU o número secreto era {numero_secreto}, você usou {chutes_Tentados} chutes.')
    print("    _______________         ")
    sleep(0.3)
    print("   /               \       ")
    sleep(0.3)
    print("  /                 \      ")
    sleep(0.3)
    print("//                   \/\  ")
    sleep(0.3)
    print("\|   XXXX     XXXX   | /   ")
    sleep(0.3)
    print(" |   XXXX     XXXX   |/     ")
    sleep(0.3)
    print(" |   XXX       XXX   |      ")
    sleep(0.3)
    print(" |                   |      ")
    sleep(0.3)
    print(" \__      XXX      __/     ")
    sleep(0.3)
    print("   |\     XXX     /|       ")
    sleep(0.3)
    print("   | |           | |        ")
    sleep(0.3)
    print("   | I I I I I I I |        ")
    sleep(0.3)
    print("   |  I I I I I I  |        ")
    sleep(0.3)
    print("   \_             _/       ")
    sleep(0.3)      
    print("     \_         _/         ")
    sleep(0.3)
    print("       \_______/           ")
    print('############')
    print('GAME OVER')
    print('############')


if(__name__ == "__main__"):
    play()
