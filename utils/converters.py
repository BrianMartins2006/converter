
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
    """Converte Binário para Decimal (Luiz)"""
    try:
        resultado = 0
        
        for digito in b:
            if digito not in '01':
                return "Erro: número binário inválido"
            
            resultado = resultado * 2 + int(digito)
        
        return resultado
    except ValueError:
        return "Erro: Entrada inválida"


def binary_to_hexadecimal(b):
    try:
        resultado = 0
        hex_chars = "0123456789ABCDEF"
        
        # binário → decimal
        for digito in b:
            if digito not in '01':
                return "Erro: número binário inválido"
            
            resultado = resultado * 2 + int(digito)
        
        # decimal → hexadecimal
        if resultado == 0:
            return "0"
        
        hexadecimal = ""
        while resultado > 0:
            hexadecimal = hex_chars[resultado % 16] + hexadecimal
            resultado //= 16
        
        return hexadecimal
    
    except ValueError:
        return "Erro: Entrada inválida"

def binary_to_octal(b):
    try:
        resultado = 0
        oct_chars = "012345678"
        
        # binário → decimal
        for digito in b:
            if digito not in '01':
                return "Erro: número binário inválido"
            
            resultado = resultado * 2 + int(digito)
        
        # decimal → octal
        if resultado == 0:
            return "0"
        
        octal = ""
        while resultado > 0:
            octal = oct_chars[resultado % 8] + octal
            resultado //= 8
        
        return octal
    
    except ValueError:
        return "Erro: Entrada inválida"


def hexadecimal_to_binary(h):
    """Converte Hexadecimal para Binário (Nicolas)"""
    try:
        # hexadecimal → decimal
        decimal = hexadecimal_to_decimal(h)
        if isinstance(decimal, str):
            return decimal  # erro
        
        # decimal → binário
        if decimal == 0:
            return "0"
        
        binary = ""
        while decimal > 0:
            binary = str(decimal % 2) + binary
            decimal //= 2
        
        return binary
    
    except ValueError:
        return "Erro: Entrada inválida"
    
def hexadecimal_to_decimal(h):
    """Converte Hexadecimal para Decimal (Nicolas)"""
    try:
        h = h.upper()
        hex_chars = "0123456789ABCDEF"
        resultado = 0
        
        for digito in h:
            if digito not in hex_chars:
                return "Erro: número hexadecimal inválido"
            
            valor = hex_chars.index(digito)
            resultado = resultado * 16 + valor
        
        return resultado
    
    except ValueError:
        return "Erro: Entrada inválida"

def hexadecimal_to_octal(h):
    """Converte Hexadecimal para Octal (Nicolas)"""
    try:
        # hexadecimal → decimal
        decimal = hexadecimal_to_decimal(h)
        if isinstance(decimal, str):
            return decimal  # erro
        
        # decimal → octal
        if decimal == 0:
            return "0"
        
        octal = ""
        while decimal > 0:
            octal = str(decimal % 8) + octal
            decimal //= 8
        
        return octal
    
    except ValueError:
        return "Erro: Entrada inválida"

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
