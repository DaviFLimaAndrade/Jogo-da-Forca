import random
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

    if __name__ == "__main__":
        analise_de_input()