class Objeto:
    def __init__(self, nome):
        self._nome = nome
    
    def getNome(self):
        return self._nome
    
    def setNome(self, nome):
        self._nome = nome

class Cilindro(Objeto):
    def __init__(self, nome, raio, altura):
        super().__init__(nome)
        self._raio = raio
        self._altura = altura
    
    def getRaio(self):
        return self._raio
    
    def setRaio(self, raio):
        self._raio = raio
    
    def getAltura(self):
        return self._altura
    
    def setAltura(self, altura):
        self._altura = altura

    def calcularVolume(self):
        return 3.14 * (self._raio ** 2) * self._altura
    
class Poligono(Objeto):
    def __init__(self, nome, comprimento, largura, altura):
        super().__init__(nome)
        self._comprimento = comprimento
        self._largura = largura
        self._altura = altura
    
    def getComprimento(self):
        return self._comprimento
    
    def setComprimento(self, comprimento):
        self._comprimento = comprimento

    def getLargura(self):
        return self._largura
    
    def setLargura(self, largura):
        self._largura = largura

    def getAltura(self):
        return self._altura
    
    def setAltura(self, altura):
        self._altura = altura

    def calcularVolume(self):
        return self._comprimento * self._largura * self._altura