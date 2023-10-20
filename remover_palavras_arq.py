def remover_palavra():
    opcao = input("Deseja remover alguma palavra? ").lower().strip()
    if opcao == "sim":
        print('-'*50)
        print("os arquivos são: arquivo1.txt para frutas, arquivo2.txt para animais e arquivo3.txt para comidas")
        print('-' * 50)
        arquivo = input("Digite o nome do arquivo (incluindo a extensão .txt): ")

        try:
            with open(arquivo, 'r', encoding='utf-8') as arquivo_original:
                linhas = arquivo_original.readlines()

            for i, linha in enumerate(linhas):
                palavras = linha.split()
                print(f"Palavras na linha {i + 1}: {', '.join(palavras)}")

            linha_a_modificar = int(input("Escolha o número da linha que deseja modificar: ")) - 1

            if linha_a_modificar >= 0 and linha_a_modificar < len(linhas):
                palavras_na_linha = linhas[linha_a_modificar].split()
                print(f"Palavras na linha selecionada: {', '.join(palavras_na_linha)}")

                palavra_a_remover = input("Digite a palavra que deseja remover: ").strip()

                palavras_modificadas = [palavra for palavra in palavras_na_linha if palavra != palavra_a_remover]

                linhas[linha_a_modificar] = ' '.join(palavras_modificadas)

                with open(arquivo, 'w', encoding='utf-8') as arquivo_modificado:
                    arquivo_modificado.writelines(linhas)

                print(
                    f"A palavra '{palavra_a_remover}' foi removida com sucesso da linha {linha_a_modificar + 1} do arquivo '{arquivo}'.")
            else:
                print("Número de linha inválido.")
        except FileNotFoundError:
            print(f"O arquivo '{arquivo}' não foi encontrado.")
        except Exception as e:
            print(f"Ocorreu um erro ao processar o arquivo '{arquivo}': {str(e)}")

if __name__ == "__main__":
    remover_palavra()