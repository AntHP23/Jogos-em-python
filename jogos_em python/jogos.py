import forca
import adivinhacao
import forca_melhor

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Adivinhação (2) forca (3) forca_melhorada ")

    jogo = int(input("Qual jogo? "))

    if jogo == 2:
        print("Jogando forca")
        forca.jogar()

    elif jogo == 3:
        print("Jogando forca_melhorada")
        forca_melhor.jogar()   

    elif jogo == 1:
        print("Jogando adivinhação")
        adivinhacao.jogar()
    else:
        print("não temos este jogo, digite o numero correspondente do jogo que deseja")

if(__name__ == "__main__"):
    escolhe_jogo()
