#usando while para preencher lista, flag se o valor for 0
l =[]
while True:
    n = int(input("Digite um número (0 para sair): "))
    if n ==0:
        break
    l.append(n)
#imprime os números add na lista l
for i in l:
    print(i)