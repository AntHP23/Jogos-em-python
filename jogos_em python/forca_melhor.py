import random

def jogar():
    palavras = []
    mensagem_de_abertura()
    palavras = tipo_da_palavra(palavras)
    palavra_escolhida, palavra_oculta = quantidade_de_letras(palavras)

    if palavra_escolhida is None or palavra_oculta is None:
        print("Não foi possível encontrar uma palavra com o número de letras especificado.")
        return

    letras_corretas = []
    letras_erradas = []
    tentativas = 8

    while True:
        print("\nPalavra: ", " ".join(palavra_oculta))
        print("Letras erradas: ", " ".join(letras_erradas))
        print("Tentativas restantes:", tentativas)

        letra = input("Digite uma letra: ").lower()

        if letra in letras_corretas or letra in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if letra in palavra_escolhida:
            letras_corretas.append(letra)
            for i in range(len(palavra_escolhida)):
                if palavra_escolhida[i] == letra:
                    palavra_oculta[i] = letra

            if "_" not in palavra_oculta:
                print("\nParabéns! Você venceu. A palavra era:", palavra_escolhida)
                break
        else:
            letras_erradas.append(letra)
            tentativas -= 1
            print("\nLetra incorreta. Você tem", tentativas, "tentativas restantes.")

        if tentativas == 7:
            print("  _______     ")
            print(" |/      |    ")
            print("|     (*_*)   ")
            print("|            ")
            print("|            ")
            print("|            ")

        if tentativas == 6:
            print("   _______     ")
            print("  |/      |    ")
            print(" |      (_)   ")
            print(" |      \     ")
            print(" |            ")
            print(" |            ")

        if tentativas == 5:
            print("   _______     ")
            print("  |/      |    ")
            print(" |      (_)   ")
            print(" |      \|    ")
            print(" |            ")
            print(" |            ")

        if tentativas == 4:
            print("   _______     ")
            print("  |/      |    ")
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |            ")
            print(" |            ")

        if tentativas == 3:
            print("   _______     ")
            print("  |/      |    ")
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |            ")

        if tentativas == 2:
            print("   _______     ")
            print("  |/      |    ")
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      /     ")

        if tentativas == 1:
            print("   _______     ")
            print("  |/      |    ")
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      / \   ")

        if tentativas == 0:
            print("\nVocê perdeu! A palavra era:", palavra_escolhida)
            print("Puxa, você foi enforcado!")
            print("    _______________         ")
            print("   /               \       ")
            print("  /                 \      ")
            print("//                   \/\  ")
            print("\|   XXXX     XXXX   | /   ")
            print(" |   XXXX     XXXX   |/     ")
            print(" |   XXX       XXX   |      ")
            print(" |                   |      ")
            print(" \__      XXX      __/     ")
            print("   |\     XXX     /|       ")
            print("   | |           | |        ")
            print("   | I I I I I I I |        ")
            print("   |  I I I I I I  |        ")
            print("   \_             _/       ")
            print("     \_         _/         ")
            print("       \_______/           ")

            break

def mensagem_de_abertura():
    print("*********************************")
    print("*****Seja muito bem-vindo *******")
    print("*******Ao jogo da forca *********")
    print("****Vejamos se consegue ganhar****")
    print("*****HAHAHAHA! (risada maleguina)**")
    print("*********************************")

def tipo_da_palavra(palavras):
    print("Escolha as categorias do jogo")
    categoria = input("1 - cidades, 2 - frutas, 3 - objetos:")

    if categoria == "1":
        with open('cidades.txt') as arquivo:
            linhas = arquivo.readlines()
        for linha in linhas:
            palavras.append(linha.strip())

    elif categoria == "2":
        with open('frutas.txt') as arquivo:
            linhas = arquivo.readlines()
        for linha in linhas:
            palavras.append(linha.strip())

    elif categoria == "3":
        with open('objetos.txt') as arquivo:
            linhas = arquivo.readlines()
        for linha in linhas:
            palavras.append(linha.strip())

    else:
        print("Categoria inválida. Escolha uma categoria válida.")
        return tipo_da_palavra(palavras)

    return palavras

def quantidade_de_letras(palavras):
    print("Escolha a quantidade de letras da palavra:")
    letras = int(input("4 letras, 5 letras, 6 letras:"))

    palavras_com_letras = [palavra for palavra in palavras if len(palavra) == letras]

    if palavras_com_letras:
        palavra_escolhida = random.choice(palavras_com_letras)
        palavra_oculta = ["_" for _ in palavra_escolhida]  # Cria uma lista de underscores do mesmo tamanho da palavra
        print("Palavra escolhida aleatoriamente:", " ".join(palavra_oculta))
        return palavra_escolhida, palavra_oculta
    else:
        print(f"Não há palavras com {letras} letras na categoria escolhida.")
        return None, None

if __name__ == "__main__":
    jogar()