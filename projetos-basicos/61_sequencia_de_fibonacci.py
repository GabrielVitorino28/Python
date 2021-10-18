# Programa que lê um número inteiro N e mostra na tela os N primeiros elementos de uma Sequência de Fibonacci.

nt = 2
t1 = 0
t2 = 1
t3 = t1 + t2
print('(---------- Sequência de Fibonacci ----------)')
n = int(input('Quantos termos da sequência de Fibonacci você quer mostrar? '))

if n == 1:
    print(t1, end=' -> ')
elif n == 2:
    print(t1, end=' -> ')
    print(t2, end=' -> ')
elif n > 2:
    print(t1, end=' -> ')
    print(t2, end=' -> ')
    while nt < n:
        print(t3, end=' -> ')
        t1 = t2
        t2 = t3
        t3 = t1 + t2
        nt += 1
print('(Fim)')
