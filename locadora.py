# -*- coding: utf-8 -*-
import sqlite3
import sys


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
        self.cur = self.conn.cursor()

    def get_conn_cursor(self):
        return self.conn, self.cur


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

        self.conn, self.cur = creator.get_conn_cursor()

        self.init_tables()


    def init_tables(self):
        self.cur.execute(" ".join(['CREATE TABLE IF NOT EXISTS Filme(',
                                   '`id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,',
                                   '`id_cliente` INTEGER, `nome`    TEXT NOT NULL,',
                                   '`preco` REAL NOT NULL);']))
        self.conn.commit()

        self.cur.execute(" ".join(['CREATE TABLE IF NOT EXISTS Cliente (',
                                   '`id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,',
                                   '`nome`  TEXT NOT NULL);']))
        self.conn.commit()


    def cadastrar_filme(self):
        print("Você quer cadastrar um filme...!")

        done = False
        while not done:
            print("Digite o nome do filme:")
            nome_filme = input()
            done = len(nome_filme) > 0
            if not done:
                print("Você não digitou o nome do filme!")

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

        try:
            self.cur.execute("INSERT INTO Filme(nome, preco) VALUES ('{}', {})".
                             format(nome_filme, preco_filme))
            self.conn.commit()

            print("Filme {} cadastrado com sucesso!".format(nome_filme))
        except sqlite3.Error as e:
            print("Erro ao cadastrar o filme!")
            if self.conn:
                self.conn.rollback()
            print('Abortando a execução do programa!')
            sys.exit(1)


    def cadastrar_cliente(self):
        print("Você quer cadastrar um cliente...!")

        done = False
        while not done:
            print("Digite o nome do cliente:")
            nome_cliente = input()
            done = len(nome_cliente) > 0
            if not done:
                print('Você não digitou o nome do cliente!')

        print("O nome inserido foi:", nome_cliente)

        try:
            self.cur.execute("INSERT INTO Cliente(nome) VALUES ('{}')".
                             format(nome_cliente))
            self.conn.commit()
            print("Cliente {} cadastrado com sucesso!".format(nome_cliente))
            # print("ID deste cliente: {}".format(id_cliente))
        except sqlite3.Error as e:
            print('Erro ao cadastrar o cliente!')
            if self.conn:
                self.conn.rollback
            print('Abortando a execução do programa!')
            sys.exit(1)


    def listar_filmes(self):
        print('Você quer listar todos os filmes...!')

        self.cur.execute("SELECT * FROM Filme")

        rows = self.cur.fetchall()

        if rows:
            for row in rows:
                print("----------------")
                print("ID do filme: {}".format(row[0]))
                print("Nome do filme: {}".format(row[2]))
                print("Preco: R$ {:.2f}".format(float(row[3])))
        else:
            print("Nenhum filme cadastrado.")


    def listar_clientes(self):
        pass


    def quit(self):
        print("Você quer sair do programa...!")
        self.finish_tables()


    def get_options_str(self):
        return "\r\n".join([self.option_stock_dict[k].opt_str for k in sorted(self.option_stock_dict.keys())])


    def fill_option_stock(self):
        self.option_stock_dict[3] = OptionDBManager(3, self.listar_filmes, '3  - Listar todos os filmes')
        self.option_stock_dict[2] = OptionDBManager(2, self.cadastrar_cliente, "2  - Cadastrar um cliente")
        self.option_stock_dict[1] = OptionDBManager(1, self.cadastrar_filme, "1  - Cadastrar um filme")
        self.option_stock_dict[0] = OptionDBManager(0, self.quit, "0  - Sair")


    def execute_option(self, num):
        self.option_stock_dict[num].opt_fun()


    def finish_tables(self):
        self.cur.close()
        self.conn.close()

    def get_size_option_stock(self):
        return len(self.option_stock_dict.keys())


def menu(dbm):
    string = dbm.get_options_str()
    qtde_opcoes_disponiveis = dbm.get_size_option_stock()
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
        opcao = menu(dbm)
        dbm.execute_option(opcao)
        if opcao == 0:
            break


if __name__ == "__main__":
    rodar()
