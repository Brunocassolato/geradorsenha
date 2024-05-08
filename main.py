import random
import string

tamanho = int(input("Tamanho da Senha:"))

def gerarSenha(lenght):
  caracteres = string.ascii_letters + string.digits +string.punctuation
  senha = ''.join(random.choice(caracteres) for i in range(lenght))
  return senha

print(gerarSenha(tamanho))