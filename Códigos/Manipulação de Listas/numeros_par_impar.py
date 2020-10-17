#Leia 20 números inteiros e armazene-os numa lista. Separe os números pares na lista PAR e os
#números ímpares na lista IMPAR. Imprima as três listas.
# # # # # # ############################## # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def par_impar(n):
    numero = []
    par = []
    impar = []
    for i in range(n):
        #add valores na lista numero
        numero.append(int(input("Digite um número: ")))
    #verifica se valor é par ou ímpar
    for v in numero:
        #se par add na lista de numero par se não na lista de impares
        if v %2 ==0:
            par.append(v)
        else:
            impar.append(v)
    print(f'A lista de números informados: {numero}')
    print(f'Dos quais esses são par: {par}')
    print(f'E esses são ímpar:{impar}')


def main():
    par_impar(20)

if __name__=='__main__':
    main()