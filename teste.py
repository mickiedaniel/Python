a = int(input('Escreva o valor de A: '))
b = int(input('Escreva o valor de B: '))
#int transforma a entrada do input em int

soma = a+b
sub = a-b
multi = a*b
div = a/b

print('A soma de A + B é  {soma}. A subtração de A + B é  {sub}. A multiplicação de A * B é  {multi}. A divisão de A / B é  {div}' .format(soma=soma,sub=sub,multi=multi,div=div))
#format adiciona a variavel no print independente do tipo da variavel
