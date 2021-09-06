class Empresa:
    def __init__(self,nom,ruc,dir,tele,ciud,tipEmpr):#3
        self.nombre=nom
        self.ruc=ruc
        self.direccion=dir
        self.telefono=tele
        self.ciudad=ciud
        self.tipoEmpresa=tipEmpr

    def datosEmpresa(self):#3
        self.nombre=input("Ingresar nombre de la empres")
        self.ruc=ruc
        self.direccion=dir
        self.telefono=tele
        self.ciudad=ciud
        self.tipoEmpresa=tipEmpr

# class Empleado():
#     def __init__(self):
#         pass

#     def empleado(self,nom,ced,dir,tele):
#         self.nombre=nom
#         self.cedula=ced
#         self.direccion=dir
#         self.telefono=tele

#     def empleadoObrero(self,nom,ced,dir,tele,email,estado): 
#         self.nombre=nom
#         self.cedula=ced
#         self.direccion=dir
#         self.telefono=tele
#         self.correo=email
#         self.estadocivil=estado

#     def empleadoOficina(self,nom,ced,dir,tele):#falta dos atributo como definicion de oficina
#         self.nombre=nom
#         self.cedula=ced
#         self.direccion=dir
#         self.telefono=tele

# class Departamento(2):
#     def __init__(self):
#         pass

# class Pagos():
#     def __init__(self):
#         pass

#     def pagoNormal(self, valhora,hoesti,hotraba, desc, desper):
#         self.valorhora=valhora
#         self.horaestimada=hoesti
#         self.horastrabajadas=hotraba
#         self.descuentos=desc
#         self.permisos=desper
        
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



emp=Empresa()
emp.datosEmpresa()
# emple=Empleado()
# emple.empleado()
# emple.empleadoObrero()
# emple.empleadoOficina()

