import random
import remover_palavras_arq
import cadastrar_palavras_arq

# aqui é o arquivo onde tem toda a lógica de cadastro
cadastrar_palavras_arq.cadastrar_palavras()

# esse aqui tem toda a lógica de remover
remover_palavras_arq.remover_palavra()

def analise_de_input():
    with open('arquivo1.txt', 'r', encoding='utf-8') as arquivo:
        frutas = [linha.strip() for linha in arquivo]

    with open('arquivo2.txt', 'r', encoding='utf-8') as arquivo:
        animais = [linha.strip() for linha in arquivo]

    with open('arquivo3.txt', 'r', encoding='utf-8') as arquivo:
        comidas = [linha.strip() for linha in arquivo]

    print('*' * 30)
    print("Escolha um dos temas abaixo: \n1. Frutas\n2. Animais\n3. Comida")
    print('*' * 30)

    while True:
        try:

            escolha = int(input("Digite o número do tema que você quer jogar: "))
            print('*' * 30)
            if escolha == 1:
                palavra = random.choice(frutas)
                print("A PALAVRA FOI SORTEADA")
                print('-' * 30)
                print("DICA: Não tem nenhuma fruta que comece com Z \n")
                break
            elif escolha == 2:
                palavra = random.choice(animais)
                print("A PALAVRA FOI SORTEADA")
                print('-'*30)
                print("DICA: Não tem nenhum inseto \n")
                break
            elif escolha == 3:
                palavra = random.choice(comidas)
                print("A PALAVRA FOI SORTEADA")
                print('-' * 30)
                print("DICA: Não tem nenhum inseto \n")
                break
            else:
                print('-' * 30)
                print("DIGITE UM NÚMERO VÁLIDO: 1, 2 ou 3")
                print('-' * 30)
        except ValueError:
            print("Erro: digite um número válido (1, 2 ou 3)")

    return palavra

def processo_jogo():
    letras_usuario = []
    chances = 7
    ganhou = False
    palavra = analise_de_input()

    while chances > 0:
        letra_digitada = input("Digite uma letra: ").lower()

        if len(letra_digitada) != 1 or not letra_digitada.isalpha():
            print("Por favor, digite uma única letra válida.")
            print('*' * 30)
            continue

        if letra_digitada in letras_usuario:
            print("Você já tentou esta letra.")
            print('*' * 30)
            continue

        letras_usuario.append(letra_digitada)

        if letra_digitada in palavra:
            print(f"Boa escolha! A letra '{letra_digitada}' está na palavra.")
            print('*' * 30)
        elif letra_digitada not in palavra:
            chances -= 1
            print(f"Letra '{letra_digitada}' não está na palavra. Você tem {chances} chances restantes.")
            print('*' * 30)

        if chances == 7:
            print("BONEQUINHO")
            print("|----- ")
        elif chances == 6:
            print("BONEQUINHO")
            print("|----- ")
            print("|    | ")
        elif chances == 5:
            print("BONEQUINHO")
            print("|----- ")
            print("|    | ")
            print("|    O ")
        elif chances == 4:
            print("BONEQUINHO")
            print("|----- ")
            print("|    | ")
            print("|    O ")
            print("|   /|\\ ")
        elif chances == 3:
            print("BONEQUINHO")
            print("|----- ")
            print("|    | ")
            print("|    O ")
            print("|   /|\\ ")
            print("|    | ")
        elif chances == 2:
            print("BONEQUINHO")
            print("|----- ")
            print("|    | ")
            print("|    O ")
            print("|   /|\\ ")
            print("|    | ")
            print("|   / \\ ")
        elif chances == 1:
            print("BONEQUINHO")
            print("|----- ")
            print("|    | ")
            print("|    O ")
            print("|   /|\\ ")
            print("|    | ")
            print("|   / \\ ")
            print("_      ")

        palavra_escondida = ''.join([letra if letra in letras_usuario else '-' for letra in palavra])
        print('=' * 40)
        print(f"1:  {palavra_escondida}")
        print(f"2:  Suas tentativas {letras_usuario}")
        print(f"3:  você tem {chances} restantes")
        print('=' * 40)
        if palavra_escondida == palavra:
            ganhou = True
            break

    if ganhou:
        print(f"Parabéns, você ganhou. A palavra era: {palavra}")
    else:
        print(f"Você perdeu. A palavra era: {palavra}")

processo_jogo()
