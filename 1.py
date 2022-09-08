"""Entrada"""
from re import sub


valor_1=int(input("Informe o primeiro valor inteiro: "))
valor_2=int(input("Informe o segundo valor inteiro: "))
codigo_operaçao=input("Informe o código da operação (+,-,* ou /): ")
"""Processo"""
soma=(valor_1+valor_2)
subt=(valor_1-valor_2)
mult=(valor_1*valor_2)
div=(valor_1/valor_2)
"""Saída"""
if (codigo_operaçao=="+"):
    print("O resultado da soma é de",int(soma))
if (codigo_operaçao=="-"):
    print("O resultado da subtração é de",int(subt))
if (codigo_operaçao=="*"):
    print("O resultado da multiplicação é de",int(mult))
if (codigo_operaçao=="/"):
    print("O resultado da diisão é de",int(div))