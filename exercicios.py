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

# need to verify this
# value1 = bool(input("Type either True or False for value 1: "))
# value2 = bool(input("Type either True or False for value 2: "))
# and_result = value1 and value2
# print(f"The result of value 1 and value 2 is {and_result}")

# # Exemplo de entrada
# valor1 = True
# valor2 = True
# resultado_and = valor1 and valor2
# print("Resultado do AND lógico:", resultado_and)

# # GPT Help

# # Get input as string and standardize

# value1 = input("Type either True or False for value 1: ").strip().lower()
# value2 = input("Type either True or False for value 2: ").strip().lower()

# # Convert to actual booleans
# bool1 = value1 == "true"
# bool2 = value2 == "true"

# and_result = bool1 and bool2
# print(f"The result of value 1 and value 2 is {and_result}")

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

# valor1 = input("Digite True ou False: ").strip().lower()
# valor2 = input("Digite True ou False: ").strip().lower()

# bool1 = valor1 == "true"
# bool2 = valor2 == "true"

# resultado_or = bool1 and bool2
# print(f"O resultado do OR lógico é {resultado_or}")

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

# valor1 = input("Digite True or False: ").strip().lower()
# bool1 = valor1 == "true"
# valor1_invertido = not bool1
# print(f"O valor invertido é {valor1_invertido}")

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

# value1 = input("Digite um número: ")
# value2 = input("Digite outro número: ")

# result_equal_test = value1 == value2

# print(f"{value1} equals {value2} statement is: {result_equal_test}")

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# value1 = input("Digite um número: ")
# value2 = input("Digite outro número: ")

# result_diff_test = value1 != value2

# print(f"{value1} differs from {value2} statement is: {result_diff_test}")

# #### try-except e if

# 21: Conversor de Temperatura

# Escreva um programa que converta a temperatura de Celsius para Fahrenheit. 
# O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError. 
# Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

# try:
#     temp_celsius = float(input("Digite uma temperatura em Celsius: "))
#     temp_fahrenheit = (temp_celsius*(9/5)) + 32
#     print(f"{temp_celsius}°C equivale à {temp_fahrenheit:.2f}°F")
# except ValueError:
#     print("A temperatura deve ser um número")

# 22: Verificador de Palíndromo

# Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). 
# Utilize try-except para garantir que a entrada seja uma string. Dica: Utilize a função isinstance() para verificar o tipo da entrada.

# My solution
# word_user = input("Digite uma palavra: ")
# rev = ''.join(reversed(word_user))
# if word_user == rev:
#     print("É um palíndromo")
# else:
#     print("Não é um palíndromo")

# JD Solution
# entrada = input("Digite uma palavra ou frase: ")
# if isinstance(entrada, str):
#     formatado = entrada.replace(" ", "").lower()
#     if formatado == formatado[::-1]:
#         print("É um palíndromo.")
#     else:
#         print("Não é um palíndromo.")
# else:
#     print("Entrada inválida. Por favor, digite uma palavra ou frase.")


# 23: Calculadora Simples

# My Solution
# try:
#     num1 = float(input("Digite um número: "))
#     num2 = float(input("Digite mais um número: "))
#     operador = input("Digite um dos operadores indicados (+,-,*,/): ")
    
#     if operador == "+":
#         soma = num1 + num2
#         print(f"O resultado da soma é: {soma}")
#     elif operador == "-":
#         subtracao = num1 - num2
#         print(f"O resultado da subtração é: {subtracao}")
#     elif operador == "*":
#         multiplicacao = num1 * num2
#         print(f"O resultado da multiplicação é: {multiplicacao}")
#     elif operador == "/" and num2 != 0:
#         divisao = num1 / num2
#         print(f"O resultado da divisão é: {divisao}")
#     else:
#         print("Operador inválido ou divisão por zero.")
# except ValueError:
#     print("Por favor, digite um número para os dois primeiros campos.")

# JD Solution
# try:
#     num1 = float(input("Digite o primeiro número: "))
#     num2 = float(input("Digite o segundo número: "))
#     operador = input("Digite o operador (+, -, *, /): ")
#     if operador == '+':
#         resultado = num1 + num2
#     elif operador == '-':
#         resultado = num1 - num2
#     elif operador == '*':
#         resultado = num1 * num2
#     elif operador == '/' and num2 != 0:
#         resultado = num1 / num2
#     else:
#         print("Operador inválido ou divisão por zero.")
#     print("Resultado:", resultado)
# except ValueError:
#     print("Erro: Entrada inválida. Certifique-se de inserir números.")


# 24: Classificador de Números

# Tell if the number is positive, negative or zero, and also if it's even or odd

# My Solution

# user_number = float(input("Digite um número: "))

# try:
#     if user_number > 0:
#         sign = "positive"
#     elif user_number < 0:
#         sign = "negative"
#     else:
#         sign = "not positive nor negative"

#     if user_number % 2 == 0:
#         even_odd = "even"
#     else:
#         even_odd = "odd"

#     print(f"{user_number} is {sign}, and it's also an {even_odd} number.")
# except ValueError:
#     print("Please insert a valid number.")


# 25: Conversão de Tipo com Validação

# entrada_lista = input("Digite uma lista de números separados por vírgula: ")
# numeros_str = entrada_lista.split(",")
# numeros_int = []
# try:
#     for num in numeros_str:
#         numeros_int.append(int(num.strip()))
#     print("Lista de inteiros:", numeros_int)
# except ValueError:
#     print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")

### Desafio - Refatorar o projeto da aula anterior evitando Bugs!

# 1) Solicita ao usuário que digite seu nome
nome_usuario = input("Digite o seu nome: ")

# Handling errors
if nome_usuario.isdigit():
    print("Você digitou um número no seu nome. Por favor, tente novamente.") # Number in the name
    exit()
elif len(nome_usuario) == 0:
    print("Você enviou seu nome em branco. Por favor, tente novamente.") # Blank name
    exit()
elif nome_usuario.isspace():
    print("Você enviou seu nome em branco. Por favor, tente novamente.") # Typed only spaces
    exit()


# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
try:
    salario_usuario = float(input("Digite o seu salário: "))
except ValueError:
    print("O salário deve ser um número. Por favor, tente novamente.") # For strings, empty, or space only

# Handling errors
try:
    if salario_usuario == 0:
        print("O salário deve ser maior do que zero. Por favor, tente novamente.") # For zero salary
        exit()
    if salario_usuario < 0:
        print("O salário deve ser maior do que zero. Por favor, tente novamente.") # For negative
        exit()
except NameError:
    pass


# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
try:
    bonus_usuario = float(input("Digite o seu bônus em porcentagem: "))
except ValueError:
    print("O bônus deve ser um número. Por favor, tente novamente.") # For strings, empty, or space only

# Handling errors
try:
    if bonus_usuario == 0:
        print("O bônus deve ser maior do que zero. Por favor, tente novamente.") # For zero
        exit()
    elif bonus_usuario < 0:
        print("O bônus deve ser maior do que zero. Por favor, tente novamente.") # For negative
        exit()
except NameError:
    pass

bonus_usuario_pct = float(bonus_usuario / 100)

# 4) Calcule o valor do bônus final
kpi_bonus = 1000 + salario_usuario * bonus_usuario_pct
salario_total = salario_usuario + kpi_bonus

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"{nome_usuario}, com um salário de R${salario_usuario} e bônus de {bonus_usuario}%, o seu Bônus KPI é de R${kpi_bonus}. Seu salário total é R${salario_total}")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?

