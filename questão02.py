"""
Desenvolver um programa que faça duas perguntas: o valor referente às horas atuais e o valor referente aos
minutos atuais. Exemplo, se agora são 09:35h o usuário deverá informar como resposta às horas atuais o valor
09 e como resposta aos minutos atuais o valor 35. Em seguida o programa deverá apresentar como resposta
quantos minutos já se passaram desde às 00:00h deste dia.
"""
horas = int(input("Que Horas são?"))
min = int(input("Que Minutos são?"))

soma = (horas * 60) + min

print("desde 00:00 já se passaram",soma,"minutos")