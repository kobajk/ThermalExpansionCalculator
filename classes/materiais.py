class Material:
    def __init__(self, material, dilatacao, temp_max, classe):
        self.__material = material
        self.__dilatacao = dilatacao
        self.__temp_max = temp_max
        self.__classe = classe
    
    def getMaterial(self):
        return self.__material
    
    def setMaterial(self, novo_material):
        self.__material = novo_material

    def getDilatacao(self):
        return self.__dilatacao
    
    def setDilatacao(self, nova_dilatacao):
        self.__dilatacao = nova_dilatacao
    
    def getTempMax(self):
        return self.__temp_max
    
    def setTempMax(self, nova_temp_max):
        self.__temp_max = nova_temp_max

    def getClasse(self):
        return self.__classe
    
    def setClasse(self, nova_classe):
        self.__classe = nova_classe

    def exibirInfo(self):
        print(f"Classe: {self.__classe}\
                Material: {self.__material}\
                Dilatacao: {self.__dilatacao}\
                Temperatura Máxima: {self.__temp_max}")
