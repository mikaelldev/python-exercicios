print('Viagens até 200 km custam 0,50 por km, já maior que isso custa 0,30 por km')

km = float(input('Qual a distância da viagem em [km]??: '))

if km <= 200:
    print(f'sua passagem custou: {km*0.50}')
    
else:
    print(f'sua passagem custou: {km*0.30}')    