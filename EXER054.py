from datetime import date
data = date.today()
maior = menor = idade = 0

for c in range(0, 7):
    ano = int(input('Em que ano você nasceu? '))
    idade = data.year - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'Há {menor} pessoas com menos de 21 anos, e {maior} com mais de 21 anos.')
