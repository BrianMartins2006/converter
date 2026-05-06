# Conversor de Bases Numéricas - Redes de Computadores 1

Este é um projeto desenvolvido para a disciplina de **Redes de Computadores 1**, ministrada pelo **Prof. Fábio Corsini**. O objetivo da aplicação é realizar a conversão entre diferentes bases numéricas (Decimal, Binário, Hexadecimal e Octal) utilizando algoritmos de conversão implementados manualmente, sem o uso de bibliotecas nativas de conversão do Python.

## 🚀 Tecnologias Utilizadas

- **Python 3**
- **Flask** (Framework Web)
- **HTML5 / CSS3** (Design Premium com Glassmorphism)
- **JavaScript** (Integração assíncrona e Modais)

## 📋 Pré-requisitos

Antes de começar, você precisará ter instalado em sua máquina:
- [Python 3.x](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/) (Instalador de pacotes do Python)

## 🔧 Instalação e Execução

Siga os passos abaixo para rodar o projeto localmente:

1. **Clone o repositório:**
   ```bash
   git clone git@github.com:BrianMartins2006/converter.git
   cd converter
   ```

2. **Crie um ambiente virtual (Opcional, mas recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Linux/Mac
   # venv\Scripts\activate     # No Windows
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a aplicação:**
   ```bash
   python app.py
   ```

5. **Acesse no navegador:**
   Abra o endereço [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 🧠 Lógica de Conversão

Conforme os requisitos da atividade, **não foram utilizadas** funções como `bin()`, `hex()`, `oct()` ou `int(n, base)`. Todas as conversões seguem a lógica de:
- **Decimal para outras bases:** Algoritmo de divisões sucessivas.
- **Outras bases para Decimal:** Algoritmo de soma de potências da base.

## 👥 Equipe

- **Brian Martins**: Desenvolvimento do Backend, Lógica de Decimal e Estruturação.
- **Luiz Felipe**: Lógica de Binário.
- **Nicolas Vitor Alves**: Lógica de Hexadecimal.
- **Lucas Antonio Ferreira Neto**: Lógica de Octal.

---
*Projeto desenvolvido para fins acadêmicos.*
