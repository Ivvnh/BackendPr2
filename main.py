from flask import Flask, jsonify, request
from flask_cors import CORS
from pacientes import pacientes
from doctores import doctores
from enfermeras import enfermeras
from medicinas import medicinas
from citas import citas
from pedidos import pedidos

import json 


#Arreglos

Pacientes = []
Doctores = []
Enfermeras =[]
Medicamentos=[]
Citas=[]
Pedidos=[]
enfermedades=[]

#contadores
contadormedica=0
contadorpedidos=0
contadorcita=0

enfermedades.append('Gripe')
enfermedades.append('Fractura')
enfermedades.append('Cancer')
enfermedades.append('Gastritits')
enfermedades.append('Infeccion estomacal')
enfermedades.append('Covid-19')



app = Flask(__name__)
CORS(app)



#obtner todos los pacientes
@app.route('/Pacientes', methods=['GET'])
def getPacientes():
    global Pacientes
    Datos = []
    for pacientes in Pacientes:
        objeto = {
            'Nombre': pacientes.getNombre(),
            'Apellido': pacientes.getApellido(),
            'Fecha_de_nacimiento': pacientes.getNacimiento(),
            'Sexo': pacientes.getSexo(),
            'Nombre_de_usuario': pacientes.getUsuario(),
            'Contrasena': pacientes.getContraseña(),
            'Telefono': pacientes.getTelefono(),
        }
        Datos.append(objeto)
    return(jsonify(Datos))


#obtener solo un paciente
@app.route('/Pacientes/<string:nombre>', methods=['GET'])
def ObtenerPaciente(nombre): 
    global Pacientes
    for pacientes in Pacientes:
        if pacientes.getUsuario() == nombre:
            objeto = {
            'Nombre': pacientes.getNombre(),
            'Apellido': pacientes.getApellido(),
            'Fecha_de_nacimiento': pacientes.getNacimiento(),
            'Sexo': pacientes.getSexo(),
            'Nombre_de_usuario': pacientes.getUsuario(),
            'Contrasena': pacientes.getContraseña(),
            'Telefono': pacientes.getTelefono(),
            }
            return(jsonify(objeto))
    salida = { "Mensaje": "No existe el usuario con ese nombre"}
    return(jsonify(salida))

#guardar un nuevo paciente
@app.route('/Nuevopaciente', methods=['POST'])
def Agregarpaciente():
    global Pacientes
    global Doctores 
    global Enfermeras
    nombre = request.json['Nombre']
    apellido = request.json['Apellido']
    nacimiento = request.json['Fecha_de_nacimiento']
    sexo = request.json['Sexo']
    usuario = request.json['Nombre_de_usuario']
    contraseña = request.json['Contrasena']
    telefono = request.json['Telefono']
    buscado = False
    for i in range(len(Pacientes)):
        if usuario == Pacientes[i].getUsuario():
            buscado = True
            return jsonify({'Mensaje':'El nombre de usuario ya existe'})
        else:
            for i in range(len(Doctores)):
                if usuario == Doctores[i].getUsuario():
                    buscado = True
                    return jsonify({'Mensaje':'El nombre de usuario ya existe'})
                else:
                    for i in range(len(Enfermeras)):
                        if usuario == Enfermeras[i].getUsuario():
                            buscado = True
                            return jsonify({'Mensaje':'El nombre de usuario ya existe'})
    nuevop = pacientes(nombre,apellido,nacimiento,sexo,usuario,contraseña,telefono)
    Pacientes.append(nuevop)
    return jsonify({'Mensaje':'Se agrego el usuario correctamente',})


# actualizar paciente
@app.route('/Actualizarpaciente/<string:nombre>', methods=['PUT'])
def ActualizarPaciente(nombre):
    global Pacientes
    for i in range(len(Pacientes)):
        if nombre == Pacientes[i].getUsuario():
            Pacientes[i].setNombre(request.json['Nombre'])
            Pacientes[i].setApellido(request.json['Apellido'])
            Pacientes[i].setNacimiento(request.json['Fecha_de_nacimiento'])
            Pacientes[i].setSexo(request.json['Sexo'])
            Pacientes[i].setUsuario(request.json['Nombre_de_usuario'])
            Pacientes[i].setContraseña(request.json['Contrasena'])
            Pacientes[i].setTelefono(request.json['Telefono'])
            return jsonify({'Mensaje':'Se actualizo la informacion correctamente'})
    return jsonify({'Mensaje':'No se encontro el dato'})

# eliminar paciente
@app.route('/Eliminarpaciente/<string:nombre>', methods=['DELETE'])
def EliminarPaciente(nombre):
    global Pacientes
    for i in range(len(Pacientes)):
        if nombre == Pacientes[i].getUsuario():
            del Pacientes[i]
            return jsonify({'Mensaje':'Se elimino el paciente correctamente'})
    return jsonify({'Mensaje':'No se encontro el dato'})

#----------------------------------------------------------------------------------------------------------------------------------------
#obtner todos los doctores
@app.route('/Doctores', methods=['GET'])
def getDoctores():
    global Doctores
    Datos = []
    for doctores in Doctores:
        objeto = {
            'Nombre': doctores.getNombre(),
            'Apellido': doctores.getApellido(),
            'Fecha_de_nacimiento': doctores.getNacimiento(),
            'Sexo': doctores.getSexo(),
            'Nombre_de_usuario': doctores.getUsuario(),
            'Contrasena': doctores.getContraseña(),
            'Especialidad': doctores.getEspecialidad(),
            'Telefono': doctores.getTelefono(),
        }
        Datos.append(objeto)
    return(jsonify(Datos))


#obtener solo un doctor
@app.route('/Doctores/<string:nombre>', methods=['GET'])
def ObtenerDoctor(nombre): 
    global Doctores
    for doctores in Doctores:
        if doctores.getUsuario() == nombre:
            objeto = {
            'Nombre': doctores.getNombre(),
            'Apellido': doctores.getApellido(),
            'Fecha_de_nacimiento': doctores.getNacimiento(),
            'Sexo': doctores.getSexo(),
            'Nombre_de_usuario': doctores.getUsuario(),
            'Contrasena': doctores.getContraseña(),
            'Especialidad': doctores.getEspecialidad(),
            'Telefono': doctores.getTelefono(),
            }
            return(jsonify(objeto))
    salida = { "Mensaje": "No existe el usuario con ese nombre"}
    return(jsonify(salida))

#guardar un nuevo doctor
@app.route('/Nuevodoctor', methods=['POST'])
def Agregardoctor():
    global Doctores
    global Pacientes
    global Enfermeras
    nombre = request.json['Nombre']
    apellido = request.json['Apellido']
    nacimiento = request.json['Fecha_de_nacimiento']
    sexo = request.json['Sexo']
    usuario = request.json['Nombre_de_usuario']
    contraseña = request.json['Contrasena']
    especialidad = request.json['Especialidad']
    telefono = request.json['Telefono']
    buscado = False
    for i in range(len(Pacientes)):
        if usuario == Pacientes[i].getUsuario():
            buscado = True
            return jsonify({'Mensaje':'El nombre de usuario ya existe'})
        else:
            for i in range(len(Doctores)):
                if usuario == Doctores[i].getUsuario():
                    buscado = True
                    return jsonify({'Mensaje':'El nombre de usuario ya existe'})
                else:
                    for i in range(len(Enfermeras)):
                        if usuario == Enfermeras[i].getUsuario():
                            buscado = True
                            return jsonify({'Mensaje':'El nombre de usuario ya existe'})
    nuevod = doctores(nombre,apellido,nacimiento,sexo,usuario,contraseña,especialidad,telefono)
    Doctores.append(nuevod)
    return jsonify({'Mensaje':'Se agrego el usuario correctamente',})


# actualizar doctor
@app.route('/Actualizardoctor/<string:nombre>', methods=['PUT'])
def ActualizarDoctor(nombre):
    global Doctores
    for i in range(len(Doctores)):
        if nombre == Doctores[i].getUsuario():
            Doctores[i].setNombre(request.json['Nombre'])
            Doctores[i].setApellido(request.json['Apellido'])
            Doctores[i].setNacimiento(request.json['Fecha_de_nacimiento'])
            Doctores[i].setSexo(request.json['Sexo'])
            Doctores[i].setUsuario(request.json['Nombre_de_usuario'])
            Doctores[i].setContraseña(request.json['Contrasena'])
            Doctores[i].setEspecialidad(request.json['Especialidad'])
            Doctores[i].setTelefono(request.json['Telefono'])
            return jsonify({'Mensaje':'Se actualizo la informacion correctamente'})
    return jsonify({'Mensaje':'No se encontro el dato'})

# eliminar doctor
@app.route('/Eliminardoctor/<string:nombre>', methods=['DELETE'])
def EliminarDoctor(nombre):
    global Doctores
    for i in range(len(Doctores)):
        if nombre == Doctores[i].getUsuario():
            del Doctores[i]
            return jsonify({'Mensaje':'Se elimino el paciente correctamente'})
    return jsonify({'Mensaje':'No se encontro el dato'})

#----------------------------------------------------------------------------------------------------------------------------------------
#obtner todos los enfermaras
@app.route('/Enfermeras', methods=['GET'])
def getenfermera():
    global Enfermeras
    Datos = []
    for enfermeras in Enfermeras:
        objeto = {
            'Nombre': enfermeras.getNombre(),
            'Apellido': enfermeras.getApellido(),
            'Fecha_de_nacimiento': enfermeras.getNacimiento(),
            'Sexo': enfermeras.getSexo(),
            'Nombre_de_usuario': enfermeras.getUsuario(),
            'Contrasena': enfermeras.getContraseña(),
            'Telefono': enfermeras.getTelefono(),
        }
        Datos.append(objeto)
    return(jsonify(Datos))


#obtener solo un enfermera
@app.route('/Enfermeras/<string:nombre>', methods=['GET'])
def ObtenerEnfermera(nombre): 
    global Enfermeras
    for enfermeras in Enfermeras:
        if enfermeras.getUsuario() == nombre:
            objeto = {
            'Nombre': enfermeras.getNombre(),
            'Apellido': enfermeras.getApellido(),
            'Fecha_de_nacimiento': enfermeras.getNacimiento(),
            'Sexo': enfermeras.getSexo(),
            'Nombre_de_usuario': enfermeras.getUsuario(),
            'Contrasena': enfermeras.getContraseña(),
            'Telefono': enfermeras.getTelefono(),
            }
            return(jsonify(objeto))
    salida = { "Mensaje": "No existe el usuario con ese nombre"}
    return(jsonify(salida))

#guardar un nuevo enfermera
@app.route('/Nuevoenfermera', methods=['POST'])
def Agregarenfermera():
    global Enfermeras
    global Doctores
    global Pacientes
    nombre = request.json['Nombre']
    apellido = request.json['Apellido']
    nacimiento = request.json['Fecha_de_nacimiento']
    sexo = request.json['Sexo']
    usuario = request.json['Nombre_de_usuario']
    contraseña = request.json['Contrasena']
    telefono = request.json['Telefono']
    buscado = False
    for i in range(len(Pacientes)):
        if usuario == Pacientes[i].getUsuario():
            buscado = True
            return jsonify({'Mensaje':'El nombre de usuario ya existe'})
        else:
            for i in range(len(Doctores)):
                if usuario == Doctores[i].getUsuario():
                    buscado = True
                    return jsonify({'Mensaje':'El nombre de usuario ya existe'})
                else:
                    for i in range(len(Enfermeras)):
                        if usuario == Enfermeras[i].getUsuario():
                            buscado = True
                            return jsonify({'Mensaje':'El nombre de usuario ya existe'})
    nuevoe = enfermeras(nombre,apellido,nacimiento,sexo,usuario,contraseña,telefono)
    Enfermeras.append(nuevoe)
    return jsonify({'Mensaje':'Se agrego el usuario correctamente',})


# actualizar enfermera
@app.route('/Actualizarenfermera/<string:nombre>', methods=['PUT'])
def ActualizarEnfermera(nombre):
    global Enfermeras
    for i in range(len(Enfermeras)):
        if nombre == Enfermeras[i].getUsuario():
            Enfermeras[i].setNombre(request.json['Nombre'])
            Enfermeras[i].setApellido(request.json['Apellido'])
            Enfermeras[i].setNacimiento(request.json['Fecha_de_nacimiento'])
            Enfermeras[i].setSexo(request.json['Sexo'])
            Enfermeras[i].setUsuario(request.json['Nombre_de_usuario'])
            Enfermeras[i].setContraseña(request.json['Contrasena'])
            Enfermeras[i].setTelefono(request.json['Telefono'])
            return jsonify({'Mensaje':'Se actualizo la informacion correctamente'})
    return jsonify({'Mensaje':'No se encontro el dato'})

# eliminar enfermera
@app.route('/Eliminarenfermera/<string:nombre>', methods=['DELETE'])
def Eliminarenfermera(nombre):
    global Enfermeras
    for i in range(len(Enfermeras)):
        if nombre == Enfermeras[i].getUsuario():
            del Enfermeras[i]
            return jsonify({'Mensaje':'Se elimino el paciente correctamente'})
    return jsonify({'Mensaje':'No se encontro el dato'})

#----------------------------------------------------------------------------------------------------------------------------------------
#obtner todos los medicinas
@app.route('/Medicamentos', methods=['GET'])
def getMedicamento():
    global Medicamentos
    Datos = []
    for medicinas in Medicamentos:
        objeto = {
            'Id': medicinas.getId(),
            'Nombre': medicinas.getNombre(),
            'Precio': medicinas.getPrecio(),
            'Descripcion': medicinas.getDescripcion(),
            'Cantidad': medicinas.getCantidad()
        }
        Datos.append(objeto)
    return(jsonify(Datos))


#obtener solo un medicamento
@app.route('/Medicamentos/<string:nombre>', methods=['GET'])
def Obtenermedicina(nombre): 
    global Medicamentos
    for medicinas in Medicamentos:
        if medicinas.getId() == nombre:
            objeto = {
            'Nombre': medicinas.getNombre(),
            'Precio': medicinas.getPrecio(),
            'Descripcion': medicinas.getDescripcion(),
            'Cantidad': medicinas.getCantidad()
            }
            return(jsonify(objeto))
    salida = { "Mensaje": "No existe el medicamento con ese nombre"}
    return(jsonify(salida))

#guardar un nuevo medicamento
@app.route('/Nuevomedicamento', methods=['POST'])
def Agregarmedicina():
    global Medicamentos
    global contadormedica
    contadormedica=contadormedica+1
    id = str(contadormedica)
    nombre = request.json['Nombre']
    precio = float(request.json['Precio'])
    descripcion = request.json['Descripcion']
    cantidad = int(request.json['Cantidad'])
    nuevom = medicinas(id,nombre,precio,descripcion,cantidad)
    Medicamentos.append(nuevom)
    return jsonify({'Mensaje':'Se agrego el medicamento correctamente',})


# actualizar medicina
@app.route('/Actualizarmedicamento/<string:nombre>', methods=['PUT'])
def Actualizarmedicamento(nombre):
    global Medicamentos
    for i in range(len(Medicamentos)):
        if nombre == Medicamentos[i].getId():
            Medicamentos[i].setNombre(request.json['Nombre'])
            Medicamentos[i].setPrecio(request.json['Precio'])
            Medicamentos[i].setDescripcion(request.json['Descripcion'])
            Medicamentos[i].setCantidad(int(request.json['Cantidad']))
            return jsonify({'Mensaje':'Se actualizo la informacion correctamente'})
    return jsonify({'Mensaje':'No se encontro el dato'})

# actualizar medicina
@app.route('/Actualizarcantidad/<string:nombre>', methods=['PUT'])
def Actualizarcantidad(nombre):
    global Medicamentos
    for i in range(len(Medicamentos)):
        if nombre == Medicamentos[i].getId():
            cantidadactual= int(Medicamentos[i].getCantidad())
            Medicamentos[i].setCantidad(cantidadactual - int(request.json['Cantidad']))
            return jsonify({'Mensaje':'Se actualizo la informacion correctamente'})
    return jsonify({'Mensaje':'No se encontro el dato'})

# eliminar medicamento
@app.route('/Eliminarmedicamento/<string:nombre>', methods=['DELETE'])
def Eliminarmedicamento(nombre):
    global Medicamentos
    for i in range(len(Medicamentos)):
        if nombre == Medicamentos[i].getId():
            del Medicamentos[i]
            return jsonify({'Mensaje':'Se elimino el medicamento correctamente'})
    return jsonify({'Mensaje':'No se encontro el dato'})

#----------------------------------------------------------------------------------------------------------------------------------------

def buscarp(nombreb):
    global Pacientes
    for i in range(len(Pacientes)):
        if nombreb == Pacientes[i].getUsuario():
            print (nombreb)
            return Pacientes[i]
    return 'null'

def buscard(nombrec):
    global Doctores
    for i in range(len(Doctores)):
        if nombrec == Doctores[i].getUsuario():
            return Doctores[i]
    return 'null'

def buscare(nombree):
    global Enfermeras
    for i in range(len(Enfermeras)):
        if nombree == Enfermeras[i].getUsuario():
            return Enfermeras[i]
    return 'null'    
    


# Login
@app.route('/Inicio', methods=['PUT'])
def login():
    nombre = request.json['Nombre_de_usuario']
    contra = request.json['Contrasena']
    busqueda=buscarp(nombre)
    buscado=buscard(nombre)
    buscas=buscare(nombre)

    if nombre.lower() == "admin" and contra == "1234":
        return jsonify({'Mensaje':'administracion.html',})
    elif  busqueda!='null':
        if nombre==busqueda.getUsuario() and contra==busqueda.getContraseña():
            return jsonify({'Mensaje':'Paci.html',})
        else:
            return jsonify({'Mensaje':'Credenciales incorrectas',})
    elif buscado != 'null':
        if nombre==buscado.getUsuario() and contra==buscado.getContraseña():
            return jsonify({'Mensaje':'Doct.html',})
        else: 
            return jsonify({'Mensaje':'Credenciales incorrectas',})
    elif  buscas!='null':
        if nombre==buscas.getUsuario() and contra==buscas.getContraseña():
            return jsonify({'Mensaje':'enfe.html',})
        else:
            return jsonify({'Mensaje':'Credenciales incorrectas',})        
    else:
        return jsonify({'Mensaje':'El usuario no existe',})

#---------------------------------------------------------------------------------------------------------------------------------------
#ver un nuevo cita
@app.route('/Citas', methods=['GET'])
def getcita():
    global Citas
    Datos = []
    for citas in Citas:
        objeto = {
            'Id': citas.getId(),
            'Nombre': citas.getNombre(),
            'Fecha': citas.getFecha(),
            'Hora': citas.getHora(),
            'Motivo': citas.getMotivo(),
            'Estado': citas.getEstado()
        }
        Datos.append(objeto)
    return(jsonify(Datos))


#guardar un nuevo cita
@app.route('/Nuevacita', methods=['POST'])
def Agregarcita():
    global Citas
    global contadorcita
    contadorcita=contadorcita+1
    id=str(contadorcita)
    nombre = request.json['Nombre']
    fecha = request.json['Fecha']
    hora = request.json['Hora']
    motivo= request.json['Motivo']
    estado= request.json['Estado']
    for i in range(len(Citas)):
        if Citas[i].getNombre() == nombre and Citas[i].getEstado()!="Completada":
            if Citas[i].getNombre() == nombre and Citas[i].getEstado()!="Rechazada":
                return jsonify({'Mensaje':'El usuario ya tiene una cita existente'})  
    nuevac = citas(id,nombre,fecha,hora,motivo,estado)
    Citas.append(nuevac)
    return jsonify({'Mensaje':'Se agrego la cita correctamente',})


# actualizar cita
@app.route('/Actualizarcita/<string:nombre>', methods=['PUT'])
def Actualizarcita(nombre):
    global Citas
    for i in range(len(Citas)):
        if nombre == Citas[i].getId():
            Citas[i].setEstado(request.json['Estado'])
            return jsonify({'Mensaje':'Se Acepto la cita correctamente'})
    return jsonify({'Mensaje':'No se encontro el dato'})

#-----------------------------------------------------------------------------------------------------------------------------------------------------

#guardar un nuevo pedido
@app.route('/Nuevopedido', methods=['POST'])
def Agregarpedido():
    global Pedidos
    global contadorpedidos
    contadorpedidos=contadorpedidos+1
    nombre = str(contadorpedidos) 
    medicin =   request.json['Medicinas']
    nuevopd= pedidos(nombre,medicin)
    Pedidos.append(nuevopd)
    return jsonify({'Mensaje':'Se agrego el pedido',})

#obtner todos los pedidos
@app.route('/Pedidosa', methods=['GET'])
def getpedidos():
    global Pedidos
    Datos = []
    for pedidos in Pedidos:
        objeto = {
            'Nombre': pedidos.getNombre(),
            'Precio': pedidos.getMedicinas(),
        }
        Datos.append(objeto)
    return(jsonify(Datos))


#obtener los medicamentos del pedido
@app.route('/pedidos/<string:nombre>', methods=['GET'])
def Obtenermedicinas(nombre): 
    global Pedidos
    for pedidos in Pedidos:
        if pedidos.getNombre() == nombre:
            medicinass= pedidos.getMedicinas()
    objeto = {
        'Nombre': pedidos.getNombre(),
        'Medicamentos': medicinass
    }        
    return(jsonify(objeto))


#obtner todos las enfermedades
@app.route('/Enfermedades', methods=['GET'])
def getEnfermedades():
    global enfermedades
    Datos = []
    for i in range(len(enfermedades)):
        objeto = {
            'Nombre': enfermedades[i]
        }
        Datos.append(objeto)
    return(jsonify(Datos))






if __name__ == "__main__":
    app.run(host="0.0.0.0",port=3000, debug=True)