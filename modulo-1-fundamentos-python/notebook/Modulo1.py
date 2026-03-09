"""
# Módulo 1 – Fundamentos de Python

Este notebook apresenta os conceitos introdutórios da linguagem Python, abordando sintaxe básica, variáveis, tipos de dados, operadores,
entrada e saída de dados, estruturas condicionais, estruturas de repetição, listas, tuplas, dicionários e boas práticas de programação.
"""

# Primeiro código
print("Hello world!")

# Variáveis
nome = "Ana"
idade = 20
altura = 1.65

print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)

# Tipos de dados
idade = 25
nota = 9.5
curso = "Ciência de Dados"
aprovado = True

print(type(idade))
print(type(nota))
print(type(curso))
print(type(aprovado))

# Operadores aritméticos
a = 10
b = 5

print("Soma:", a + b)
print("Subtração:", a - b)
print("Multiplicação:", a * b)
print("Divisão:", a / b)

# Operadores relacionais e lógicos
x = 10
y = 5

print(x > y)
print(x == y)
print(x != y)
print(x > 5 and y < 10)

# Entrada e saída de dados
# nome = input("Digite seu nome: ")
# print("Olá,", nome)

nome = "Camila"
print("Olá,", nome)

# Estrutura condicional
idade = 18

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

# Condicional com elif
nota = 7

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")

# Repetição com for
for i in range(5):
    print("Número:", i)

# Repetição com while
contador = 0

while contador < 3:
    print("Contador:", contador)
    contador += 1

# Listas
frutas = ["maçã", "banana", "uva"]

print(frutas)
print(frutas[0])

frutas.append("laranja")
print(frutas)

# Tuplas
cores = ("azul", "verde", "amarelo")

print(cores)
print(cores[1])

# Dicionários
aluno = {
    "nome": "Maria",
    "idade": 21,
    "curso": "Ciência de Dados"
}

print(aluno)
print(aluno["nome"])
print(aluno["curso"])

# Exemplo integrando conceitos
alunos = ["Ana", "Bruno", "Carlos"]

for aluno in alunos:
    print("Aluno:", aluno)

"""## Boas práticas de programação

Algumas boas práticas importantes no desenvolvimento em Python são:

- utilizar nomes de variáveis claros e objetivos;
- manter a indentação correta;
- evitar códigos confusos ou desorganizados;
- adicionar comentários quando necessário;
- testar o código com frequência.

## Conclusão

Neste notebook, foram apresentados os fundamentos da linguagem Python, incluindo variáveis, tipos de dados, operadores, entrada e saída, estruturas condicionais, estruturas de repetição e estruturas de dados básicas.

Esses conceitos servirão de base para os próximos módulos do curso, especialmente para manipulação, visualização e análise de dados.
"""