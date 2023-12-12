print('1=SOMA ; 2=SUBTRACAO ; 3= MULTIPLICACAO ; 4=DIVISAO ')

operacao = int(input('DIGITE SUA OPERAÇÃO: '))
n1 = int(input('DIGITE O PRIMEIRO NUMERO: '))
n2 = int(input('DIGITE O SEGUNDO NUMERO: '))

if operacao == 1:{
    print(n1 + n2)
}

elif operacao == 2:{
    print(n1 - n2)
}

elif operacao == 3:{
    print(n1 * n2)
}

elif operacao == 4:{
    print(n1 / n2)
}