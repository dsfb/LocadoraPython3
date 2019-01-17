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


class DBCreator(object):
	def __init__(self, filename):
		self.filename = filename

		self.create()

	def create(self):
		# criando uma conexão passando o nome do arquivo
		self.conn = sqlite3.connect(self.filename)

		# obtendo um cursor
		self.c = self.conn.cursor()

	def get_conn_cursor(self):
		return self.conn, self.c

class OptionDBManager(object):
	def __init__(self, opt_num, opt_fun, opt_str):
		self.opt_num = opt_num
		self.opt_fun = opt_fun
		self.opt_str = opt_str


class DBManager(object):
	def __init__(self):
		self.option_stock_dict = {}
		self.fill_option_stock()

		creator = DBCreator('locadora.sqlite3')

		self.conn, self.c = creator.get_conn_cursor()

		self.init_tables()


	def init_tables(self):
		self.c.execute(" ".join(['CREATE TABLE IF NOT EXISTS Filme(',
								 '`id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,',
								 '`id_cliente` INTEGER, `nome`	TEXT NOT NULL,',
								 '`preco` REAL NOT NULL);']))
		self.conn.commit()
		self.c.execute(" ".join(['CREATE TABLE IF NOT EXISTS Cliente (',
								 '`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,',
								 '`nome`	TEXT NOT NULL);']))
		self.conn.commit()


	def cadastrar_filme(self):
		print("Você quer cadastrar um filme...!")

		print("Digite o nome do filme:")

		nome_filme = input()

		print("O nome inserido foi:", nome_filme)

		done = False
		while not done:
			print("Digite o preço do filme, em reais:")
			dado = input()
			try:
				preco_filme = float(dado)
				done = True
			except ValueError:
				try:
					preco_filme = float(dado.replace(',', '.'))
					done = True
				except ValueError:
					print("Você inseriu um valor errado para o preço do filme!")

		print("Filme {} cadastrado com sucesso!".format(nome_filme))


	def quit(self):
		print("Você quer sair do programa...!")
		self.finish_tables()


	def get_options_str(self):
		return "\r\n".join([s.opt_str for s in self.option_stock_dict.values()])


	def fill_option_stock(self):
		self.option_stock_dict[1] = OptionDBManager(1, self.cadastrar_filme, "1 - Cadastrar um filme")
		self.option_stock_dict[0] = OptionDBManager(0, self.quit, "0 - Sair")


	def execute_option(self, num):
		self.option_stock_dict[num].opt_fun()


	def finish_tables(self):
		self.c.close()
		self.conn.close()


def menu(string):
	qtde_opcoes_disponiveis = 2
	while True:
		print("------------------------------ Locadora GeeksBR ------------------------------")
		print("Digite o numero da opcao desejada: ")
		print(string)
		try:
			opcao = int(input())
			if opcao in [i for i in range(qtde_opcoes_disponiveis)]:
				return opcao
			else:
				print("Opção inválida! Digite uma opção válida!")
		except ValueError:
			print('Você digitou uma string inválida')
		except EOFError:
			pass


def rodar():
	dbm = DBManager()
	while True:
		opcao = menu(dbm.get_options_str())
		dbm.execute_option(opcao)
		if opcao == 0:
			break


if __name__ == "__main__":
	rodar()
