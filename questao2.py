num1 = int(0)
num2 = int(1)
num3 = int(0)

print("2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.# Sequência de Fibonacci")
print("==========================================================")
valor = int(input("Digite um número:"))

while valor > num3:
    num3 = num1 + num2
    num1 = num2
    num2 = num3
if valor == 0 | valor == 1:
    print("O número informado (" + str(valor) +
          ") pertence a sequência de Fibonacci.")
elif valor == num3:
    print("O número informado (" + str(valor) +
          ") pertence a sequência de Fibonacci.")
else:
    print("O número informado não pertence a sequência de Fibonacci.")
