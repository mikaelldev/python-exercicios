print('Bem vindo a bilheteria') 

preco = 100
dinheiro = int(input('Digite seu saldo atual:  '))
idade = int(input('Digite sua idade: '))   

if (dinheiro >= preco) and (idade >= 18):{
    print('Ingresso comprado com sucesso')
}

else:
    print('Não está no padrão da compra')