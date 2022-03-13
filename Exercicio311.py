# Faça um programa que solicite o preço de uma mercadoria e o percentual em desconto. Exiba o valor do desconto e o novo preço do produto.

preco_produto = float(input('Entre com o preço da mercadoria: R$ '))
desconto = float(input('Entre com o valor do desconto em %: '))
valor_desconto = preco_produto - (preco_produto * (desconto / 100))
desconto_real = preco_produto - valor_desconto
print('O valor do desconto é:R$ {}'.format(desconto_real))
preco_final = preco_produto - desconto_real
print('O preço com desconto é: R$ {}'.format(preco_final))