class medicinas:   
    def __init__(self,id,nombre,precio,descripcion,cantidad):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.id=id


   
    def getNombre(self):
        return self.nombre
    
    def getPrecio(self):
        return self.precio
    
    def getDescripcion(self):
        return self.descripcion

    def getCantidad(self):
        return self.cantidad 

    def getId(self):
        return self.id 

    


   
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setPrecio(self, precio):
        self.precio = precio
    

    def setDescripcion(self,descripcion):
        self.descripcion = descripcion

    def setCantidad(self,cantidad):
        self.cantidad = cantidad    

    def setId(self,id):
        self.id = id

   