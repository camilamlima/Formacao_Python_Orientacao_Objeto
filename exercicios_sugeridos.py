# Um exercício baseado nessa aula seria criar uma função chamada "limpar_console()" que utilize a biblioteca "os" do Python para limpar o console antes de exibir uma mensagem. Você pode testar a função chamando-a e imprimindo uma mensagem de sua escolha. Lembre-se de importar a biblioteca "os" no início do código.

# Nesta aula, os instrutores discutiram sobre a importância de organizar o código em blocos de execução e como fazer isso utilizando funções no Python. Eles destacaram que colocar vários prints dentro de condicionais pode deixar o código poluído e difícil de manter. Por isso, é recomendado isolar comportamentos específicos em sequências de código, o que facilita a edição e atualização do código.

# Para criar uma função no Python, utiliza-se a palavra-chave "def" seguida pelo nome da função. É importante lembrar de colocar dois pontos após o nome da função. Dentro da função, é possível adicionar todo o código relacionado ao comportamento que se deseja implementar.

# Os instrutores também mencionaram a utilização da biblioteca "os" do Python, que fornece acesso a algumas funções embutidas, como a função "system". Essa função permite limpar o console antes de exibir mensagens. No Windows, utiliza-se "os.system('cls')" e no Mac, utiliza-se "os.system('clear')".

# Além disso, foi ressaltado que é uma boa prática de programação utilizar funções específicas para realizar ações específicas, ao invés de escrever todas as linhas de código dentro de um bloco "else". Isso torna o código mais organizado e fácil de entender.

# Uma vantagem de utilizar funções é que é possível fechar o bloco de código correspondente a função no editor de código sem apagá-lo, o que torna o código mais limpo e legível.

# No exemplo dado, foi criada uma função chamada "finalizar_app()" que é executada quando a opção escolhida não é um, dois ou três. No entanto, a função está marcada como indefinida e precisa ser definida adicionando o código desejado dentro da função, como por exemplo, um print com a mensagem "Finalizando o app".


# Claro! Aqui está um exercício baseado na aula:

# Escreva um programa em Python que exiba um menu de opções para o usuário, permitindo que ele escolha entre as seguintes opções:

# Cadastrar um novo cliente
# Listar todos os clientes cadastrados
# Atualizar informações de um cliente
# Sair
# Utilize a função input() para receber a escolha do usuário e armazene-a em uma variável. Em seguida, utilize estruturas condicionais para executar a ação correspondente à opção escolhida pelo usuário.

# Lembre-se de utilizar mensagens claras para orientar o usuário sobre o que deve ser digitado em cada caso.

# Espero que esse exercício seja útil para você praticar o que aprendeu na aula! Se tiver mais alguma dúvida, é só me perguntar. 😊


# Copiar código
# nome = input('Digite o seu nome: ')
# print('Olá,', nome, '! Bem-vindo(a)!')
# Exemplo de uso do input() para receber dois números e exibir a soma deles:
# python
# Copiar código
# num1 = float(input('Digite o primeiro número: '))
# num2 = float(input('Digite o segundo número: '))
# soma = num1 + num2
# print('A soma dos números é:', soma)
# Exemplo de uso do input() para receber a idade do usuário e exibir uma mensagem de acordo com a faixa etária:
# python
# Copiar código
# idade = int(input('Digite a sua idade: '))
# if idade < 18:
#     print('Você é menor de idade.')
# else:
#     print('Você é maior de idade.')
# Esses exemplos ilustram diferentes formas de utilizar o input() para receber dados do usuário e trabalhar com eles no programa. Lembre-se de sempre utilizar mensagens claras para orientar o usuário sobre o que deve ser digitado.

# Espero que esses exemplos adicionais sejam úteis para você! Se tiver mais alguma dúvida, é só me perguntar. 😊


# Com certeza! Aqui está um exercício mais complexo baseado na aula de Manipulação de Strings e Interpolação de String:

# Escreva um programa em Python que solicite ao usuário seu nome completo e sua data de nascimento no formato DD/MM/AAAA. Em seguida, exiba uma mensagem personalizada que inclua o nome do usuário e sua idade atual.

# Para calcular a idade atual, você pode utilizar a biblioteca datetime do Python. Pesquise como utilizar essa biblioteca para obter a data atual e realizar o cálculo da idade.

# Exemplo de saída: "Olá, [nome]! Você tem [idade] anos."

# Lembre-se de utilizar a interpolação de strings para inserir as informações corretas na mensagem. Divirta-se resolvendo o exercício!

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