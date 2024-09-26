from random import randint,seed

matriz1 = []
matriz2 = []

#   manter os mesmos numeros aleatorios
seed(5)

#   Função para a entrada de dados
def Digite_numeros(matriz):
    matriz.clear()
    for i in range(3):
        linha = []
        for j in range(3):
            while True:
                try:
                    n = int(input(f'Digite o numero correspondente da coordenada({i},{j}): '))
                    linha.append(n)
                    break
                except ValueError:
                    print("Por favor, digite um número válido.")

        matriz.append(linha)
    return matriz

#   Função que gera aleatoriamento os numeros das matrizes
def Gerar_matriz(matriz):
    matriz.clear()
    for _ in range(3):
        linha = []
        for _ in range(3):
            n = randint(0,10)
            linha.append(n)
        matriz.append(linha)
    return matriz

#   Função para transpor matriz    
def Transposicao_matriz(matriz):
    
    return [[matriz[j][i] for j in range(3)] for i in range(3)]

#   Função que soma as matrizes
def Somar_matrizes(matriz1,matriz2):
    
     return [[matriz1[j][i] + matriz2[i][j] for j in range(3)] for i in range(3)]

#   Função para multiplicar as matrizes
def multiplicar_matrizes(matriz1, matriz2):
    matriz_produto = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                matriz_produto[i][j] += matriz1[i][k] * matriz2[k][j]
    return matriz_produto

#   Função para visualizar as matrizes
def imprimir_matriz(matriz):
    for linha in matriz:
         print(" ".join(map(str, linha)))

#   Menu
while True:
        print("\nMenu:")
        print("1. Digitar Matriz 1")
        print("2. Gerar Matriz 2 aleatoriamente")
        print("3. Transpor Matriz 1")
        print("4. Somar Matrizes")
        print("5. Multiplicar Matrizes")
        print("6. Imprimir Matrizes")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print('Matriz A')
            Digite_numeros(matriz1)
            
            print('Matriz B')
            Digite_numeros(matriz2)
            
            print('     A')
            imprimir_matriz(matriz1)
            
            print('     B')
            imprimir_matriz(matriz2)
        
        elif opcao == '2':
            Gerar_matriz(matriz1)
            Gerar_matriz(matriz2)
            
            print("\nMatriz A e B (gerada aleatoriamente):")
            imprimir_matriz(matriz1)
            imprimir_matriz(matriz2)
        
        elif opcao == '3':
            if matriz1:
                matriz_transposta = Transposicao_matriz(matriz1)
                print("\nMatriz A Transposta:")
                imprimir_matriz(matriz_transposta)
            else:
                print("Você deve primeiro digitar a Matriz 1.")
        
        elif opcao == '4':
            if matriz1 and matriz2:
                matriz_soma = Somar_matrizes(matriz1, matriz2)
                print("\nMatriz Soma:")
                imprimir_matriz(matriz_soma)
            else:
                print("Você deve primeiro digitar a Matriz 1 e a Matriz 2.")
        
        elif opcao == '5':
            if matriz1 and matriz2:
                matriz_produto = multiplicar_matrizes(matriz1, matriz2)
                print("\nMatriz Produto:")
                imprimir_matriz(matriz_produto)
            else:
                print("Você deve primeiro digitar a Matriz 1 e gerar a Matriz 2.")
        elif opcao == '6':
            print("\nMatriz A:")
            imprimir_matriz(matriz1)
            print("\nMatriz B:")
            imprimir_matriz(matriz2)
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
