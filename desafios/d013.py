n = float(input('Salário atual: R$'))
a = (n*0.15)
sn = (n+a)
print('Seu salário atual é de R${}'.format(n))
print('Após algumas reuniões decidimos lhe dar um aumento de R${:.2f} referente à 15%'.format(a))
print('Seu novo salário será de R${:.2f}'. format(sn))
