# Pede para o usuário inserir o primeiro valor da soma (input significa entrada de dados). Recebe os valores em formato de string.
# Atribui o valor digitado para a variável "valor_1"
valor_1 = input ("Digite o primeiro valor: ")

# Pede para o usuário inserir o segundo valor da soma
# Atribui o valor digitado para a variável "valor_2"
valor_2 = input ("Digite o segundo valor: ")

# Faz o cálculo do valor_1 + valor_2 e o atribbui a variável "calculo". Atenção: o "int" antes 
# das variáveis serve para transformá-las em números inteiros e possibilitar que a conta seja feita (pois quando o dado vem através de um input, ele está no formato de string).
calculo = int(valor_1) + int(valor_2)

# Pede para imprimir (função print) o texto "SOMA = " e o concatena (concatena significa juntar algo) com a variável calculo.
# Repare que a variável calculo precisa ser transformada novamente para string (str) para ser impressa junto com o texto digitado.
print ("SOMA = ", str(calculo))


valor_1 = input ("Digite o primeiro valor: ")

valor_2 = input ("Digite o segundo valor: ")

calculo = int(valor_1) + int(valor_2)

print ("SOMA = ", str(calculo))
