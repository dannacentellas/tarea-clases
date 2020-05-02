class Mascota():
    def __init__(self,nombre,especie):
        self.nombre = nombre
        self.especie = especie

    def comer(self):
        print("Necesito croquetas")
    def salir_pasear(self):
        print("sacame a pasear")

    def __str__(self):
        return "nombre: {} ,especie {}".format(self.nombre, self.especie)


perro=Mascota("Balto","pastor aleman")
print(perro.comer())



"""class Tablets():
    def __init__(self,tipo, marca):
        self.tipo = tipo
        self.marca = marca

    def bateria(self):
        print("Necesito bateria ,CARGAME!")
    def caliente(self):
        print("yame usaste mucho, me calente!, lee algo si")

    def __str__(self):
        return "tipo: {} ,marca {}".format(self.tipo, self.marca)
        
        
ta=Tablets("S6","sony")
print(ta.bateria())
        
        """
