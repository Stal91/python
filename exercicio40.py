# Calculadora com while

#pedir primeiro numero
#pedir segundo numero
#pedir o operador
#fazer a operacao

while True:

    num_1 = input("Digite um numero: ")
    num_2 = input("Digite outro numero: ")
    operador = input("Digite o operador (+-/*): ")

    numeros_validos = None

    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        numeros_validos = True
    except Exception :
        numeros_validos = None
        
    if numeros_validos is None:
        print("Um ou ambos os numeros digitas sao invalidos")
        continue

    operadores_permitidos = "+-/*"

    if operador not in operadores_permitidos:
        print("Operador invalido")
        continue

    if len(operador) > 1:
        print("Digite apenas um operador. ")
        continue

    print("Realizando sua conta. Confira o resultado abaixo: ")

    if operador == "+":
        print(f"{num_1_float}+{num_2_float}=", num_1_float + num_2_float)
    elif operador == "-":
        print(f"{num_1_float}-{num_2_float}=",num_1_float - num_2_float)    
    elif operador == "/":
        print(f"{num_1_float}/{num_2_float}=",num_1_float / num_2_float)
    elif operador == "*":
        print(f"{num_1_float}*{num_2_float}=",num_1_float * num_2_float)    
    else:
        print("Se chegar aqui desligue O PC!!!")

    sair = input("Quer sair? [S]im: ").lower().startswith("s")
    
    if sair is True:
        break

