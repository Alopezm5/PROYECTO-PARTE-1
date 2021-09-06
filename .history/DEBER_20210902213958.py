class Nomina: 
    def __init__(self,nom="",ruc=0,dire="",tele=0,ciud="",tipEmpr="",email="",estado="",profe="",dep="", valhora=0,hotraba=0):#3
        self.nombre=nom
        self.ruc=ruc
        self.direccion=dire
        self.telefono=tele
        self.ciudad=ciud
        self.tipoEmpresa=tipEmpr
        self.correo=email
        self.estadocivil=estado
        self.profesion=profe
        self.departamento=dep
        self.valorhora=valhora
        self.horastrabajadas=hotraba
        # self.descuentos=desc
        # self.permisos=desper

class Empresa(Nomina):
    def datosEmpresa(self):#3
        self.nombre=input("Ingresar nombre de la empresa: ")
        self.ruc=int(input("Ingresar ruc de la empresa: "))
        self.direccion=input("Ingresar la direccion de la empresa: ")
        self.telefono=int(input("Ingresar el numero de telefono de la empresa: "))
        self.ciudad=input("Ingresar ciudad donde esta la empresa: ")
        self.tipoEmpresa=input("Ingresar tipo de empresa publica o privada: ")
    
    def mostrarEmpresa(self):
        print("Datos de la Empresa")
        print("La empresa {}\n De RUC #{} \n Está ubicada en {}\n Se puede comunicar al #{}\n Está empresa esta en la ciudad de {}\n Es una entidad {}".format(self.nombre,self.ruc,self.direccion, self.telefono,self.ciudad, self.tipoEmpresa))

class Departamento(Empleado):
    def departa(self):
        self.departamento=input("Ingresar el departamento al que pertenece el empleado: ")

    def mostrarDeparta(self):
        print("El empleado pertenece al departamento de: {}".format(self.departamento))

class Empleado(Nomina):
    def empleado(self):
        self.nombre=input("Ingresar nombre del empleado: ")
        self.cedula=int(input("Ingresar numero de cedula: "))
        self.direccion=input("Ingresar la direccion del empleado: ")
        self.telefono=int(input("Ingresar numero de contacto del empleado: "))
        self.correo=input("Ingresar correo personal del empleado: ")

    def empleadoObrero(self): 
        self.estadocivil=input("Ingresar estado civil del empleado: ")

    def empleadoOficina(self):#falta dos atributo como definicion de oficina
      self.profesion=input("Ingresar profesion del empleado: ")

    def mostrarempleado(self):
        print("El empleado: {} con # de C.I. {} \n Con direccion {}, y numero de contacto{}\n Y correo {} \n".format(self.nombre,self.cedula,self.direccion,self.telefono,self.correo))
        if eleccion==1:
            print("De estado civil",self.estadocivil)
        elif eleccion==2:
            print("Con profesion de",self.profesion)   

class Pagos(Nomina):
#     def pagoNormal(self):
#        
        
#     def pagoExtra(self, valhora,hoesti,hotraba,incentivos):
#         self.valorhora=valhora
#         self.horaestimada=hoesti
#         self.horastrabajadas=hotraba
#         self.bono=incentivos

#     def Nomina(self, nom, valhora,hoesti,hotraba, desc, desper,incentivos):#faltan 8 atributos incluir cosas del empleado y  sobretiempo
#         self.nombre= nom
#         self.valorhora=valhora
#         self.horaestimada=hoesti
#         self.horastrabajadas=hotraba
#         self.descuentos=desc
#         self.permisos=desper
#         self.bono=incentivos


nomi=Nomina()
emp=Empresa()
emp.datosEmpresa()
emp.mostrarEmpresa()
emple=Empleado()
emple.empleado()
eleccion=int(input("Va a ingresar un empleado tipo 1. Obreo o 2.Oficina: "))
if eleccion==1:
    emple.empleadoObrero()
elif eleccion==2:
    emple.empleadoOficina()
else:
    print("No selecciono el tipo de empleado")
emple.mostrarempleado()