import random

def escolher_palavra():
    palavras = ["python", "programacao", "desenvolvimento", "openai", "inteligencia"]
    return random.choice(palavras)

def jogar_forca(palavra):
    letras_certas = set()
    tentativas = 6

    while tentativas > 0:
        letra = input("Digite uma letra: ")

        if letra in palavra:
            letras_certas.add(letra)
            print("Letra correta!")
        else:
            tentativas -= 1
            print(f"Letra incorreta! Tentativas restantes: {tentativas}")

        palavra_oculta = ''.join([letra if letra in letras_certas else '_' for letra in palavra])
        print(f"Palavra: {palavra_oculta}")

        if set(palavra) == letras_certas:
            print("Parabéns! Você acertou a palavra!")
            break

    if tentativas == 0:
        print(f"Game over! A palavra era: {palavra}")

palavra_secreta = escolher_palavra().lower()
print("Bem-vindo ao jogo da Forca!")
jogar_forca(palavra_secreta)