from random import randint
from time import sleep
cont = 0
n = -1
num = randint(0, 100)#Computador pensar
print("\033[1;32m-=-\033[m"*26)
print('O computador gerou um número aletório entre 0 e 100, tente adivinhar qual foi!')
print("\033[1;33m-=-\033[m"*26)
while n != num:
    n = int(input('Qual a sua escolha?'))#Tenta adivinhar
    print('\033[1;34mPRECESSANDO...\033[m')
    sleep(1)
    if n == num:
        print('Parabens voce \033[1;32mACERTOU!\033[m'if n == num else 'Voce \033[1;31merrou\033[m eu pensei no número {} não no {}.'.format(num, n))
    else:
        print('\033[1;31mERROU\033[m')
        if num > n:
            print('Mais... Tente mais uma vez!')
        else:
            print('Menos.. Tente mais uma vez')
        cont += 1
        print('_'*30)
print('Você realzou {} tentantivas até acerta o numero que eu pensei.'.format(cont))
