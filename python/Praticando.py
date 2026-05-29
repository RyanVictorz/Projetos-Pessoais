n1 = float(input())
n2 = float(input())
sinal = str(input())

resultado = 0

if sinal == "*":
    resultado = n1 * n2    
elif sinal == "/":
    resultado = n1 / n2
elif sinal == "+":
    resultado = n1 + n2
elif sinal == "-":
    resultado = n1 - n2
else:
    resultado = -1 
    print("Erro: Operação inválida!")

if resultado != -1:
    print(resultado)
