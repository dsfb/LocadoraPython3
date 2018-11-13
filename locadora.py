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

class OptionDBManager(object):
	def __init__(self, opt_num, opt_fun, opt_str):
		self.opt_num = opt_num
		self.opt_fun = opt_fun
		self.opt_str = opt_str


class DBManager(object):
	def __init__(self):
		pass

	def cadastrar_filme(self):
		pass

	def get_options_str(self):
		return "\r".join(["1 - Cadastrar um filme",
							"0 - Sair"])


def menu(string):
	print("Testing:");
	print(string)
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
		finally:
			return -1

def rodar():
	dbm = DBManager()
	while True:
		opcao = menu(dbm.get_options_str())
		if opcao == 1:
			dbm.cadastrar_filme()
		break

if __name__ == "__main__":
	rodar()
