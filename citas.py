class citas:   
    def __init__(self,id,nombre,fecha,hora,motivo,estado):
        self.nombre = nombre
        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo
        self.estado = estado
        self.id = id


   
    def getNombre(self):
        return self.nombre
    
    def getFecha(self):
        return self.fecha
    
    def getHora(self):
        return self.hora

    def getMotivo(self):
        return self.motivo

    def getEstado(self):
        return self.estado

    def getId(self):
        return self.id

    


   
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setFecha(self, fecha):
        self.fecha = fecha
    

    def setHora(self,hora):
        self.hora = hora

    def setMotivo(self,motivo):
        self.motivo = motivo    

    def setEstado(self,estado):
        self.estado = estado 

    def setId(self,id):
        self.id = id