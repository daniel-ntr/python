frase = str(input('Digite um frase qualquer: ').strip().upper())
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}')
if junto == inverso:
    print('Que legal! Esta frase é um palíndromo! ')
else:
    print('Esta frase não é um palíndromo! ')

'''frase = str(input('Digite uma frase:').strip().upper())
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso} ')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')'''

