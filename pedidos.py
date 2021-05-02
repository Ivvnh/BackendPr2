class pedidos:   
    def __init__(self,nombre,medicinas):
        self.nombre = nombre

        self.medicinas= medicinas
       


   
    def getNombre(self):
        return self.nombre
    
  
   
    def getMedicinas(self):
        return self.medicinas


   
    def setNombre(self, nombre):
        self.nombre = nombre
    
 
    
    def setMedicinas(self, medicinas):
        self.medicinas = medicinas

   