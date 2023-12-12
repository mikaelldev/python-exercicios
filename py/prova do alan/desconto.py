produto_valor = float(input('Digite o valor do produto desejado: '))

print(f'seu produto vale {produto_valor}')
print('escolha a opção de desconto desejada: ')
print('  Digite [1] para pagar no pix/dinheiro e fique com 10 porcento de desconto')
print('  Digite [2] para pagar a vista no cartão e fique com 5 porcento de desconto')
print('  Digite [3] para pagar em 2x no cartão de crédito: preço normal')
print('  Digite [4] para pagar 3x no cartão: 20 porcento de juros')

pagamento = int(input('Digite sua forma de pagmento: '))

if pagamento == 1:
    print(f'seu produto custa em R$: { produto_valor - (produto_valor*10)/100}')

elif pagamento == 2:
    print(f'seu produto custa em R$: { produto_valor - (produto_valor*5)/100}')
    
elif pagamento == 3:
    print(f'seu produto foi divido em 2 partes de : {produto_valor/2} R$')
    
else:
    print(f'seu produto custa em R$: {(produto_valor*20)/100 + produto_valor}')    

        
    