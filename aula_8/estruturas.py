# Estrutura de Repetição
# if (se) -> Verifica se uma condição é true (verdadeira). Se for, ele exucuta o código.
# elif (senão se) -> é  usado para testar varias condições. Ele só executa se todas as condições anteriores forem falsas. 
# else (senão) -> Executa o código se a condição if for false (falsa).

# usuario_idade = 15
# # se o usuario for maio de 18 anos, eu vou passar a informação: Você é maior de idade;
# if usuario_idade >= 18:
#     print("Você é maior de idade")
# else:
#     print("Você é menor de idade")

idade = 10
if idade >= 18:
    print("Você é maior de idade")
elif idade >= 0 and idade < 17:
    print("Você é novo")
elif idade >= 70:
    print("Você é velho")
else: 
    print("Você é menor de idade")        