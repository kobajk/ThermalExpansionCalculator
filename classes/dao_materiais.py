# data access object

class MaterialDAO:
    def __init__(self, conexao):
        self.conn = conexao
        self.cursor = conexao.cursor
    
    def inserirMaterial(self, material):
        self.cursor.execute('''
                            INSERT INTO 
                            materiais (material, dilatacao, temperatura_max, classe)
                            VALUES 
                            (?,?,?,?)
                            ''',(material.getMaterial(), material.getDilatacao(), material.getTempMax(), material.getClasse()))
        self.conn.commit()
    
    def deletarMaterial(self, material):
        self.cursor.execute('''
                            DELETE FROM materiais
                            WHERE material = ?
                            ''',(material.getMaterial(),))
        self.conn.commit()

    def atualizarMaterial(self, material):
        self.cursor.execute('''
                            UPDATE materiais
                            SET dilatacao = ?, temperatura_max = ?, classe = ?
                            WHERE material = ?
                            ''',(material.getDilatacao(), material.getTempMax(), material.getClasse(), material.getMaterial()))
        self.conn.commit()

    def buscarMaterial(self, material):
        self.cursor.execute('''
                            SELECT * FROM materiais
                            WHERE material = ?
                            ''',(material.getMaterial(),))
        material_sel = self.cursor.fetchone()
        return material_sel

    def listarMateriais(self):
        self.cursor.execute('''SELECT * FROM materiais''')
        materiais = self.cursor.fetchall()
        return materiais