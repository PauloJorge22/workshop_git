def add(n1, n2):
    return n1 + n2

def multiply(n1, n2):
    return n1 * n2


def calculadora_simples():
    print("------------------------------")
    
    numero1 = float(input("Primeiro número: "))
    operador = input("Operador: ")
    numero2 = float(input("Segundo número: "))

    if operador == '+':
        resultado = add(numero1, numero2)
<<<<<<< HEAD
    
    if operador == 'x1':
        resultado = multiply(numero1, numero2)

=======
    if operador == '-':
        resultado=numero1-numero2
>>>>>>> origin/main
    else:
        print("Operador inválido.")
        return

    print("Resultado: " + str(round(resultado)))

# Executa
while True:
    calculadora_simples()
