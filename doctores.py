class doctores:   
    def __init__(self,nombre,apellido,nacimiento,sexo,usuario,contraseña,especialidad,telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.nacimiento = nacimiento
        self.sexo = sexo
        self.usuario = usuario
        self.contraseña = contraseña
        self.especialidad = especialidad
        self.telefono = telefono


   
    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def getNacimiento(self):
        return self.nacimiento

    def getSexo(self):
        return self.sexo     

    def getUsuario(self):
        return self.usuario
        
    def getContraseña(self):
        return self.contraseña

    def getEspecialidad(self):
        return self.especialidad

    def getTelefono(self):
        return self.telefono

  



   
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellido(self, apellido):
        self.apellido = apellido
    

    def setNacimiento(self,nacimiento):
        self.nacimiento = nacimiento

    def setSexo(self,sexo):
        self.sexo = sexo    

    def setUsuario(self,usuario):
        self.usuario = usuario
        
    def setContraseña(self,contraseña):
        self.contraseña = contraseña

    def setEspecialidad(self,especialidad):
        self.especialidad = especialidad

    def setTelefono(self,telefono):
        self.telefono = telefono

