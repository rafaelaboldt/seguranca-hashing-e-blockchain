# Parte 1 - Senhas
# Cadastro de usuário, geração de hash com salt, simulação de login e mensagem de sucesso ou erro.

import hashlib
import os

def gerar_hash_senha(senha):
    salt = os.urandom(16)
    hash_senha = hashlib.pbkdf2_hmac('sha256', senha.encode(), salt, 100000)
    return salt, hash_senha

def verificar_senha(senha_digitada, salt, hash_salvo):
    novo_hash = hashlib.pbkdf2_hmac('sha256', senha_digitada.encode(), salt, 100000)
    return novo_hash == hash_salvo


if __name__ == "__main__":
    senha_cadastro = "senha123"
    salt, hash_salvo = gerar_hash_senha(senha_cadastro)
    print("Senha cadastrada para demo: 'senha123'")
    print("Teste com senha correta:", verificar_senha("senha123", salt, hash_salvo))
    print("Teste com senha incorreta:", verificar_senha("outra_senha", salt, hash_salvo))

