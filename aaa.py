#camisa
print("       Olá Cliente, Seja bem vindo a loja virtual THE GREATS!\n")
print("Em nossa Loja temos várias camisas muito bonitas!\n")

olharcamisa = input("gostaria de olhar nosso catálogo? ")

camisas = ["Tak: R$58,00", "TEL: R$43,00"] 
if olharcamisa.lower() == "sim":
    print("Que bom! Nossos modelos são:")
    for n in camisas:
        print(n)
else:
    print("OK, Obrigado por visitar nossa loja! :)\n")


