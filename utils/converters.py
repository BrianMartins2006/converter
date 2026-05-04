
def decimal_to_binary(n):
    """Converte Decimal para Binário (Brian)"""
    try:
        n = int(n)
        if n == 0: return "0"
        binary = ""
        while n > 0:
            binary = str(n % 2) + binary
            n //= 2
        return binary
    except ValueError:
        return "Erro: Entrada inválida"

def decimal_to_hexadecimal(n):
    """Converte Decimal para Hexadecimal (Brian)"""
    try:
        n = int(n)
        if n == 0: return "0"
        hex_chars = "0123456789ABCDEF"
        hexadecimal = ""
        while n > 0:
            hexadecimal = hex_chars[n % 16] + hexadecimal
            n //= 16
        return hexadecimal
    except ValueError:
        return "Erro: Entrada inválida"

def decimal_to_octal(n):
    """Converte Decimal para Octal (Brian)"""
    try:
        n = int(n)
        if n == 0: return "0"
        octal = ""
        while n > 0:
            octal = str(n % 8) + octal
            n //= 8
        return octal
    except ValueError:
        return "Erro: Entrada inválida"


# Todo 
def binary_to_decimal(b):
    """Converte Binário para Decimal (Brian)"""
   # TODO:
    return "Em desenvolvimento..."

def binary_to_hexadecimal(b):
    """Converte Binário para Hexadecimal (Brian)"""
    # TODO:
    return "Em desenvolvimento..."

def binary_to_octal(b):
    """Converte Binário para Octal (Brian)"""
    # TODO:
    return "Em desenvolvimento..."

def hexadecimal_to_binary(h):
    """Converte Hexadecimal para Binário (Nicolas)"""
    # TODO:
    return "Em desenvolvimento..."

def hexadecimal_to_decimal(h):
    """Converte Hexadecimal para Decimal (Nicolas)"""
    # TODO: 
    return "Em desenvolvimento..."

def hexadecimal_to_octal(h):
    """Converte Hexadecimal para Octal (Nicolas)"""
    # TODO:
    return "Em desenvolvimento..."

def octal_to_binary(o):
    """Converte Octal para Binário (Lucas)"""
    # TODO: 
    return "Em desenvolvimento..."

def octal_to_decimal(o):
    """Converte Octal para Decimal (Lucas)"""
    # TODO:
    return "Em desenvolvimento..."

def octal_to_hexadecimal(o):
    """Converte Octal para Hexadecimal (Lucas)"""
    # TODO: 
    return "Em desenvolvimento..."
