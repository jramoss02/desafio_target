"""
Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
"""

def inverter_string(s):
    invertida = ""
    for i in range(len(s) - 1, -1, -1):
        invertida += s[i]
    return invertida

entrada = input("Digite uma string: ")
print("String invertida:", inverter_string(entrada))
