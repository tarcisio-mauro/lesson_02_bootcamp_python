# # TypeError, Type Check e Type Conversion em Python

# Exemplo que causa TypeError

# resultado = len(5)

# Solução que impede que o programa termine a execução por causa do erro

# try:
#     resultado = len(5)
# except TypeError as e:
#     print(e)  # Imprime a mensagem de erro

# Exemplo de aplicação de Type Check

# numero = 10.5
# if isinstance(numero, int):
#     print("A variável é um inteiro.")
# else:
#     print("A variável não é um inteiro.")

# Exemplo de aplicação de Type Conversion

# numero_inteiro = 5
# numero_flutuante = 2.5
# # Converte o inteiro para flutuante e realiza a soma
# soma = float(numero_inteiro) + numero_flutuante
# print(soma)  # Resultado: 7.5

# Exemplo de try-except

# try:
#     # Código que pode gerar uma exceção
#     resultado = 10 / 0

#     print(resultado)
# except ZeroDivisionError:
#     # Código que executa se a exceção ZeroDivisionError for levantada
#     print("Divisão por zero não é permitida.")

# É possível encontrar listas extensas de erros comuns e preparar o código para saber lidar com esses problemas
# Esse tipo de pensamento e skill é um grande diferencial entre programadores avançados e júniors