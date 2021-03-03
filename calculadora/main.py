from operations import operations

def calcular(a, b, operador):
    return operations[operador](a, b)

if __name__ == '__main__':
    operadores = list(operations.keys())
    a = int(input('Digite o primeiro dígito: '))
    operador = input(f'Operadores disponíveis: {operadores}. Digite o operador: ')
    b = int(input('Digite o segundo dígito: '))
    resultado = calcular(a, b, operador)
    print(f'{a} {operador} {b} = {resultado}')

