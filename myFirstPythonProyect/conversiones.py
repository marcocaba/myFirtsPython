def hexa(numero):
    return hex(int(numero))[2:].upper()

def octal(numero):
    return oct(int(numero))[2:]

def romano(numero):
    n = int(numero)

    romanos = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    resultado = ""

    for valor, simbolo in romanos:
        while n >= valor:
            resultado += simbolo
            n -= valor
    
    return resultado


def romtodec(romano_str):
    valores_romanos = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    valor = 0
    for letra in reversed(romano_str.upper()):
        valor_actual = valores_romanos[letra]
        if valor_actual >= valor:
            total += valor_actual
        else:
            total -= valor_actual
        valor = valor_actual
        
    return total