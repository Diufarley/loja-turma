"""
Este arquivo faz o Python encontrar o código que está na pasta src/.
Não precisa mexer nele.

Para rodar os testes, abra o terminal na pasta do projeto e digite:
    py -m unittest -v
"""
import os
import sys

PASTA_SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src")
sys.path.insert(0, PASTA_SRC)
