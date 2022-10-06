from flask import json, jsonify, request
import sqlite3
import os

def Listardespesas():
	ROOT_DIR = os.getcwd()
	DB_URL = os.path.join(ROOT_DIR, 'data', 'database.db')
	conexao =  sqlite3.connect(DB_URL)
	cursor = conexao.cursor()
	query = """SELECT * FROM despesas"""
	cursor.execute(query)
	rows = cursor.fetchall()
	despesas = []
	for row in rows:
		t = (row[0], row[1], row[2], row[3], row[4], row[5])
		despesas.append(t)
	responseBody = {
        "data": despesas,
		"status": True
    }
	return jsonify(responseBody)

def Cadastrardespesa():
	valor = request.form.get('valor')
	data_compra = request.form.get('data_compra')
	descricao = request.form.get('descricao')
	tipo_pagamento_id = request.form.get('tipo_pagamento_id')
	categoria_id = request.form.get('categoria_id')
	ROOT_DIR = os.getcwd()
	DB_URL = os.path.join(ROOT_DIR, 'data', 'database.db')
	conexao =  sqlite3.connect(DB_URL)
	cursor = conexao.cursor()
	query = """INSERT INTO despesas (valor, data_compra, descricao, tipo_pagamento_id, categoria_id) VALUES (?, ?, ?, ?, ?)"""
	cursor.execute(query, [valor, data_compra, descricao, tipo_pagamento_id, categoria_id])
	conexao.commit()
	responseBody = {
        "data": int(cursor.lastrowid),
		"status": True
    }
	cursor.close()
	return jsonify(responseBody)