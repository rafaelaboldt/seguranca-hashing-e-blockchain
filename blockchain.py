# Parte 3 — Blockchain simplificada
# Criar três blocos encadeados com dados, hash anterior e hash atual. Alterar o primeiro bloco e observar o impacto.

import hashlib
from typing import List, Dict


def gerar_hash_bloco(dados: str, hash_anterior: str) -> str:
    conteudo = dados + hash_anterior
    return hashlib.sha256(conteudo.encode()).hexdigest()


def criar_blockchain() -> List[Dict[str, str]]:
    b1 = {"dados": "A paga 10 para B", "hash_anterior": "0000"}
    b1["hash_atual"] = gerar_hash_bloco(b1["dados"], b1["hash_anterior"])

    b2 = {"dados": "B paga 5 para C", "hash_anterior": b1["hash_atual"]}
    b2["hash_atual"] = gerar_hash_bloco(b2["dados"], b2["hash_anterior"])

    b3 = {"dados": "C paga 2 para A", "hash_anterior": b2["hash_atual"]}
    b3["hash_atual"] = gerar_hash_bloco(b3["dados"], b3["hash_anterior"])

    return [b1, b2, b3]


def imprimir_blockchain(chain: List[Dict[str, str]]) -> None:
    for i, b in enumerate(chain, start=1):
        print(f"Bloco {i}: Dados: '{b['dados']}', Hash Anterior: {b['hash_anterior']}, Hash Atual: {b['hash_atual']}")


def verificar_blockchain(chain: List[Dict[str, str]]) -> bool:
    for i in range(1, len(chain)):
        if chain[i]["hash_anterior"] != chain[i - 1]["hash_atual"]:
            return False
    return True


if __name__ == "__main__":
    chain = criar_blockchain()
    print("Blockchain inicial:")
    imprimir_blockchain(chain)
    print("Válida inicialmente?", verificar_blockchain(chain))

    chain[0]["dados"] = "A paga 100 para B"
    chain[0]["hash_atual"] = gerar_hash_bloco(chain[0]["dados"], chain[0]["hash_anterior"])

    print("\nApós alteração do Bloco 1 (hash recomputado somente no bloco 1):")
    imprimir_blockchain(chain)
    print("Válida após alteração?", verificar_blockchain(chain))