class Empresa():
    def __init__(self,nom="",ruc=0,dire="",tele=0,ciud="",tipEmpr=""):
        self.nombre=nom
        self.ruc=ruc
        self.direccion=dire
        self.telefono=tele
        self.ciudad=ciud
        self.tipoEmpresa=tipEmpr

    def datosEmpresa(self):#3
        self.nombre=input("Ingresar nombre de la empresa: ")
        self.ruc=int(input("Ingresar ruc de la empresa: "))
        self.direccion=input("Ingresar la direccion de la empresa: ")
        self.telefono=int(input("Ingresar el numero de telefono de la empresa: "))
        self.ciudad=input("Ingresar ciudad donde esta la empresa: ")
        self.tipoEmpresa=input("Ingresar tipo de empresa publica o privada: ")
    
    def mostrarEmpresa(self):
        print("")
        print("Datos de la Empresa")
        print("La empresa de nombre {}\n De RUC #{} \n Está ubicada en {}\n Se puede comunicar al #{}\n Está empresa esta en la ciudad de {}\n Es una entidad {}".format(self.nombre,self.ruc,self.direccion, self.telefono,self.ciudad, self.tipoEmpresa))

class Empleado(Empresa):
    def __init__(self,nom="",ruc=0,dire="",tele=0,email="",estado="",profe=""):
        self.nombre=nom
        self.ruc=ruc
        self.direccion=dire
        self.telefono=tele
        self.correo=email
        self.estadocivil=estado
        self.profesion=profe

    def empleado(self):
        self.nombre=input("Ingresar nombre del empleado: ")
        self.cedula=int(input("Ingresar numero de cedula del empleado: "))
        self.direccion=input("Ingresar la direccion del empleado: ")
        self.telefono=int(input("Ingresar numero de contacto del empleado: "))
        self.correo=input("Ingresar correo personal del empleado: ")

    def empleadoObrero(self): 
        self.estadocivil=input("Ingresar estado civil del empleado: ")

    def empleadoOficina(self):#falta dos atributo como definicion de oficina
      self.profesion=input("Ingresar profesion del empleado: ")

    def mostrarempleado(self):
        print("El empleado: {} con # de C.I. {} \n Con direccion {}, y numero de contacto{}\n Y correo {}".format(self.nombre,self.cedula,self.direccion,self.telefono,self.correo))
        if eleccion==1:
            print("De estado civil",self.estadocivil)
        elif eleccion==2:
            print("Con profesion de",self.profesion)  

class Departamento(Empleado):
    def __init__(self,dep=""):
        self.departamento=dep
    def departa(self):
        self.departamento=input("Ingresar el departamento al que pertenece el empleado: ")

    def mostrarDeparta(self):
        print("El empleado pertenece al departamento de: {}".format(self.departamento))

class Pagos(Empleado):
    def __init__(self, desc=0,desper=0,valhora=0,hotraba=0,extra=0):
        self.descuentos=desc
        self.permisos=desper
        self.valorhora=valhora
        self.horastrabajadas=hotraba
        self.valextra=extra

    def pagoNormal(self):
        self.valorhora=float(input("Ingresar valor a pagar por cada hora: "))
        self.horaestimada=int(input("Ingresar horas normales trabajadas: "))
        
        
    def pagoExtra(self):
        self.horastrabajadas=int(input("Ingresar horas extras trabajada: "))
        self.valextra=float(input("Ingresar valor por cada hora extra: "))

    def calculoSueldo(self,tt1=0,tt2=0):
        self.tt1=self.valorhora*self.horaestimada
        self.tt2=self.valextra*self.horastrabajadas
sueldo = Sueldo del empleado
# valor_hora = sueldo/240
# Sobretiempo = valor_hora * (horasRecargo*0.50+horasExtraordinarias*2)
# comisionEmpOficina =  Deducciones.comision*sueldo
# antiguedadEmpObrero = Deducciones.antiguedad*(FechaNomina - FechaIngreso)/365*sueldo
# iessEmpleado = Deducciones.iess*(sueldo+sobretiempo)
# prestamoEmpleado = cuota del prestamo
# toting = sueldo+sobretiempo+ comisionEmpOficina+ antiguedadEmpObrero
# totdes = iessEmpleado + prestamoEmpleado
# liquidoRecibir = toting - totdes


    def mostrarSueldo(self):
        print(self.tt1,self.tt2)
        #self.bono=incentivos
#         self.descuentos=desc
#         self.permisos=desper
#         self.bono=incentivos

emp=Empresa()
emp.datosEmpresa()
emp.mostrarEmpresa()
print("")
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
pag=Pagos()
pag.pagoNormal()
inf=int(input("El trabajador trabajo horas 1.Si o cualquier otro numero.No"))
if inf==1:
    pag.pagoExtra()
else:
    pass    
pag.calculoSueldo()
pag.mostrarSueldo()