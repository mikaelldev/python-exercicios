n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('DIgite o terceiro número: '))

if n1<n2<n3:
    print(f'{n1} é o menor e {n3} o maior')     
    
elif n2<n3<n1:
    print(f'{n2} é o menor e {n1} o maior')      
    
elif n3<n1<n2:
    print(f'{n3} é o menor e {n2} o maior')     
    
elif n3<n2<n1:
    print(f'{n3} é o menor e {n1} o maior')     