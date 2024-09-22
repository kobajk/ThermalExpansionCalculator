from classes.conexao_bd import ConexaoBD
from classes.materiais import Material
from classes.dao_materiais import MaterialDAO

if __name__ == "__main__":
    conexao = ConexaoBD()
    conexao.criarTabela()
    # conexao.popularTabela() # Descomente essa linha para popular a tabela
    # conexao.fecharConexao()
    