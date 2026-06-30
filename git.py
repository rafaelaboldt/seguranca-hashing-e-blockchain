"""Parte 2 - Git simplificado
Função que recebe conteúdo de arquivo e gera hash. Testa duas versões distintas.
"""

import hashlib


def gerar_hash_conteudo(conteudo: str) -> str:
	return hashlib.sha1(conteudo.encode()).hexdigest()


if __name__ == "__main__":
	conteudo1 = "Olá turma"
	conteudo2 = "Olá turma!"

	hash1 = gerar_hash_conteudo(conteudo1)
	hash2 = gerar_hash_conteudo(conteudo2)

	print(f"Hash da versão 1: {hash1}")
	print(f"Hash da versão 2: {hash2}")
	print("Hashes iguais?", hash1 == hash2)