from ex0107 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda(p)} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos: {moeda.aumentando(p,10)}')
print(f'Reduzindo 13%, temos: {moeda.reduzindo(p,13)}')
