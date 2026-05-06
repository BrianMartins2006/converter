from flask import Flask, render_template, request, jsonify
from utils.converters import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/equipe')
def equipe():
    integrantes = [
        {"nome": "Brian Martins", "funcao": "Desenvolvimento do Backend, Lógica de Decimal, Estruturação do Projeto."},
        {"nome": "Luiz Felipe S. T. A. Pereira", "funcao": "Lógica de Binário."},
        {"nome": "Nicolas Vitor Alves", "funcao": "Lógica de Hexadecimal e Integração de Testes."},
        {"nome": "Lucas Antonio Ferreira Neto", "funcao": "Lógica de Octal e Documentação Técnica."},
    ]
    return render_template('team.html', integrantes=integrantes)

@app.route('/conversor')
def conversor():
    return render_template('converter.html')

@app.route('/api/convert', methods=['POST'])
def convert():
    data = request.json
    value = data.get('value')
    from_base = data.get('from_base')
    to_base = data.get('to_base')
    
    result = ""
    
    if from_base == 'decimal':
        if to_base == 'binary': result = decimal_to_binary(value)
        elif to_base == 'hex': result = decimal_to_hexadecimal(value)
        elif to_base == 'octal': result = decimal_to_octal(value)
    elif from_base == 'binary':
        if to_base == 'decimal': result = binary_to_decimal(value)
        elif to_base == 'hex': result = binary_to_hexadecimal(value)
        elif to_base == 'octal': result = binary_to_octal(value)
    elif from_base == 'hex':
        if to_base == 'binary': result = hexadecimal_to_binary(value)
        elif to_base == 'decimal': result = hexadecimal_to_decimal(value)
        elif to_base == 'octal': result = hexadecimal_to_octal(value)
    elif from_base == 'octal':
        if to_base == 'binary': result = octal_to_binary(value)
        elif to_base == 'decimal': result = octal_to_decimal(value)
        elif to_base == 'hex': result = octal_to_hexadecimal(value)
        
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
