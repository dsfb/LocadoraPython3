# -*- coding: utf-8 -*-
import sqlite3


class filme(object):
	def __init__(self, fid, id_cliente, nome, preco):
		self.id = fid
		self.id_cliente = id_cliente
		self.nome = nome
		self.preco = preco


class cliente(object):
	def __init__(self, cid, nome):
		self.cid = cid
		self.nome = nome


def menu():
	print("------------------------------ Locadora GeeksBR ------------------------------");
	print("\n\n1  - Cadastrar um filme\n");
	print("0  - Sair\n");
	print("Digite o numero da opcao: ");
	while True:
		try:
			return int(input())
		except ValueError:
			print('Você digitou uma string inválida')
		except EOFError:
			pass

def rodar():
	while True:
		opcao = menu()
		break

if __name__ == "__main__":
	rodar()
