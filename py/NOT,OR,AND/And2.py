peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = (peso/altura**2)

if imc <= 18.5:
    print('Abaixo do peso,kkkkkkkkkk')
    
elif imc >= 18.5 and imc <=24.9:
    print('Peso normal,brabo dms')   

elif imc >= 25 and imc <=29.9:
    print('Sobre peso,kkkkkkkcria vergonha na carakkkkkkk')
    
else:
    print('OBESIDADE,KAKAKAKAKAKKAKKAKAKAKAKKAKAKAKAKAKAKAKAKAKAAKAKAKAKAKKAKA')         