def cadastrar_palavras():

    while True: # aqui definimos um pequeno looping onde se SIM ele continua o codigo, se diferente de SIM ele quebra

        palavra_cadastrada = False
        opcao = input("deseja cadastrar uma palavra? \n").strip().lower()
        if opcao == 'sim':
            print('-'*30)
            cadastrada = str(input("Insira a palavra que deseja cadastrar: ")).lower()
            print('-' * 30)
        elif opcao != "sim":

            break

        if cadastrada: # aqui ele verifica se a palavra cadastrada não está em nenhum arquivo
            with open('arquivo1.txt', 'r', encoding='utf-8') as arquivo:
                lista_verifica = arquivo.readlines() # aqui ele está lendo o arquivo linha por linha e armazena na lista(vetor)

                for linha in lista_verifica:
                    if cadastrada in linha:
                        palavra_cadastrada = True
                        print('-' * 30)
                        print("essa palavra ja foi cadastrada")
                        print('-' * 30)


            with open('arquivo2.txt', 'r', encoding='utf-8') as arquivo:
                lista_verifica1 = arquivo.readlines()

                for linha in lista_verifica1:
                    if cadastrada in linha:
                        palavra_cadastrada = True
                        print('-' * 30)
                        print("essa palavra ja foi cadastrada")
                        print('-' * 30)

            with open('arquivo3.txt', 'r', encoding='utf-8') as arquivo:
                lista_verifica2 = arquivo.readlines()

                for linha in lista_verifica2:
                    if cadastrada in linha:
                        palavra_cadastrada = True
                        print('-'*30)
                        print("essa palavra ja foi cadastrada")
                        print('-' * 30)

        if not palavra_cadastrada:
            try:
                escolha = int(input("Digite o tema onde deseja cadastrar a palavra:\n"
                                " 1-Frutas \n 2-Animais \n 3-Comidas"
                                " \n qual o tema desejado: (Se não for cadastrar apenas deixe este campo vazio): "))

                if escolha == 1:
                    with open('arquivo1.txt', 'a', encoding='utf-8') as arquivo:
                        arquivo.write(cadastrada + '\n')
                        print("Palavra cadastrada com sucesso")
                        break
                elif escolha == 2:
                    with open('arquivo2.txt', 'a', encoding='utf-8') as arquivo:
                        arquivo.write(cadastrada + '\n')
                        print("Palavra cadastrada com sucesso")
                        break
                elif escolha == 3:
                    with open('arquivo3.txt', 'a', encoding='utf-8') as arquivo:
                        arquivo.write(cadastrada + '\n')
                        print('-' * 30)
                        print(" Palavra cadastrada com sucesso")
                        print('-' * 30)
                    break
            except:
                print("aceitamos somente numeros inteiro de 1 a 3")

    if __name__ == "__main__":
        cadastrar_palavras()