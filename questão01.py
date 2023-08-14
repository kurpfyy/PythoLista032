'''
Desenvolver um programa que pergunte o valor da conta a ser paga no restaurante e exiba como resposta o
valor com o acréscimo dos 10% da gorjeta do garçom.
'''

conta = float(input("qual o valor da conta a ser paga?"))
gorjeta = (conta / 10)
valor = (conta + gorjeta)
print("A conta deu",conta,"então a gorjeta do garçom devera ser",gorjeta,"no total a conta sai por", valor)