import math
import statistics

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

# numero_1 = int(input("inserir um número inteiro: "))
# numero_2 = int(input("inserir outro número inteiro: "))
# resultado = numero_1 + numero_2
# print(f"O resultado da soma é {resultado}")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

# numero_usuario = float(input("Insira um número: "))
# CTE_DIVISAO = 5
# resultado = numero_usuario % CTE_DIVISAO
# print(f"O resto da divisão por {CTE_DIVISAO} do número inserido é {resultado}")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

# numero_1 = int(input("Insira  um número inteiro: "))
# numero_2 = int(input("Insira outro número inteiro: "))
# resultado_multiplicacao = numero_1 * numero_2
# print(f"O resultado da multiplicação entre os números é {resultado_multiplicacao}")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

# try:
#     numero_1 = int(input("inserir um número inteiro: "))
#     numero_2 = int(input("inserir outro número inteiro: "))
#     resultado = numero_1 // numero_2
#     print(resultado)
# except ZeroDivisionError:
#     print("integer division or module by zero")
# except KeyboardInterrupt:
#     print("Acho que você não quis inserir um número")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# numero_usuario = int(input("Insira um número inteiro: "))
# CTE_POTENCIA = 2
# resultado = numero_usuario ** CTE_POTENCIA
# print(f"O número {numero_usuario} elevado ao quadrado é {resultado}.")

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

# numero_1 = float(input("Insira um número: "))
# numero_2 = float(input("Insira outro número: "))
# resultado = numero_1 + numero_2
# print(f"A soma dos números {numero_1} e {numero_2} é {resultado}.")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

# numero_1 = float(input("Insira um número: "))
# numero_2 = float (input("Insira outro número: "))
# numbers = [numero_1, numero_2]
# resultado = statistics.mean(numbers)
# print(f"A média dos números é {resultado}")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

# base_usuario = float(input("Insira um número para a base: "))
# expoente_usuario = float(input("Insira um número para o expoente: "))
# resultado = base_usuario ** expoente_usuario
# print(f"{base_usuario}^({expoente_usuario}) = {resultado}")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

# temp_celsius = float(input("Digite uma temperatura em Celsius: "))
# temp_fahrenheit = (temp_celsius*(9/5)) + 32
# print(f"{temp_celsius}°C equivale à {temp_fahrenheit:.2f}°F")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

# raio_do_circulo = float(input("Digite o raio do círculo: "))
# area_do_circulo = math.pi * raio_do_circulo ** 2
# print(f"{area_do_circulo:.2f}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

# string1_usuario = str(input("Digite um texto: "))
# string1_maiuscula = string1_usuario.upper()
# print(f"Texto em letras maiúsculas: {string1_maiuscula}")

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

# nome_usuario = str(input("Digite o seu nome completo: "))
# nome_minusculo = nome_usuario.lower()
# print(f"Nome minúsculo: {nome_minusculo}")

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

# texto_usuario = str(input("Digite um texto com espaços no início ou final: "))
# texto_trimmed = texto_usuario.strip()
# print(f"Texto corrigido: {texto_trimmed}")

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

# data_do_usuario = input("Insira uma data no formato dd/mm/aaaa: ")
# lista_dia_mes_ano = data_do_usuario.split("/")
# print(f"Dia: {lista_dia_mes_ano[0]}")
# print(f"Mês: {lista_dia_mes_ano[1]}")
# print(f"Ano: {lista_dia_mes_ano[2]}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# texto1_usuario = str(input("Digite o primeiro texto: "))
# texto2_usuario = str(input("Digite o segundo texto: "))
# texto_concatenado = texto1_usuario + texto2_usuario
# print(f"Esse é o texto concatenado: {texto_concatenado}")

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação
