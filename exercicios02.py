#1-Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
# C  = float(input("Digite o Número:"))
# if C > 0 :
#     print(C, "é positivo")
#
# else:
#     print(C, "é negativo")

# 2- Faça um Programa que peça dois números e imprima o maior deles.
# A  = float(input("Digite o primeiro Número:"))
# B = float(input("Digite o segundo Numero:"))
# if A > B :
#     print(A,"é maior")
# elif B > A:
#     print(B, "É maior")
# else:
#     print("os números são iguais")

#3-Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que C.
# A  = float(input("Digite o primeiro Número:"))
# B = float(input("Digite o segundo Numero:"))
# C = float(input("Digite o terceiro Numero:"))
#
# S = A+B
#
# if S < C :
#     print('O terceiro número é maior que a soma dos dois primeiros')
# elif S > C :
#     print('O terceiro número é menor que a soma dos dois primeiros')
# else:
#     print('O terceiro número é igual que a soma dos dois primeiros')


# 4-Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

# Sexo = input("Digite uma letra:")
# if Sexo == "f" :
#     print("Feminino")
#
# elif Sexo == "m" :
#    print("Masculino")
#
# else:
#     print("sexo invalido")

#5-Faça um Programa que peça um número inteiro e determine se ele é par ou ímpar. Dica: utilize o operador módulo

# N = int(input("Digite um número: "))
#
# if (N % 2 == 0) :
#     print("Número par.")
# else:
#     print("Número ímpar")

#6-Faça um algoritmo que leia um número e some 5 caso seja par ou some 8 caso seja ímpar. Por fim, imprima o resultado desta soma.

# N = int(input("Digite um número: "))
# if (N % 2 == 0) :
#      print(N+5)
# else:
#     print(N+8)

#7-Crie um programa que peça uma nota de trabalho e uma de prova (as duas de 0 a 100). Se a média aritmética das notas for maior ou igual a 60, escreva “Aprovado”, se não, “Reprovado”.
# nota1 = float(input("Digite a nota da prova:"))
# nota2 = float(input("Digite a nota do trabalho:"))
#
# N = nota1 + nota2 / 2
#
# if N >= 60 and N<=100 :
#      print("Aprovado")
# else:
#     print('Reprovado')

#8-Construa um algoritmo, que receba três valores, A, B e C. Em seguida, apresente na tela os números em ordem crescente.
# A  = float(input("Digite o primeiro Número:"))
# B = float(input("Digite o segundo Numero:"))
# C = float(input("Digite o terceiro Numero:"))
#
# if A>B and A>C :
#     print('O primeiro é maior dos 3 numeros')
# elif B>A and B>C :
#     print('O segundo é o maior dos 3 numeros')
# else:
#     C>A and C>B
#     print('O terceiro é o maior dos 3 numeros')

#9

#10-Uma loja está com uma promoção de 10% desconto em todos os seus produtos. Faça um programa que receba um valor, calcule e imprima o valor do desconto (em reais) e o valor final do produto após aplicar o desconto.

# preco_bruto = float(input("Digite o valor do produto:"))
# d10 = preco_bruto * (10/100)
# preco_final = preco_bruto - d10
#
# print("Final: R$", preco_bruto)
# print("Final com 10%: R$", preco_final)
