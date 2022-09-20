import sqlite3

class Crud():
    def __init__(self):
        self.conexao = sqlite3.connect('data/database.db', check_same_thread=False)

    def insert(self, valor, data, descricao, tipo_pagamento, categoria):
        try:
            c = self.conexao.cursor()
            c.execute("INSERT INTO despesas (valor, data_compra, descricao, tipo_pagamento_id, categoria_id) VALUES (?, ?, ?, ?, ?)", (valor, data, descricao, tipo_pagamento, categoria))
            self.conexao.commit()
            c.close()

            return {
                'data': None, 
                "success": True
                }
        except:
            return {
                'data': None, 
                "success": False
                }

    def list(self):
        try:
            c = self.conexao.cursor()
            c.execute("SELECT dsp.valor, dsp.data_compra, dsp.descricao, tp.tipo , ct.nome FROM despesas dsp left join tipos_pagamento tp on dsp.tipo_pagamento_id = tp.id left join categorias ct on dsp.categoria_id = ct.id where strftime('%m', dsp.data_compra) = strftime('%m', 'now') order by dsp.data_compra desc")
            dados = c.fetchall()
            c.close()
            return {
                'data': dados, 
                "success": True
                }
        except:
            return {
                'data': None, 
                "success": False
                }