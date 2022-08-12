print("5)Escreva um programa que inverta os caracteres de um string.")
palavra = input("Digite uma palavra:")
letras = []
invertida = ''

for letra in palavra:
    letras.append(letra)

tam = len(letras) - 1

while tam >= 0:
    invertida += (letras[tam])
    tam -= 1

print("Resultado: ")
print(invertida)