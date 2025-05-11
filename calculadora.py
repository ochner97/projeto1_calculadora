# Projeto #1 - Calculadora

# mensagem1
print("Projeto #1 - Calculadora")
print("Você pode somar (+), subtrair (-), multiplicar (*) ou dividir (/)")

# Pergunta o primeiro número
num1 = float(input("Digite o primeiro número: "))
#Lembrando que o input serve para pedir ao usuário digitar algo
#O float faz com que a num1 seja um número decimal

# Pergunta a operação
operacao = input("Digite a operação (+, -, *, /): ")

# Pergunta o segundo número
num2 = float(input("Digite o segundo número: "))

#Cálculo
if operacao == "+":
    result = num1 + num2
elif operacao == "-":
    result = num1 - num2
elif operacao == "*":
    result = num1 * num2
elif operacao == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Erro! Divisão por zero."
else:
    result = "Operação inválida."

print("Resultado:", result) 