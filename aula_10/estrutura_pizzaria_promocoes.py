# Variaveis da pizzaria
FRETE = 2 #Constante Fake em Python
pizza_sabor = input("Informe o sabor da pizza - [frango com requeijão], [calabresa], [mussarela], [banana com chocolate]: ")
pizza_tamanho = input("Informe o tamanho da pizza - [pequena], [media], [grande]: ")
dia_semana = input("Informe o dia da semana -[domingo],[quarta],[quinta],[sexta],[sabado]: ")

print(f"O sabor da pizza escolhido é {pizza_sabor} e o tamanho da pizza é {pizza_tamanho} e hoje é {dia_semana}")
# Promoções -> Estruturas condicionais
# Comprando qualquer pizza e qualquer tamanho no sábado, o refri é gratuito.

if dia_semana == "sabado":
    print(f"Pedido aceito com sucesso!")
    print(f"O Refri hoje é por conta da casa!")
# Comprando qualquer pizza de qualquer tamanho no domingo, o frete e o refri é gratis

elif dia_semana == "domingo":
    print(f"Pedido aceito com sucesso!")
    print(f"O Frete e o Refri hoje são por conta da casa!")
# Comprando uma pizza de calabresa tamanho médio, em qualquer dia, o frete é gratis

elif pizza_sabor == "calabresa" and pizza_tamanho == "media":
    print(f"Pedido aceito com sucesso!")
    print(f"O Frete hoje é por conta da casa!")
    