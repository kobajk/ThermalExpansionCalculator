import sqlite3

class ConexaoBD:
    def __init__(self):
        try:
            self.conn = sqlite3.connect("bd/materiais.bd")
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f" Erro ao se conectar ao BD: {e}")

    def criarTabela(self):
        if self.conn:
            try:
                self.cursor.execute('''CREATE TABLE IF NOT EXISTS materiais
                                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    material VARCHAR(250) NOT NULL,
                                    dilatacao FLOAT NOT NULL,
                                    temperatura_max FLOAT NOT NULL,
                                    classe VARCHAR(250) NOT NULL)''')
            except sqlite3.Error as e:
                print(f" Erro na criação da tabela materiais: {e}")
        else:
            print(f" Falha na conexão: {e}")


    def popularTabela(self):
        matp = ['ABS', 'PP', 'PA', 'PS', 'PC']
        ap = [(90 * 10**-6), (140 * 10**-6), (110 * 10**-6), (65 * 10**-6), (67.5 * 10**-6)]
        tempmaxp = [100, 160, 160, 100, 150]
        matm = ['Alumínio', 'Cobre', 'Ouro', 'Prata', 'Titânio']
        am = [(23.6 * 10**-6), (17.6 * 10**-6), (14.2 * 10**-6), (19.8 * 10**-6), (8.64 * 10**-6)]
        tempmaxm = [660, 1084, 1064, 961.78, 1668]
        if self.conn:
            try:
                for i in range(len(matp)):
                    self.cursor.execute('''
     try:                 for i in range(len(matp)):.                                                    INSERT INTO materiais (material, dilatacao, temperatura_max, classe)
                                        VALUES (?,?,?,?)
                                        ''',(matp[i], ap[i], tempmaxp[i], 'Plástico'))
                for i in range(len(matm)):
                    self.cursor.execute('''
                                        INSERT INTO materiais (material, dilatacao, temperatura_max, classe)
                                        VALUES (?,?,?,?)
                                        ''',(matm[i], am[i], tempmaxm[i], 'Metal'))
                self.conn.commit()
            except sqlite3.Error as e:
                print(f" Erro ao popular a tabela materiais: {e}")
            

    def fecharConexao(self):
        if self.conn:
            try:
                self.conn.close()
            except sqlite3.Error as e:
                print(f"Erro ao fechar conexão: {e}")
        else:
            print(f" Falha na conexão: {e}")