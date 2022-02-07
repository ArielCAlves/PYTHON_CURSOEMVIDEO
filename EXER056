## Perguntas a serem respondidas ##
# 1) Qual é a média de idades?
# 2) Qual é o nome do homem mais velho?
# 3) Quais são os nomes das mulheres com menos de 20 anos.

# bibliotecas utilizadas
import pandas as pd
import warnings
warnings.filterwarnings("ignore")


lista_nome = []
lista_idd = []
lista_sexo = []

while True:
    nome = input('Digite o nome: ').strip().title()
    idd = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Digite o sexo (M/F): ').strip().upper()[0]

    lista_nome.append(nome)
    lista_idd.append(idd)
    lista_sexo.append(sexo)

    print('Deseja continuar preenchendo?')
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Digite Sim ou Não: ').strip().upper()[0]
    if resposta == 'N':
        break

# criação do dataframe para trabalhar com linhas e colunas
df = pd.DataFrame({
                    'Nome': lista_nome,
                    'Idade': lista_idd,
                    'Sexo': lista_sexo
})

# média de idades
media = df['Idade'].mean()

# subset para identificar os que são homens
homem = df.loc[(df['Sexo'] == 'M')]
homem.drop(['Sexo'], axis=1, inplace=True)

print('#'*60)
print(f'A média de idade destas pessoas é de {media:.1f}.\n')

print('#'*60)
print(f'Homem mais velho é: {homem.max()}.\n')

# poderia fazer subset aqui também, porém quis mostrar outra forma de consulta
print('#'*60)
print(f'''Mulheres com idade inferior a 20 anos
{df.query('Idade < 20 & Sexo=="F"')}.''')
