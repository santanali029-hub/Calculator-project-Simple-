print("Digite a operação desejada: ", 0, "Saída", 1, "Soma", 2, "Subtração", 3, "Multiplicação", 4, "Divisão")

op = int(input())

print('Escolha dois números')

num1 = int(input())
num2 = int(input())

while op == 0:
    print("Saída")
    break
if op == 1:
    print("O resultado é = ", num1 + num2)

elif op == 2:
    print("O resultado é = ", num1 - num2)

elif op == 3:
    print("O resultado é = ", num1 * num2)

elif op == 4:
    print("O resultado é = ", num1 / num2)

else:
    print("Operação Inválida")