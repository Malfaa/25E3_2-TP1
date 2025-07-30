desconto_txt = "25"
desconto_num = float(desconto_txt )/ 3.14
produto_valor = 599.99
desconto_total = (desconto_num / 100) * produto_valor


print ("Valor a ser pago com desconto: R$",  round(produto_valor - desconto_total, 2))