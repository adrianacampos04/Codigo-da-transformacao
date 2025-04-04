print("Olá, mundo!")

caixa= "caneta"

print(caixa)

nome= "Adriana" #String
idade= 21  # Inteiro int
altura= 1.55 # Float possui casa decimal
estudantes= True # Booleano valores logicos

print(f'nome: {nome}, idade: {idade}, altura: {altura}, estudantes: {estudantes}') #f string para concatenar strings e variavel

mensagem = 'Python e divertido' 

print(mensagem.strip()) # remove espaços em branco
print(mensagem.lower()) # transforma em minusculo
print(mensagem.upper()) # transforma em maiusculo 

nome= input("qual é o seu nome? ") # input para pegar dados do usuario
print(f'Olá {nome}, seja bem vindo(a) a introducao Python')
 
from datetime import datetime # importa biblioteca Data e Hora

nome= input("qual o seu nome? ") # input para pegar dados do usuario
agora= datetime.now()
hora_atual= agora.strftime('%H:%M:%S') # formatando a data e hora
print(f'Olá {nome}, agora são {hora_atual}')